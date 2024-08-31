import reflex as rx
from link_bioo.styles.styles import Size as Size
from link_bioo.styles.colors import Color as Color
from link_bioo.styles.colors import TextColor as TextColor
import datetime


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link("loviu", href="youtube.com",
        is_external=True,
        font_size=Size.MEDIUM.value,
        color=Color.SECONDARY.value), 

        rx.text(f"{datetime.date.today().year} sdkjasndakkc funsteks dmalsk skkfa iloviu ashd acnamalia",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value,
                color=TextColor.HEADER.value)))

    