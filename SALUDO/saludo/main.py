import flet as ft

def mostrar_nombre(text_field,page):
    nombre=text_field.value
    dialog=ft.AlertDialog(
        title=ft.text("HOLA ÑAÑIELA")
        content=ft.text(f"tu nombre es: {nombre}"+"BIENVENIDA A FLET"),
    action=[
        ft.text_button("Da click para salir"),on_click=lambda e:close_dialog(page))
        ]
    )
    page.dialog=dialog
    page.dialog.open=True
    page.updtae()
    
def close_dialog(page)
    page.dialog.open=False
    page.update()

def main(page: ft.Page):
    page.title="mostrar nombre"
    page.bgcolor=#c661b3
    text_field =ft.textfield(label="ingresa tu nombre")
    button=ft.elevated_button(
        text="di mi nombre",
        on_click=lamdba e:mostrar_nombre(text_fiel,page)
    )
    page.add(
        ft.row(controls=[
            text_field,button
        ]
    )
ft.app(main)
