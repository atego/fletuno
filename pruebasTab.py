import flet
from flet import Container, Icon, Page, Tab, Tabs, Text, Image, ElevatedButton, Column,alignment, icons, colors


def main(page: Page):
    mensaje = Text(size=24, color=colors.PURPLE)
    imagen = Image(src='/sin-imagen.jpg', width=200)
    mensaje2 = Text(size=24, color=colors.RED_800)

    t = Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            Tab(
                text="Tab 1",
                content=Container(
                    content=Text("This is Tab 1"),
                    alignment=alignment.center,
                ),
            ),
            Tab(
                tab_content=Icon(icons.SEARCH),
                content=mensaje2
            ),
            Tab(
                text="Tab 3",
                icon=icons.SETTINGS,
                content=Container(
                    content=Column(
                        controls=[mensaje, imagen],
                        spacing=20,
                        horizontal_alignment='center'
                    )
                )
            ),
        ],
        expand=1,
    )

    def cambiar_texto(e):
        mensaje.value = 'Vaya mierda!!'
        mensaje2.value = 'Pues parece que funciona...'
        imagen.src = '/audacity.png'
        page.update()

    boton = ElevatedButton(text='cambiar texto', on_click=cambiar_texto)

    page.add(t, boton)


flet.app(target=main, assets_dir='assets')
