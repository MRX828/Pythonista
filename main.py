from kivymd.app import *
from kivy.lang import *
from kivy.clock import Clock 
from kivy.core.clipboard import*
from kivymd.uix.label import *
from kivy.uix.screenmanager import *
from kivymd.uix.card import *
from kivy.core.window import *
from kivymd.uix.dialog import*
from plyer import*
from kivymd.uix.button import*
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import*
from kivy.core.text import LabelBase
LabelBase.register(name="Roboo",fn_regular="Poppins-SemiBold.ttf")
LabelBase.register(name="Roboto",fn_regular="B.ttf")

Builder.load_file("joke.kv")
class cards(MDCard):
	def __init__(self,y,**kwargs):
		super().__init__(**kwargs)
		self.ids.textos.text=y
class card	(MDCard):
	def __init__(self,y,**kwargs):
		super().__init__(**kwargs)
		self.ids.texto.text=y
	
			
	def dialog(self,*x):
		m=MDDialog(title="Quer Sair",buttons=[MDFlatButton(text="sim"),MDFlatButton(text="Nao")])
		m.open()
			
		
	
class Jokes(Screen):


	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		self.ids.py.clear_widgets()
		memes_mocambique = [
    "Por que a mão do moçambicano está sempre gelada? - Porque ele vive na terra do sorvete.",
    "O que acontece quando um moçambicano encontra uma nota de 1000 meticais? - Ele faz uma festa!",
    "Qual é o esporte favorito dos moçambicanos? - Corrida de chapas!",
    "Por que o moçambicano nunca fica com frio? - Porque ele sabe como se agasalhar bem com capulanas.",
    "O que o moçambicano disse para o sapo? - Sai da estrada, camundongo!",
    "Por que o moçambicano nunca perde a esperança? - Porque sabe que a chuva de abril sempre chega.",
    "Qual é o segredo da boa comida moçambicana? - Um toque de piri-piri!",
    "Por que o moçambicano não gosta de escalada? - Porque ele prefere subir na vida de outra forma.",
    "O que o moçambicano disse para o ovo? - Anda cá que eu já te galo!",
    "Por que o moçambicano nunca está atrasado? - Porque ele segue o horário à moda africana.",
    "Qual é o esporte mais popular em Moçambique? - Futebol, é claro! É só olhar para as ruas durante uma partida importante.",
    "Por que o moçambicano é ótimo em festas? - Porque ele sabe como animar a pista com ritmos tradicionais.",
    "O que o moçambicano disse para a água? - Se juntas já causam, imagina misturadas!",
    
    "Por que o moçambicano é conhecido por sua hospitalidade? - Porque ele tem o coração tão grande quanto o Monte Namuli.",
    "O que o moçambicano disse para a girafa? - Como é lá de cima?",
    
    "Por que o Presidente Nyusi é tão bom em resolver problemas? Porque ele sempre encontra uma saída diplomática, como uma verdadeira figura de Estado!",
    "Qual é o prato favorito do Presidente Nyusi? Frango à Moçambicana, porque ele sabe como liderar com tempero e sabedoria!",
    "O que o Presidente Nyusi disse quando encontrou um buraco na estrada? 'Vamos tapar isso rapidamente e seguir em frente para um Moçambique ainda melhor!'",
    "Qual é a bebida favorita do Presidente Nyusi? Água de coco, porque ele sempre mantém a calma mesmo sob pressão!",
    "Por que o Presidente Nyusi adora histórias? Porque ele sabe que cada narrativa carrega lições valiosas para o futuro de Moçambique!",
    "Por que o Presidente Nyusi não usa óculos? Porque ele já tem uma visão clara para liderar Moçambique!",
    "O que o Presidente Nyusi disse para o mar? 'Deixe as ondas calmas guiarem o nosso país!'",
    "Qual é o animal favorito do Presidente Nyusi? O elefante, porque ele sempre leva a nação nas costas!",
    "Por que o Presidente Nyusi é bom em resolver enigmas? Porque ele sempre encontra a chave para o sucesso de Moçambique!",
    "O que o Presidente Nyusi disse para o sol? 'Brilhe forte, como a esperança que guia nosso povo!'",
    "Qual é o filme favorito do Presidente Nyusi? 'O Rei Leão', porque ele acredita no ciclo da vida e do desenvolvimento!"
]

	
		for x in memes_mocambique :
			self.ids.py.add_widget(card(x))
		memes = [
    "Por que Alberto sempre está sorrindo? Porque ele é a luz do ambiente!",
    "Kelvin é tão frio que até o inverno pede um casaco quando ele chega.",
    "Alberto é tão inteligente que até o Google pede conselhos a ele.",
    "Kelvin é tão tranquilo que até o mar fica calmo na presença dele.",
    "Alberto é tão enérgico que até o Sol pede dicas de como brilhar mais.",
    "Quando Kelvin chega, até as nuvens ficam impressionadas com sua serenidade.",
    "Alberto é tão talentoso que até as estrelas pedem autógrafos a ele.",
    "Kelvin é tão magnético que até os ímãs querem ser amigos dele.",
    "Alberto é tão confiável que até os relógios pedem para ele dar as horas.",
    "Quando Kelvin fala, até o vento para para ouvir suas palavras sábias.",
    "O que uma laranja disse para a outra? - Você é tão espremida!",
    "Por que o tomate virou super-herói? - Porque ele era ketchup-tão!",
    "Qual é o café que todo mundo tem medo? - O ex-presso.",
    "Por que a galinha foi para o espaço? - Para visitar o planeta Martérnico.",
    "Por que o cachorro entrou na igreja? - Para seguir o caminho dos cãodidatos.",
    "O que o livro de matemática disse para o livro de história? - Você me conta uma história que eu te resolvo um problema."
]


		for x in memes:
			self.ids.pys.add_widget(cards(x))

	def menu(self):
		menu_item=[{"viewclass":"OneLineListItem","text":"sair","divider_color":[1,1,1,1],"on_release":lambda x="m":MDApp.get_running_app().stop()},{"viewclass":"OneLineListItem","text":"Sobre","on_release":lambda x="m":self.sobre()}]
		self.MEnu=MDDropdownMenu (items=menu_item,caller=self.ids.navi, width_mult=2,pos_hint={"x":.4,"y":.84})
		self.MEnu.open()
	def sobre(self):
		self.MEnu.dismiss()
		M=MDDialog(title="MEMES MOZ",text=" MEMES MOZ É UM APP QUE VEIO PARA MELHOR A SUA VIDA COMO MEMEIRO")
		M.open()
	def falar(self):
		tts.speak("SEJA FELIZ COM MEMES MOZ")

class Demo(MDApp):
	def build(self):
		#self.theme_cls.theme_style="Dark"
		
		return Jokes()
	def copiar(self,x):
		Clipboard.copy(x)
		toast ("MEME COPIADO COM SUCESSO ")
	
Demo().run()