import flet as ft

def main(page:ft.Page):
  page.horizontal_alignment = 'center'
  page.vertical_alignment = 'center'
  #page.window_maximized = True
  #page.window_resizable = False

  def logar(e):
    page.remove(Register)
    page.add(Login)
    page.update()

  def cadastrar(e):
    page.remove(Login)
    page.add(Register)
    page.update()

  Login = ft.Column([
    ft.Container(
      width=page.window_width - 10, 
      height=page.window_height - 60,
      bgcolor=ft.colors.GREY_400,
      border_radius=10,

      content=ft.Column([
        ft.Container(
          bgcolor=ft.colors.WHITE,
          width=400,
          height=320,
          border_radius=10,

          content= ft.Column([
            ft.Container(
              padding = ft.padding.only(
                top=10,
                bottom=12
              ),


              content = ft.Column([
                ft.Text(
                  value="Login",
                  weight='bold',
                  size=20,
                  color=ft.colors.BLACK,
                )
              ])
            ),

            ft.Column([
              ft.TextField(

                hint_text='Email',
                width=300,
                height=40,
                border_radius=40,
                prefix_icon=ft.icons.PERSON,
                keyboard_type=ft.KeyboardType.EMAIL,
                color=ft.colors.BLACK,
                text_vertical_align=1,
                hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
              ),

              ft.TextField(
                hint_text='Senha',
                width=300,
                height=40,
                border_radius=40,
                prefix_icon=ft.icons.LOCK,
                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                password=True,
                can_reveal_password=True,
                color=ft.colors.BLACK,
                text_vertical_align=1,
                hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
              ),

              ft.ElevatedButton(
                text='Entrar',
                bgcolor=ft.colors.GREEN_200,
                on_hover=ft.colors.GREEN_100,
                color=ft.colors.BLACK,
                width=300,
                height=40
              ),

              ft.Row([
                ft.TextButton('Recuperar conta'),
                ft.TextButton(
                  text='Cadastre-se',
                  on_click=cadastrar
                )
              ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ], spacing=10),

              ft.Row([
                ft.IconButton(icon=ft.icons.EMAIL),
                ft.IconButton(icon=ft.icons.FACEBOOK),
                ft.IconButton(icon=ft.icons.TELEGRAM)
              ], alignment='center')

          ], horizontal_alignment='center')
        )
      ],horizontal_alignment='center', alignment='center')
    )
  ])

  Register = ft.Column([
      ft.Container(
        width=page.window_width - 10,
        height=page.window.height - 60,
        bgcolor= ft.colors.GREY_400,
        border_radius=10,

        content=ft.Column([
          ft.Container(
            bgcolor=ft.colors.WHITE,
            width=400,
            height=450,
            border_radius=10,

            content=ft.Column([
              ft.Container(
                padding= ft.padding.only(
                  top=10,
                  bottom=12
                ),

                content= ft.Column([
                  ft.Text(
                    value='Cadastre-se',
                    weight='bold',
                    color=ft.colors.BLACK,
                    size=20,
                  )
                ])
              ), 


              ft.Column([
                ft.TextField(
                  hint_text="Primeiro nome",
                  width=300,
                  height=40,
                  border_radius=40,
                  prefix_icon=ft.icons.PERSON,
                  keyboard_type=ft.KeyboardType.NAME,
                  color=ft.colors.BLACK,
                  text_vertical_align=1,
                  hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
                ),  

                ft.TextField(
                  hint_text="Segundo nome",
                  width=300,
                  height=40,
                  border_radius=40,
                  prefix_icon=ft.icons.PERSON,
                  keyboard_type=ft.KeyboardType.NAME,
                  color=ft.colors.BLACK,
                  text_vertical_align=1,
                  hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
                ),

                ft.TextField(
                  hint_text='Email',
                  width=300,
                  height=40,
                  border_radius=40,
                  prefix_icon=ft.icons.EMAIL,
                  keyboard_type=ft.KeyboardType.EMAIL,
                  color=ft.colors.BLACK,
                  text_vertical_align=1,
                  hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
                ),

                ft.TextField(
                  hint_text='Telefone',
                  width=300,
                  height=40,
                  border_radius=40,
                  prefix_icon=ft.icons.PHONE,
                  color=ft.colors.BLACK,
                  keyboard_type=ft.KeyboardType.PHONE,
                  text_vertical_align=1,
                  hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
                ),

                ft.TextField(
                  hint_text='Senha',
                  width=300,
                  height=40,
                  border_radius=40,
                  prefix_icon=ft.icons.LOCK,
                  color=ft.colors.BLACK,
                  keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                  password=True,
                  can_reveal_password=True,
                  hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
                ),

                ft.TextField(
                  hint_text='Confirme sua senha',
                  width=300,
                  height=40,
                  border_radius=40,
                  prefix_icon=ft.icons.LOCK,
                  color=ft.colors.BLACK,
                  keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                  password=True,
                  can_reveal_password=True,
                  hint_style=ft.TextStyle(
                  color=ft.colors.BLACK54,)
                ),

                ft.ElevatedButton(
                  text='Cadastrar',
                  width=300,
                  height=40,
                  bgcolor=ft.colors.GREEN_200,
                  on_hover=ft.colors.GREEN_100,
                  color=ft.colors.BLACK, 
                ),

                ft.Row([
                  ft.TextButton('Recuperar conta'),
                  ft.TextButton(
                    text='Já possuo conta',
                    on_click=logar
                  )
                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

              ], spacing=10)


            ], horizontal_alignment='center')
          ),

        ], horizontal_alignment='center', alignment='center')

      )
  ])


  page.add(Login)
if __name__ == "__main__":
  ft.app(target=main)