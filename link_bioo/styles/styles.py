import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .font import Font as Font
from .font import FontWeight as FontWeight
# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL="0.5em"
    MEDIUM = "0.75em"
    DEFAULT="1em"
    LARGE = "1.5em"
    BIG="2em"

STYLESHEETS =[

    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@500&display=swap"
]         

# Styles

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weigth": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value, 
    rx.heading:{
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weigth": FontWeight.MEDIUM.value,

    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
                "background_color": Color.SECONDARY.value,

        }
    },
    rx.link : {
        "text_decoration": "none",
        "_hover": {}
        }
    }


narvar_title_style=dict(
    font_family=Font.LOGO.value,
    font_weigth= FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value

)

title_style=dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_tittle_style = dict(
    font_family=Font.TITLE.value,
    font_weigth= FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_wight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)
