import reflex as rx
import link_bioo.utils as utils
from link_bioo.componants.navbar import navbar
from link_bioo.views.header.header import header
from link_bioo.views.index_links import links
from link_bioo.componants.footer import footer
import link_bioo.styles.styles as styles
from link_bioo.routes import Route

@rx.page(
        route=Route.COURSES.value,
        title=utils.courses_title,
        description=utils.courses_description,
        image=utils.preview,
        meta=utils.courses_meta
)
def courses() -> rx.Component:
    
    return rx.box(
        utils.lang(),
        navbar(),
            rx.center(
                rx.vstack( 
                    header(),
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=styles.Size.BIG.value,
                    padding=styles.Size.BIG.value
                )
            ),
            footer()
    )


