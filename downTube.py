from ctypes import windll
from time import sleep
from pytube import YouTube
import moviepy.editor as mp
from re import search
import os
#coding: utf-8

#definindo nome de titulo
windll.kernel32.SetConsoleTitleW("downTube v0.0.2  ~Anthony")

escolha = True

#pastas de download na raiz do app
video_path = './downloads'
mp3_path1 = './downloads/mp3'


#programa
while escolha:

    #pedido do while
    os.system("cls || clear")
    print("\nO que deseja fazer?\n")
    print("1- Baixar um video.\n")
    print("2- Baixar um audio.\n")
    print("3- Sair do Programa:\n")
    escolha = input("Qual sua opção? ")

    if escolha == "1":
        link = input("\n\nDigite a URL a ser baixada:\n")
        yt = YouTube(link)

        #detalhando video
        print("\nTítulo: ", yt.title)

        #confirmação de download
        confirm = input("\nÉ este é a URL certa?(s/n) ")
        if confirm == "s":
            ys = yt.streams.get_highest_resolution()

            print("Baixando, aguarde...")
            ys.download(video_path)
            print("\nDownload Completo!!\n\n")
            input("Aperte qualquer tecla para continuar...")

        else:
            print("\n\nTente Novamente")
            input("Aperte qualquer tecla para continuar...")

    if escolha == "2":
        link = input("\nDigite a URL a ser baixada:\n")
        yt = YouTube(link)

        #detalhando video
        print("\nTítulo: ", yt.title)

        #confirmação de download
        confirm = input("\nÉ este é a URL certa?(s/n) ")   
        if confirm == "s":
            print("Baixando, aguarde...")
            ys = yt.streams.filter(only_audio=True).first().download(mp3_path1)
            print("\nDownload Completo!!\n\n")

            print('Convertendo arquivo...')
            for file in os.listdir(mp3_path1):
                if search('mp4',file):
                    mp4_path = os.path.join(mp3_path1, file)
                    mp3_path = os.path.join(mp3_path1, os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)

            print("\nSucesso!\n\n")
            input("Aperte qualquer tecla para continuar...")

        else:
            print("\n\nTente Novamente")
            input("Aperte qualquer tecla para continuar...")

    if escolha == "3":
        print("\n\nSaindo do Programa...")
        sleep(2.5)
        break
