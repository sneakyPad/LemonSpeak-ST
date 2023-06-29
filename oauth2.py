import base64
import requests
import streamlit as st
from oauthlib.oauth2 import WebApplicationClient
import custom_markdown
import jwt
from authlib.integrations.requests_client import OAuth2Session


client_id = st.secrets.auth0_credentials.AUTH0_CLIENT_ID
client_secret = st.secrets.auth0_credentials.AUTH0_CLIENT_SECRET
authorization_endpoint = st.secrets.auth0_credentials.AUTH0_DOMAIN
token_endpoint = st.secrets.auth0_credentials.AUTH0_TOKEN_ENDPOINT

redirect_uri =st.secrets.url.redirect_url
client = WebApplicationClient(client_id)


def google_as_identity_provider():
    authorization_url = client.prepare_authorization_request(
        authorization_url=authorization_endpoint,
        redirect_url=redirect_uri,
        scope=['profile', 'email'],
        access_type='offline',
    )
    return authorization_url[0]


def oauth0_as_identity_provider():
    oauth = OAuth2Session(client_id, client_secret, scope='openid profile email offline_access')
    authorization_url, state = oauth.create_authorization_url(f'https://{authorization_endpoint}/authorize',
                                                              redirect_uri=redirect_uri,
                                                              audience =
                                                              f'https://{authorization_endpoint}/api/v2/',
                                                              )

    return authorization_url

# Define a function to initiate the authentication flow

def render_authentication_btn():
    google_button_id = custom_markdown.google_button_id
    authorization_url = oauth0_as_identity_provider()
    # authorization_url = google_as_identity_provider()

    print(f'{authorization_url}')
    button_text = "Sign Up"
    link_html = f'<a id="{google_button_id}" href="{authorization_url}">{button_text}</a>'
    dl_link =custom_markdown.create_custom_css()+f'<div id="btn_wrapper"><div id="div_auth">{link_html}</div></div>'
    st.markdown(dl_link, unsafe_allow_html=True)


def get_user_id_email(access_token):
    decoded = jwt.decode(access_token, options={"verify_signature": False})
    user_id = decoded.get("sub")
    email = decoded.get("https://test/email")
    return user_id, email


# Define a function to exchange the authorization code for an access token
def exchange_code_for_access_token(get_session):
    # Get the authorization code from the query parameters
    code = st.experimental_get_query_params().get('code', None)
    if code is None or code[0] == 'refresh':
        return None

    # Exchange the authorization code for an access token
    token_url = token_endpoint
    token_response = requests.post(
        token_url,
        data=client.prepare_request_body(
            code=code[0],
            redirect_uri=redirect_uri,
            client_secret=client_secret,
        ),
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )


    client.parse_request_body_response(token_response.text)
    access_token = client.token['access_token']
    refresh_token = client.token['refresh_token']
    user_id, email = get_user_id_email(access_token)
    # Store the access token in the session state
    # session_state.token = access_token
    get_session().token = access_token
    get_session().refresh_token = refresh_token
    get_session().user_id = user_id
    get_session().email = email
    print(f'session_state : {get_session()}')
    st.experimental_rerun()


def exchange_refresh_token_with_access_token(get_session):
    # Exchange the refresh token for a new access token
    token_url = token_endpoint
    token_response = requests.post(
        token_url,
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': get_session().refresh_token,
            'grant_type': 'refresh_token',
        }
    )

    get_session().token = token_response.json()['access_token']
