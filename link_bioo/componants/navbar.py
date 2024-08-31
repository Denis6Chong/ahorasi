import reflex as rx
import link_bioo.styles.styles as styles
from link_bioo.styles.styles import Size as Size
from link_bioo.styles.colors import Color as Color
from link_bioo.styles.colors import TextColor as TextColor
import link_bioo.styles.styles as styles
from link_bioo.routes import Route
from link_bioo.componants.ant_components import float_button
import link_bioo.constanst as constants


def navbar() -> rx.Component:
    return rx.vstack(
        rx.link( 
        rx.chakra.box(
    rx.chakra.span("papi", color=Color.PRIMARY.value),

    rx.chakra.span("chong", color=Color.SECONDARY.value),
    styles=styles.narvar_title_style
    ),
    href=Route.INDEX.value
),
        float_button(
            
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    ) 