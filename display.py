import streamlit as st
from streamlit_extras.mention import mention


def sample():
    st.markdown(f'#### Showcase of an Uploaded Episode 🎙️')
    st.write(f"<b>Here's an example of the speech, John F. Kennedy gave in Berlin 1963. We'll treat "
             f"this speech as if it were a podcast. </b>",
             unsafe_allow_html=True)
    img_col1, img_col2, img_col3 = st.columns(3)
    with img_col2:
        st.image('resources/jfkennedyimg.png', caption='President John F. Kennedy delivers his '
                                                       'famous speech "I am a Berliner"')
    st.audio('resources/jfkberlinspeech.mp3')

    with open('resources/Summary John F Kennedy.txt', 'r') as f:
        summary = f.read()

    with open('resources/Transcript John F Kennedy.txt', 'r') as f:
        transcript = f.read()

    st.markdown(f'#### The Generated Transcript 📑 \n<i>{transcript}</i>', unsafe_allow_html=True)
    st.markdown(f'#### The Generated Summary 📃\n<i>{summary}</i>', unsafe_allow_html=True)


def render_follow_me():
    inline_twitter = mention(
        label="Twitter",
        icon="twitter",  # Twitter is also featured!
        url="https://www.twitter.com/paer06",
        write=False
    )
    inline_linkedin = mention(
        label="LinkedIn",
        icon="https://play-lh.googleusercontent.com/kMofEFLjobZy_bCuaiDogzBcUT-dz3BBbOrIEjJ"
             "-hqOabjK8ieuevGe6wlTD15QzOqw=w480-h960-rw",
        url="https://www.linkedin.com/in/patrick-m-snp/",
        write=False
    )
    inline_substack = mention(
        label="Substack",
        icon="https://camo.githubusercontent.com/3d4121e2061fe8a37e532bc8485e2ef0f8dbfaa26fe0f7e53f755df91d8a4333/68747470733a2f2f737562737461636b2e636f6d2f696d672f737562737461636b2e706e67",
        url="https://sneakypad.substack.com/",
        write=False
    )
    st.divider()
    st.write(f"For more content follow me or subscribe: {inline_twitter} {inline_linkedin} {inline_substack}",
                     unsafe_allow_html=True, )

def render_more_apps():
    inline_podgrader = mention(
        label="Podcast Grader - An Audio Quality Grader",
        icon="🚦",  # Twitter is also featured!
        url="https://bit.ly/podcast-grader",
        write=False
    )
    inline_titlegrader = mention(
        label="Title Grader - Improve The Title Of An Episode",
        icon="✍️",  # Twitter is also featured!
        url="https://bit.ly/episode-title-grader",
        write=False
    )
    st.divider()
    st.markdown(f'#### Pssst! 🤫', unsafe_allow_html=True)
    st.write(f"Here are more free apps for you 🥳! {inline_podgrader} {inline_titlegrader}",
                     unsafe_allow_html=True, )

def render_subscribe_button():
    subscribe_id = 'subscribe'
    button_text = 'Subscribe For More 🎙️💌'
    custom_css = f"""
                <style>
                #btn_wrapper {{
                    text-align: center;
                }}
                #div_subscribe {{
                    display: inline-block;
                    align-items: center;
                    background-color: white;
                    color: black;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-style: solid;
                    border-color: rgb(152, 152, 152);
                    border-image: initial;
                }}

                #div_subscribe:hover {{
                    background-color: darkgreen;
                    color: white;
                    border-color: darkgreen;
                }}

                #{subscribe_id} {{
                    background-color: white;
                    color: black;
                    padding: 4pt 20pt;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-color: rgb(230, 234, 241);
                    border-image: initial;
                    display: inline-block;
                    align-items: center;
                }}
                #{subscribe_id}:hover {{
                    background-color: darkgreen;
                    color: white;
                    border-color: darkgreen;
                }}
                #{subscribe_id}:active {{
                    box-shadow: none;
                    background-color: darkgreen;
                    color: white;
                }}
                </style> """

    link_html = f'<a id="{subscribe_id}" href={st.secrets.url.subscription_substack}>{button_text}</a>'
    dl_link = custom_css + f'<div id="btn_wrapper"><div id="div_subscribe">{link_html}</div></div>'
    st.markdown(dl_link, unsafe_allow_html=True)