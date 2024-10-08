import reflex as rx
import link_bioo.utils as utils
from link_bioo.componants.navbar import navbar
from link_bioo.views.header.header import header
from link_bioo.views.index_links import links
from link_bioo.componants.footer import footer
import link_bioo.styles.styles as styles
from link_bioo.api.api import hello


class IndexState(rx.State):
    
    @rx.var
    def say_hello(self):
        return hello()


@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta
)
def index() -> rx.Component:
    
    return rx.box(
        utils.lang(),
        navbar(),
            rx.center(
                rx.vstack(
                    rx.text(IndexState.say_hello),
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




