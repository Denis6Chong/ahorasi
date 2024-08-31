import reflex as rx
from link_bioo.styles.colors import Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon =  rx.image(src="/youtube-logo-svgrepo-com.svg")
    href =  "youtube.com"
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}


float_button = FloatButton.create


