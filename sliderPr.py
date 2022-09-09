import flet
from flet import (Page, TextField, Tabs, Tab, Container, Image, CircleAvatar,
                  Column, icons, colors, Text, FloatingActionButton)
import requests
from dataclasses import dataclass


@dataclass
class MediaInfo:
    titulo: str
    caratula: str
    dorso: str
    # actores: list[int]
    resumen: str


respuesta: list[dict]


def main(page: Page):
    page.title = ''
    page.window_width = 450
    page.window_height = 600
    page.window_center()

    url_buscar_1: str = 'https://api.themoviedb.org/3/search/multi?api_key=95416f08d5a3605b98c196f97deb89dc&language=es-ES&query='
    url_buscar_2: str = '&page=1&include_adult=false&region=es-ES'

    def mostrar_buscar(e):
        titulo_in.visible = True if not titulo_in.visible else False
        titulo_in.focus()
        page.update()

    def buscar_titulo(e):
        global respuesta
        if titulo_in.value:
            url: str = f'{url_buscar_1}{titulo_in.value}{url_buscar_2}'
            try:
                respuesta = requests.get(url=url).json()['results']
                titulo_in.visible = False
                pestanas.selected_index = 2
                page.update()
                mostrar_titulo(indice=0)
            except:
                print('error')

    def mostrar_titulo(indice: int):
        info: MediaInfo = MediaInfo(
            titulo=respuesta[indice]['title'] if respuesta[indice]['media_type'] == 'movie' else respuesta[indice][
                'name'],
            caratula=f'https://image.tmdb.org/t/p/w500{respuesta[indice]["poster_path"]}',
            dorso=f'https://image.tmdb.org/t/p/w500{respuesta[indice]["backdrop_path"]}',
            resumen=respuesta[indice]['overview']
        )
        titulo_portada.value = info.titulo
        imagen_portada.src = info.caratula
        avatar_dorso.foreground_image_url = info.dorso
        sinopsis_texto.value = info.resumen
        pestanas.update()

    boton_buscar = FloatingActionButton(
        icon=icons.SEARCH,
        bgcolor=colors.ORANGE,
        on_click=mostrar_buscar
    )

    titulo_in = TextField(
        border='underline', visible=False, hint_text='título',
        on_submit=buscar_titulo, color=colors.BLUE_600
    )

    titulo_portada: Text = Text(value='', size=18, color=colors.PURPLE)
    imagen_portada: Image = Image(src='/sin-imagen.jpg', width=200, border_radius=7)
    avatar_dorso: CircleAvatar = CircleAvatar(
        bgcolor=colors.BLUE_GREY_100,
        radius=100
    )
    sinopsis_texto = Text(value='', size=12, color=colors.BLUE_GREY_600)

    # PESTAÑA PORTADA (título e imagen de la portada) ******************************************************************
    pestana_titulo: Tab = Tab(
        text='Portada',
        content=Container(
            margin=30,
            content=Column(
                controls=[
                    imagen_portada,
                    titulo_portada
                ],
                horizontal_alignment='center',
                spacing=20,
                alignment='start',
            )
        )
    )

    pestana_resumen: Tab = Tab(
        text='Sinopsis',
        content=Container(
            margin=30,
            content=Column(
                controls=[avatar_dorso, sinopsis_texto],
                horizontal_alignment='center',
                spacing=20,
                alignment='start'
            )
        )
    )

    pestanas = Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[
            pestana_titulo, pestana_resumen],
    )

    page.add(titulo_in, pestanas, boton_buscar)


flet.app(target=main, assets_dir='assets')
