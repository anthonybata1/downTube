from ctypes import windll
from pytube import YouTube
import moviepy.editor as mp
from re import search
import os
#coding: utf-8

#definindo nome de titulo
windll.kernel32.SetConsoleTitleW("downTube v0.0.1  ~Anthony")

escolha = True

while escolha:
    #pedido do while
    os.system("cls || clear")
    print("\nO que deseja fazer?\n")
    print("1- Baixar um video.\n")
    print("2- Baixar um audio.\n")
    print("3- Sair do Programa:\n")
    escolha = input("Qual sua opção? ")

    if escolha == "1":
        link = input("\nDigite a URL a ser baixada:\n")
        path = input("\nDigite o local para o Download (ex: 'C:/download'):\n ")
        yt = YouTube(link)

        #detalhando video
        print("\nTítulo: ", yt.title)

        #confirmação de download
        confirm = input("\nÉ este é a URL certa?(s/n) ")
        if confirm == "s":
            ys = yt.streams.get_highest_resolution()
        
        print("Baixando, aguarde...")
        ys.download(path)
        print("\nDownload Completo!!\n\n")
        input("Aperte qualquer tecla para continuar...")

    if escolha == "2":
        link = input("\nDigite a URL a ser baixada:\n")
        path = input("\nDigite o local para o Download (ex: 'C:/download'):\n ")
        yt = YouTube(link)

        #detalhando video
        print("\nTítulo: ", yt.title)

        #confirmação de download
        confirm = input("\nÉ este é a URL certa?(s/n) ")   
        if confirm == "s":
            print("Baixando, aguarde...")
            ys = yt.streams.filter(only_audio=True).first().download(path)
        print("\nDownload Completo!!\n\n")
        
        print('Convertendo arquivo...')
        for file in os.listdir(path):
            if search('mp4',file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        
        print("\nSucesso!\n\n")
        input("Aperte qualquer tecla para continuar...")

    if escolha == "3":
        break

else:
    print("Erro!!")
    input("Aperte qualquer tecla para continuar...")
