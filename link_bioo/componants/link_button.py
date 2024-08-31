import reflex as rx
import link_bioo.styles.styles as styles

def link_button(title: str, body:str, url: str) -> rx.Component:

    return rx.link(
        
        rx.button(
            rx.hstack(
                rx.flex(
                    rx.icon("moon", stroke_width=1.5),
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value
    

                ),
                rx.vstack(
                    rx.text(title, style= styles.button_tittle_style),
                    rx.text(body, style= styles.button_body_style),
                    align_items="start"
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%",
        text_decoration="none"
    
    )
