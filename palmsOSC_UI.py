# https://stackoverflow.com/questions/24259692/kivy-and-osc-on-android
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from pythonosc import osc_message_builder
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
import time
import argparse
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty





class main(MDApp):
    jogadora = ObjectProperty()
    jogadorb = ObjectProperty()
    campo = ObjectProperty()
    campo_ip = ObjectProperty()
    IPE = ObjectProperty()
    ipx = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def login(self):
        print(self.root.ids.jogadora.text, self.root.ids.jogadorb.text)
        client.send_message(ip, self.root.ids.jogadora.text)
        client.send_message(ip, self.root.ids.jogadorb.text)
        self.root.ids.campo.text = f'{self.root.ids.jogadora.text}  VS  {self.root.ids.jogadorb.text}'
        self.root.ids.jogadora.text = ''
        self.root.ids.jogadorb.text = ''

    def iniciar(self):
        client.send_message(ip, 1)
        print('começou')

    def resetar(self):
        client.send_message(ip, 0)
        print('resetou')
        self.root.ids.campo.text = ' '

    def enviar_ip(self):
        client.send_message(ip, self.root.ids.campo_ip.text)
        self.root.ids.campo_ip.text = self.root.ids.IPE.text


    def ip_setup(self):
        if not self.ipx:
            self.ipx = MDDialog(
                title="Digite o IP com pontos",
                type="custom",
                content_cls=ip_dialog(),
                buttons=[
                    MDFlatButton(
                        text='Enviar',
                        on_release=self.fechar_ipx,
                    ),
                ]
            )
        self.ipx.open()

    def fechar_ipx(self, obj):
        self.enviar_ip()
        self.ipx.dismiss()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        return Builder.load_file('loggin.kv')


class LoginApp(MDScreen):
    pass

class ip_dialog(MDBoxLayout):
    pass


if __name__ == "__main__":
    ip = '127.0.0.1'
    sendport = 5000
    inport = 5006

    # sending message to server
    client = udp_client.SimpleUDPClient(ip, sendport)

    # catches osc messages
    disp = dispatcher.Dispatcher()
    # dispatcher.map("/status", status)

    # receiving message from server
    server = osc_server.ThreadingOSCUDPServer((ip, inport), disp)
    print("Serving on {}".format(server.server_address))
    main().run()
    server.serve_forever()
