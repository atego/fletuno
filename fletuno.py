import flet
from flet import IconButton, Page, Row, TextField, icons


def main(page: Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_width = 400
    page.window_height = 200
    page.window_center()

    def avisar(e):
        print(f'cambio!! en {e.control.data}\n{e.control.value}')

    mensage = TextField(
        value='Hola señor!!',
        width=200,
        text_align='center',
        height=26,
        content_padding=1,
        on_submit=avisar,
        data='entrada_texto'
    )

    page.add(mensage)


flet.app(target=main, port=3000, view=flet.WEB_BROWSER)
