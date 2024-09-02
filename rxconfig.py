import reflex as rx

config = rx.Config(
    app_name="link_bioo",
    cors_allowed_origins=[
        "https://chong-web.vercel.app",
        "http://localhost:3000"
    ]
)  