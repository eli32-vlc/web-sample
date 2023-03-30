"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass




style = {
    "font_family": "Comic Sans MS",
    "font_size": "16px",
}

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("This is Eason's portfolio", font_size="6em"),
            pc.text("I am a member of sheldon college.", font_size="4em"),
            pc.text("I like to code", font_size="4em"),
            pc.text("I like to publish my code on github, my github account is eli32-vlc", font_size="4em"),
            pc.text("This website is madeout of pynecone framework", font_size="4em"),
            pc.text("cool right!😉", font_size="4em"),
        )
    )   


def infor() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("Hosted on the macbook air")
        )
    )

def admin() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("Admin Portal"),
            pc.text("not available at this time"),
            pc.text("need to create a new account using the command line")
        )
    )
    
    
# Add state and page to the app.
app = pc.App(state=State, style=style)
app.add_page(index)
app.add_page(admin)
app.add_page(infor)
app.compile()
