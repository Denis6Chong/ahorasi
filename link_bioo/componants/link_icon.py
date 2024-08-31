import reflex as rx
import link_bioo.styles.styles as styles

def link_icon(direc: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(src=direc, width="1.5em"
        ),
        href=url,
        is_external=True
    )

