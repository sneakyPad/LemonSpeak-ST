# from _session_state import SessionState
import requests
# ---- oauth2
import requests
import streamlit as st
import custom_markdown
import oauth2
import time
# --- end oauth2
from streamlit_tags import st_tags, st_tags_sidebar
import streamlit_analytics
import display
import toml2json


class SessionState:
    def __init__(self):
        self.token = None
        self.refresh_token = None
        self.user_id = None
        self.email = None



# session_state = SessionState()
def create_session():
    return SessionState()

#
# @st.cache_resource()
# def get_session():
#     # session = create_session()
#     return SessionState()

def get_session():
    return st.session_state
if "token" not in st.session_state:
    st.session_state.token = None
if "refresh_token" not in st.session_state:
    st.session_state.refresh_token = None
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "email" not in st.session_state:
    st.session_state.email = None
if "page_load_time" not in st.session_state:
    st.session_state.page_load_time = time.time()

# st.experimental_set_query_params(code = 'refresh')

from io import BytesIO
from PIL import Image

def display_user_information_simple():
    # print(f'session_state after rerun: {get_session()}')

    if get_session().token is not None:
        try:
            oauth2.exchange_refresh_token_with_access_token(get_session)
            st.markdown(f'##### Welcome 👋')
            # Display user information with rounded border
            response ={}
            response['name']=''

            import base64

            with open("images/pink_avatar.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())

            # image = Image.open("green_avatar.png")
            pre = 'data:image/png;base64,'
            # faux_file = BytesIO()

            response['picture']=pre+encoded_string.decode("utf-8")
            response['email']=get_session().email
            st.markdown(custom_markdown.create_user_information(response),
                        unsafe_allow_html=True)
            # st.write(f"Name: {response['name']}")
            # st.write(f'E-Mail: {response["email"]}')
            # st.image(response['picture'], width=50)

            # st.write(f'You are logged in as {email}.')
        except Exception as e:
            print(f'Exception: {e}')
            print(f'Could not fetch user information.')
            print(f'Reset token and session token')
            get_session().token = None
            get_session().refresh_token = None



def fetch_user_info_auth0():
    no_tries = 3
    for i in range(no_tries):
        # Use the access token to retrieve the user's profile information
        user_id = get_session().user_id
        user_url = f'https://{st.secrets.auth0_credentials.AUTH0_DOMAIN}/userinfo' \
                   f'/{user_id}'

        profile_response = requests.get(
            user_url + "?scope=read:users",
            headers={"Authorization": f"Bearer {get_session().token}",
                     "scope": "read:users",
                     },
        )
        response = profile_response.json()

        if profile_response.status_code != 200:
            print(f'Refreshing access_token based on response: {profile_response.status_code}')
            oauth2.exchange_refresh_token_with_access_token(get_session)

        if profile_response.status_code == 200:
            return response
    raise Exception

def check_health():
    try:
        response = requests.get(st.secrets.url.core_ready)
        if response.status_code != 200:
            return False
        return True
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        return False
toml2json.parse_firestore_toml_to_json()
with streamlit_analytics.track(unsafe_password=st.secrets.tracking.pw,
                                  firestore_key_file=".streamlit/fs_key.json",
                                  firestore_collection_name="lemonspeak"):
    # streamlit_analytics.start_tracking()
    # -------------- SETTINGS --------------
    page_title = "LemonSpeak "
    lemon_speak_icon = ":lemon:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
    podcast_icon = ":studio_microphone:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
    page_icon = ":rocket:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
    layout = "centered"
    # ---

    st.markdown(f"<h1 style='text-align: center;'>{page_title} 🍋 🎙️</h1>", unsafe_allow_html=True)

    st.markdown(f"<h3 style='text-align: center'>Transcribe and Summarize your Podcast</h3>",
                unsafe_allow_html=True)
    # display_user_information()
    display_user_information_simple()
    st.markdown("""---""")

    st.write(
        "With LemonSpeak, you can effortlessly upload your podcast 🎙️, receive a concise summary 📝, and "
        "diarized transcription 🗣️. By enhancing your content's SEO value 🔍, LemonSpeak helps you grow "
        "your audience 📈 and makes your podcast more engaging. "
        )
    st.write("""##### How it works⚙️\n
        \n1. Head over to the left sidebar ⬅️ and upload your episode as an MP3 file
             \n2. Fill in the necessary metadata
             \n3. Don't forget to tell us the email address where we should send your 
             results.""", unsafe_allow_html=True)
    health = check_health()
    if not health:
        st.error("The service is currently unavailable due to maintenance. Please try again later.",
                 icon="⚠️")
        st.stop()

    st.markdown("""---""")

    # st.error('Our service is presently undergoing maintenance. Normal operations will resume shortly. We appreciate your patience.', icon="⚠️")


    st.sidebar.markdown('### Upload your Episode 🆙')
    mp3_file = st.sidebar.file_uploader('Currently only mp3 as a format is supported', type=["mp3"])
    st.sidebar.divider()


    # if get_session().token is not None:
    st.sidebar.markdown('### Additional Metadata 🤗')
    language = st.sidebar.selectbox('Select the language in which the podcast was recorded', ['English',
                                                                                         'German'])
    # st.sidebar.markdown("""---""")

    if language == 'English':
        language = 'en'
    else:
        language = 'de'
    # https://github.com/gagan3012/streamlit-tagsExa
    speaker_names = st_tags_sidebar(
        label='Enter the names of all speakers in your podcast 👥',
        text='Press enter to add more',
        maxtags=9,
    )

    st.sidebar.divider()

    email =st.sidebar.text_input(label='Email Address 💌', placeholder='Please enter your email address to receive the results')


    no_speaker = len(speaker_names)
    # col1, col2, col3 = st.columns([1, 1, 1])
    # password = col2.text_input("Enter a password", type="password")
    if st.sidebar.button(f"Submit your Podcast {page_icon}"):
        if email == '' or not '@' in email:
            st.sidebar.error('Please provide an email address', icon='❗️')
            st.stop()
        if mp3_file is None:
            st.sidebar.error('Please upload your file as .mp3', icon='❗️')
            st.stop()
        if no_speaker == 0:
            st.sidebar.error('You need to at least specify one speaker.', icon='❗️')
            st.stop()

        print(f'MP3File: {mp3_file.name}')
        # headers with auth token
        # headers = {"Authorization": f"Bearer {get_session().token}", "accept": "application/json"}
        headers = { "accept": "application/json"}

        files = {"file": (mp3_file.name, mp3_file, "audio/mpeg")}
        data = {'speaker_names': speaker_names, }
        print(f'Language: {language}')
        params = {"no_speaker": no_speaker, 'password': st.secrets.core_auth.pw, 'language': language, "current_user": email}

        try:
            with st.spinner('Uploading your podcast (this will take a couple of minutes) ...'):

                response = requests.post(st.secrets.url.core, params=params, headers=headers, files=files,
                                     data=data, timeout=600)

            if response.status_code == 200:
                data = response.json()
                st.success(data['message'], icon="✅")
                # st.balloons()
                print(data)
            else:
                print(f"Error {response.status_code}: {response.reason}")
                data = response.json()
                st.warning(data['message'], icon='❗️')
                st.snow()
        except Exception as e:
            print(f'Response: {response}')
            print(f'Exception: {e}')
    else:
        display.sample()

    display.render_follow_me()
    display.render_subscribe_button()
    display.render_more_apps()


    # streamlit_analytics.stop_tracking()
    # st.markdown("""---""")
    # st.write(vars(get_session()))

    # if get_session().token is None:
    #     # Authenticate the user and exchange the authorization code for an access token
    #     st.write("Sing up for our Beta and get three transcriptions for free.")
    #     oauth2.render_authentication_btn()
    #     oauth2.exchange_code_for_access_token(get_session)

    # TODO look at st.experimental_user
    # https://docs.streamlit.io/library/api-reference/personalization/st.experimental_user
    # st.experimental_user is a Streamlit command that returns information about the logged-in user on Streamlit Community Cloud. It allows developers to personalize apps for the user viewing the app. In a private Streamlit Community Cloud app, it returns a dictionary with the viewer's email. This value of this field is empty in a public Streamlit Community Cloud app to prevent leaking user emails to developers.
