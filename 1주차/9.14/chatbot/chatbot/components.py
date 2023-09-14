import reflex as rx

from chatbot import styles
from chatbot.state import QA, State


def message(qa: QA) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                qa.question,
                bg=styles.my_message_color,
                **styles.message_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.text(
                qa.answer,
                bg=styles.bot_message_color,
                **styles.message_style,
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )


def chat() -> rx.Component:
    return rx.vstack(
        rx.box(rx.foreach(State.chats[State.current_chat], message)),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
        align_items="stretch"
    )


def action_bar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.form(
                rx.hstack(
                    rx.input(
                        placeholder="챗봇에게 질문해보세요!",
                        id="question",
                        _placeholder={"color": "#111"},
                        style=styles.button_style,
                    ),
                    rx.button(
                        rx.text("Send"),
                        type_="submit",
                        style=styles.button_style,
                    ),
                ),
                on_submit=[State.process_question, rx.set_value("question", "")],
                width="100%",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        backdrop_filter="auto",
        backdrop_blur="lg",
        border_top=f"1px solid {styles.border_color}",
        align_items="stretch",
        width="100%",
    )
