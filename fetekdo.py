
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: Ejhb, Bobba Ash, Dysdylan, Ludo-R
"""
import random
import pandas
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import shutil
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Silent-night.wav")   
pygame.mixer.music.play() 

new_list = []

# Fonction de reset de la var new_list en liste vide
def resetList():
    global new_list
    new_list = []
    
# Fonction pour selectionner le fichier souhaité a passer en liste 
def addList():
    global new_list
    file_convert = filedialog.askopenfilename()
    # convert fichiers csv ou xlsx
    if file_convert.endswith('.csv') or file_convert.endswith('.xlsx'):
        df = pandas.read_csv(file_convert)
        list_csv = df.values.tolist()
        for i in list_csv:
            new_list = new_list+i
    # convert fichiers txt
    if file_convert.endswith('.txt'):
        df = pandas.read_csv(file_convert, sep="\n", header=None)
        list_csv = df.values.tolist()
        for i in list_csv:
            new_list = new_list+i

    return new_list

# Fonction principale, lecture de fichier et affichage rand de la liste contenue
def fetekdo():
    global new_list
    list_clean = new_list
    # Mélange de la liste pour un affichage rand
    random.shuffle(list_clean)
    # Affichage de la liste
    for i in list_clean:
        i = str(i)
        duo_sort.insert(END, i + ' donne à :')
    # Affichage du dernier de la liste à recevoir (premier à donner)
    duo_sort.insert(END, list_clean[0] + ', fin de la liste !')

# Fonction qui passe du menu principal au menu d'exe de la func principale
def funFetekdo():
    choiceMenu3.pack_forget()
    choiceMenu3.pack(side = RIGHT, ipadx = 20, padx = 20, ipady = 25, pady = 15)
    buttonBack.pack(side = LEFT, ipadx = 20, padx = 20, ipady = 25, pady = 15)
    nextDuo.pack(side = TOP, ipadx = 60, padx = 10, ipady = 60, pady = 20)
    choiceMenu1.pack_forget()
    choiceMenu2.pack_forget()
    choiceDelete.pack_forget()
    duo_sort.pack(side = BOTTOM)

# Bouton de retour, on désaffiche les boutons et la liste et réaffiche ceux du menu
def backMenu():
    choiceMenu1.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
    choiceMenu2.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
    choiceDelete.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
    choiceMenu3.pack_forget()
    choiceMenu3.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 15)
    nextDuo.pack_forget()
    duo_sort.delete(0, END)
    duo_sort.pack_forget()
    buttonBack.pack_forget()

# Déclaration de la fenêtre principale et design de celle ci + scrollbar
mainWindow = Tk()
img = ImageTk.PhotoImage(master = mainWindow, file="kdo.gif")
panel = Label(mainWindow, image = img)
panel.pack(side = "left", fill = "both", expand = "yes")
scrollbar = Scrollbar(mainWindow)
scrollbar.pack(side = RIGHT, fill = Y)

# Déclaration de la listbox mais unpack (cf: def funFetekdo():)
duo_sort = Listbox(mainWindow, font=('calibri', 13, 'bold'), bd=0, yscrollcommand = scrollbar.set, height = 30, width = 80)

# Déclaration bouton de retour
buttonBack = Button(mainWindow, text= "Retour", font=('calibri', 13, 'bold', 'underline'), bg='#07d800', fg='black', bd=8, command = backMenu)

# Déclaration bouton pour afficher le shuffle liste
nextDuo = Button(mainWindow, text = "Afficher la liste aléatoire", font=('calibri', 13, 'bold', 'underline'), bg='#661aff', fg='black', bd=8, command = fetekdo)

# Nom de la fenêtre / Appli
mainWindow.title('FETEKDO')

# Déclaration et affichage des boutons du 'menu principal'
choiceMenu1 = Button(mainWindow, text = "FETEKDO", bg='#ffcc00', font=('calibri', 13, 'bold', 'underline'), fg='black', bd=8, command = funFetekdo)
choiceMenu1.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
choiceMenu2 = Button(mainWindow, text = "Ajouter une liste", bg='#10d10b', font=('calibri', 12, 'bold'), fg='black', bd=8, command = addList)
choiceMenu2.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
choiceDelete = Button(mainWindow, text = "Réinitialiser les listes ?", bg='#ea8f04', font=('calibri', 12, 'bold'), fg='black', bd=8, command = resetList)
choiceDelete.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
choiceMenu3 = Button(mainWindow, text = "Quitter", bg='#d10b10', font=('calibri', 11, 'bold', 'underline'), fg='black', bd=8, command = mainWindow.destroy)
choiceMenu3.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 15)

mainWindow.mainloop()