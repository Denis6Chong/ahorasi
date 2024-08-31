import reflex as rx

#Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://moure.dev/preview.jpg"



_meta=[
                {"name": "og:type", "content": "website"},
                {"name": "og:image", "content": preview},
                {"name": "twitter:card", "content": "summary_large_image"},
                {"name": "twitter:site", "content": "@mouredev"},

            ]

# Index

index_title = "Chong"
index_description = "hola, soy el tanque del cerro"


index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]

index_meta.extend(_meta)
#Cursos

courses_title = "API REFLEX | Gratis"
courses_description = "listado de cursos"

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description}
]