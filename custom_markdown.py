google_button_id = 'google_oauth'
streamlit_red = 'rgb(255, 75, 75)'


def create_user_information(response):
    return f"""
        <div style="
            border-radius: 10px;
            border: 1px solid {streamlit_red};
            padding: 10px;
            background-color: #F5F5F5;
            display: flex;
            align-items: center;
            ">
            <img src='""" + response['picture'] + """' width='75' style='border-radius: 50%;'>
            <div style='margin-left: 10px;'>
                <h3>""" + response['name'] + """</h3>
                <p>""" + response['email'] + """</p>
            </div>
        </div>
        """



def create_custom_css():

    custom_css = f"""
        <style>
        #btn_wrapper {{
            text-align: center;
        }}
        #div_auth {{
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

        #div_auth:hover {{
            background-color: darkgreen;
            color: white;
            border-color: darkgreen;
        }}

        #div_icon {{
            background-color: white;
            border-top-left-radius: 3px;
            border-bottom-left-radius: 3px;
            height: 100%;
        }}
        #{google_button_id} {{
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
        #{google_button_id}:hover {{
            background-color: darkgreen;
            color: white;
            border-color: darkgreen;
        }}
        #{google_button_id}:active {{
            box-shadow: none;
            background-color: darkgreen;
            color: white;
        }}
        </style> """
    return custom_css


def _create_custom_css():

    custom_css = f"""
        <style>
        #btn_wrapper {{
            text-align: center;
        }}
        #div_auth {{
            display: inline-block;

            align-items: center;

             background-color: rgb(75, 124, 224);
                color: white;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;

            }}

          #div_auth:hover {{
                border-color: {streamlit_red};
                # red is: rgb(246, 51, 102)
                # color: rgb(246, 51, 102);
                color: blue;
            }}

        #div_icon{{
                background-color: white;
                border-top-left-radius: 3px;
                border-bottom-left-radius: 3px;
                height: 100%;
                # width: 20px;

        }}
            #{google_button_id} {{
                background-color: rgb(75, 124, 224);
                # color: rgb(38, 39, 48);
                color: white;
                padding: 4pt 20pt;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                # border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;
                # width: 200px;
                display: inline-block;
                align-items: center;

            }}
            #{google_button_id}:hover {{
                # border-color: rgb(246, 51, 102);
                border-color: yellow;
                # color: rgb(246, 51, 102);
                border-color: yellow;
            }}
            #{google_button_id}:active {{
                box-shadow: none;
                # background-color: rgb(246, 51, 102);
                background-color: yellow);
                color: white;
                }}
        </style> """
    return custom_css

    def create_custom_css_google():
        custom_css = f"""
            <style>
            #btn_wrapper {{
                text-align: center;
            }}
            #div_auth {{
                display: inline-block;

                align-items: center;

                 background-color: rgb(75, 124, 224);
                    # color: rgb(38, 39, 48);
                    color: white;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-style: solid;
                    border-color: rgb(230, 234, 241);
                    border-image: initial;
                    height: 50px;

                }}

              #div_auth:hover {{
                    border-color: {streamlit_red};
                    # red is: rgb(246, 51, 102)
                    # color: rgb(246, 51, 102);
                    color: blue;
                }}

            #div_icon{{
                    background-color: white;
                    border-top-left-radius: 3px;
                    border-bottom-left-radius: 3px;
                    height: 100%;
                    # width: 20px;

            }}
                #{google_button_id} {{
                    background-color: rgb(75, 124, 224);
                    # color: rgb(38, 39, 48);
                    color: white;
                    padding: 0.25em 0.38em;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    # border-style: solid;
                    border-color: rgb(230, 234, 241);
                    border-image: initial;
                    # width: 200px;
                    display: inline-block;
                    align-items: center;

                }}
                #{google_button_id}:hover {{
                    # border-color: rgb(246, 51, 102);
                    border-color: yellow;
                    # color: rgb(246, 51, 102);
                    border-color: yellow;
                }}
                #{google_button_id}:active {{
                    box-shadow: none;
                    # background-color: rgb(246, 51, 102);
                    background-color: yellow);
                    color: white;
                    }}
            </style> """
        return custom_css
    # custom_css = f"""
    #         <style>
    #             #{google_button_id} {{
    #                 background-color: rgb(75, 124, 224);
    #                 color: white;
    #                 padding: 0.25em 0.38em;
    #                 position: relative;
    #                 text-decoration: none;
    #                 border-radius: 4px;
    #                 border-width: 1px;
    #                 border-style: solid;
    #                 border-color: rgb(230, 234, 241);
    #                 border-image: initial;
    #                 width: 200px;
    #                 margin: 10px;
    #                 display: flex;
    #                 align-items: center;
    #             }}
    #             #{google_button_id}:hover {{
    #                 border-color: rgb(246, 51, 102);
    #                 color: rgb(246, 51, 102);
    #             }}
    #             #{google_button_id}:active {{
    #                 box-shadow: none;
    #                 background-color: rgb(246, 51, 102);
    #                 color: white;
    #             }}
    #             #{google_button_id}::before {{
    #                 content: "\\f1a0";
    #                 font-family: "Font Awesome 5 Brands";
    #                 font-weight: 900;
    #                 margin-right: 10px;
    #             }}
    #         </style> """
