import reflex as rx
from link_bioo.styles.colors import Color as Color
from link_bioo.styles.colors import TextColor as TextColor

from link_bioo.styles.styles import Size as Size

def info_text(inicio: None, title: str, title2: str, body:str) -> rx.Component:
    return rx.chakra.box(
                        inicio,
                        rx.chakra.span(f" {title} ", color=TextColor.HEADER.value ,font_weight="bold"), 
                        rx.chakra.span(f" {title2} ", color=Color.SECONDARY.value, font_weight="bold"),
                        body, font_size=Size.MEDIUM.value, color=TextColor.BODY.value
)

    



