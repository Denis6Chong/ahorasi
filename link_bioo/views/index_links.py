import reflex as rx
from link_bioo.componants.link_button import link_button
from link_bioo.componants.title import title
from link_bioo.routes import Route

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitter", 
            " este es mi twitter", 
            "https://x.com/@denischong2"
        ),
        link_button("You Tube", "{mi canal para aprender reflex}","https://youtube.com/@mouredev" ),
        link_button("Instagram", "[mi perdida de tiempo]", "https://instagram.com/@jd_chong"),
        link_button("Facebook", "revolico","https://facebook.com/@jorgedenischongperez" ),
        link_button("Cursos", "beibi tu eres mia mia",Route.COURSES.value),
        width="100%"
    )