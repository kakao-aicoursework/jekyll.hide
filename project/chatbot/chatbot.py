import reflex as rx

from chatbot import styles, components
from chatbot.state import State


def index() -> rx.Component:
    """The main app."""
    return rx.vstack(
        components.chat(),
        components.action_bar(),
        bg=styles.bg_color,
        color=styles.text_color,
        min_h='100vh',
        spacing="0",
        align_items="stretch",
        justify_content="space-between"
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
