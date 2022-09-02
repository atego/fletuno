import flet
from flet import Page, UserControl, Container, Column, TextField, Text, colors, icons
import requests

url_1: str = 'https://api.themoviedb.org/3/search/multi?api_key=95416f08d5a3605b98c196f97deb89dc&language=es-ES' \
             '&query= '
url_2: str = '&page=1&include_adult=true'
url_imagen = 'https://image.tmdb.org/t/p/w500'


class Inicio(UserControl):
    def build(self):
        self.lista_resultados: list = []
        # INPUT TITULO -----------------------------------------------------------------------------
        self.titulo_input = TextField(expand=True, border='underline', on_submit=self.buscar_titulo)
        # TEXTO RESULTADOS -------------------------------------------------------------------------
        self.total_resultados = Text(value='', size=16, color=colors.BLUE)
        # IMAGEN DE PORTADA ------------------------------------------------------------------------
        self.portada = Container(
            width=300,
            height=400,
            image_src='',
            image_fit='contain',
            border_radius=7
        )
        # CONTENEDOR --------------------------------------------------------------------------------
        self.contenedor = Container(
            content=Column(
                controls=[self.titulo_input, self.total_resultados, self.portada],
                height=500,
                spacing=10,
                horizontal_alignment='center'
            )
        )
        return self.contenedor

    # METODOS *********************************************************************************************************
    def buscar_titulo(self, e):
        titulo: str = self.titulo_input.value
        if titulo:
            url: str = f'{url_1}{titulo}{url_2}'
            try:
                respuesta = requests.get(url=url).json()
                self.lista_resultados = respuesta['results']
                self.total_resultados.value = f'Títulos encontrados: {len(self.lista_resultados)}'
                self.portada.image_src = f'{url_imagen}{self.lista_resultados[0]["poster_path"]}'
                self.contenedor.update()
            except:
                print('error')


def main(page: Page):
    page.title = 'Películas'
    page.window_center()
    page.update()
    page.add(Inicio())


flet.app(target=main)
