import webbrowser
from kivymd.uix.boxlayout import MDBoxLayout
from pythonosc import udp_client
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty





class main(MDApp):
    jogadora = ObjectProperty()
    jogadorb = ObjectProperty()
    campo = ObjectProperty()
    campo_ip = ObjectProperty()
    IPE = ObjectProperty()
    campo_porta = ObjectProperty()
    val = ObjectProperty()
    valp = ObjectProperty()
    ipx = None
    infox = None



    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        

    def login(self):
        print(self.root.ids.jogadora.text, self.root.ids.jogadorb.text)
        udp_client.SimpleUDPClient(self.val, self.valp).send_message(self.val, f'/name1 {self.root.ids.jogadora.text}')
        udp_client.SimpleUDPClient(self.val, self.valp).send_message(self.val, f'/name2 {self.root.ids.jogadorb.text}')
        self.root.ids.campo.text = f'{self.root.ids.jogadora.text}  VS  {self.root.ids.jogadorb.text}'
        self.root.ids.jogadora.text = ''
        self.root.ids.jogadorb.text = ''

    def iniciar(self):
        udp_client.SimpleUDPClient(self.val, self.valp).send_message(self.val, '/status 1')
        print('começou')

    def resetar(self):
        udp_client.SimpleUDPClient(self.val, self.valp).send_message(self.val, '/status 0')
        print('resetou')
        self.root.ids.campo.text = ' '

    def info(self):
        if not self.infox:
            self.infox = MDDialog(
                title="Desenvolvido por Pozzi",
                text="Para o projeto labJanssen da Noisetupi",
                buttons=[
                    MDRaisedButton(
                        text='Pozzi', on_release=self.pozzi, elevation=15
                    ),
                    MDRaisedButton(
                        text='Noisetupi', on_release=self.palm, elevation=15
                    ),
                    MDRaisedButton(
                        text='Fechar', on_release=self.fechar_info, elevation=15
                    ),
                ]
            )
        self.infox.open()

    def fechar_info(self, obj):
        self.infox.dismiss()

    def palm(self, obf):
        webbrowser.open("https://noisetupi.com.br/")

    def pozzi(self, obj):
        webbrowser.open("https://github.com/zittox")

    def ip_setup(self):
        content_cls = ip_dialog()
        if not self.ipx:
            self.ipx = MDDialog(
                title="Digite o IP com pontos",
                type="custom",
                content_cls=content_cls,
                buttons=[
                    MDFlatButton(
                        text='Enviar',
                        on_release=lambda x:self.fechar_ipx(x, content_cls),
                    ),
                ]
            )
        self.ipx.open()

    def fechar_ipx(self, instance_btn, content_cls):
        texto = content_cls.ids.campo_ip
        texport = content_cls.ids.campo_porta
        valp = texport._get_text()
        val = texto._get_text()
        print(val, valp)
        self.valp = int(valp)
        self.val = val
        self.root.ids.IPE.title = f'{val}:{valp}'
        self.root.ids.campo_id.text = ''
        self.root.ids.campo_porta.text = ''
        self.ipx.dismiss()


    def build(self):
        self.title = 'labJanssen - Input app'
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('loggin.kv')


class LoginApp(MDScreen):
    pass


class ip_dialog(MDBoxLayout):
    pass


if __name__ == "__main__":
    main().run()

