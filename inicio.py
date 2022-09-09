import flet
from flet import Page, UserControl, Image, Container, Column, TextField, Text, colors
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
        self.portada = Image(src='/sin-imagen.jpg', border_radius=7, fit='contain', width=300)
        self.contenedor_portada = Container(content=self.portada)
        # CONTENEDOR --------------------------------------------------------------------------------
        self.contenedor = Container(
            content=Column(
                controls=[self.titulo_input, self.total_resultados, self.contenedor_portada],
                height=550,
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
                print(self.lista_resultados[0])
                self.total_resultados.value = f'Títulos encontrados: {len(self.lista_resultados)}'
                self.portada.src = f'{url_imagen}{self.lista_resultados[0]["poster_path"]}'
                self.contenedor.update()
            except:
                print('error')


def main(page: Page):
    page.title = 'Películas'
    page.window_width = 400
    page.window_height = 800
    page.window_center()
    page.update()
    page.add(Inicio())



flet.app(target=main, assets_dir='assets')

# TODO añadir botones para avanzar o retorceder en la lista de títulos encontrados
