#-*-coding;utf-8:-*-
#Desenvolvido por João Pedro
import math
import time
import os
import sys
while True:
	try:
		print("Instalando dependências")
		from tqdm import tqdm
		import easygui
		from mutagen.mp3 import MP3
		from pygame import mixer 
		print("\033[92mConcluído\033[m")
		break
	except ModuleNotFoundError:
		os.system("pip install easygui")
		os.system("pip install mutagen")
		os.system("pip install tqdm")
		os.system("pip install pygame")
while True:
	msg = "Menu de escolhas"
	titulo = "Reprodutor python"
	escolhas = ["Reprodutor de músicas","Desinstalar dependências","Sair"]
	escolha = easygui.choicebox(msg, titulo, escolhas)
	if "Desinstalar dependências" in escolha:
		os.system("pip uninstall easygui")
		os.system("pip uninstall mutagen")
		os.system("pip uninstall tqdm")
		os.system("pip uninstall pygame")
		print("Desinstalado com sucesso")
		break
		sys.exit()
	elif "Sair" in escolha:
		break
		sys.exit()
	else:
		while True:
			try:
				musicPath = easygui.fileopenbox()
				audio = MP3(str(musicPath))
				break
			except:
				print("O arquivo selecionado não é de formato mp3.")
		size = math.trunc((audio.info.length))
		pbar = tqdm(total=size)
		mixer.init()
		mixer.music.load(str(musicPath))
		mixer.music.play()
		os.system("cls")
		print("Reprodução bem sucedida! Curta o som.")
		print("-"*36, "\n"*2)
		for i in range(size):
			pbar.update(1)
			time.sleep(1)
		pbar.close()