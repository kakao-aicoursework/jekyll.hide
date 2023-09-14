import reflex as rx


class WebuiConfig(rx.Config):
    pass


config = WebuiConfig(
    app_name="chatbot",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    frontend_packages=[
        "react-loading-icons",
    ],
)
