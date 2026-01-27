"""Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

from pygame import mixer, event

mixer.init()
mixer.music.load("ex021.mp3")
mixer.music.play()
input('Pressione ENTER para sair')
