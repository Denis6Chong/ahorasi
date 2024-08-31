import reflex as rx
import link_bioo.styles.styles as styles
import link_bioo.componants.link_icon as link_icon
from link_bioo.componants.info_text import info_text
from link_bioo.styles.colors import TextColor as TextColor
import link_bioo.constanst as const
import datetime


def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(fallback="DC", color_scheme="crimson", size="xl"),
                        rx.vstack(
                        
                                rx.heading(
                                        "Denis Chong",
                                        size="lg",
                                        color=TextColor.HEADER.value),
                                rx.text(
                                        "@denischong",
                                        color=TextColor.HEADER.value,
                                        margin_top="0px !important",
                                        
                                ),
                                rx.hstack(
                                        rx.link(
                                                rx.image(src="/facebook-logo-bold-svgrepo-com.svg", width="1.5em"), 
                                                href="facebook.com",
                                                is_external=True
                                        ),
                                        rx.link(
                                                rx.image(src="/instagram-logo-facebook-2-svgrepo-com.svg", width="1.5em"), 
                                                href="instagram.com",
                                                is_external=True


                                        ),
                                        rx.link(
                                                rx.image(src="/twitter-logo-bold-svgrepo-com.svg", width="1.5em"), 
                                                href="x.com",
                                                is_external=True


                                        ),
                                        rx.link(
                                                rx.image(src="/youtube-logo-svgrepo-com.svg", width="1.5em"), 
                                                href="youtube.com",
                                                is_external=True


                                        ),
                                       


                                        
                        
                                ),

                        align_items="start"),
                
                        

                ),

                rx.flex(
                        rx.vstack(
                                info_text("Hola","+", "jevas metias", ""),
                                rx.spacer(),
                                info_text("pero: ","1", "es la que me mata", "dp"),
                                rx.spacer(),
                                info_text("es todo mental","confio", "que el amor de mi vida esta ahi afuera", "la conocere"),
                                rx.spacer(),
                                
                                info_text("diablo","cringe", "pero es asi", "cora"),
                                width="100%"


                ),width="100%"),
                rx.text(""" Mucho yo lo se, que si tu me pruebas te vas a enamoraaaaar ,texto""",
                        color=TextColor.BODY.value),
                spacing=styles.Size.BIG.value,
                align_items="start" 

        )
