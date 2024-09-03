import reflex as rx
import link_bioo.styles.styles as styles
from link_bioo.pages.index import index 
from link_bioo.pages.courses import courses
from link_bioo.api.api import hello




            
        
    



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    #head_components=[
    #   rx.script(src="https://www.googletagmanager.com/gtag/js?id=")
    #]

)

app.api.add_api_route("/hello", hello)

