import tkinter as tk
from tkinter import PhotoImage, Entry, Label
from subprocess import call
import os
from PIL import Image, ImageTk
import time


def execute_cc_file_1():
    # Obter valores dos campos de entrada
    x = entry_x.get()
    y = entry_y.get()
    z = entry_z.get()
    radius = entry_radius.get()

    # Passando os valores para main.cc como argumentos de linha de comando
    compile_command = "g++ main.cc -o main.exe"
    run_command = f"main.exe {x} {y} {z} {radius}"

    # Compilar main.cc
    compile_result = call(compile_command, shell=True)
    if compile_result == 0:
        # Se a compilação for bem-sucedida, executa o programa com os valores fornecidos
        call(run_command, shell=True)
    else:
        print("Erreur lors de la compilation du fichier.")

    
    




def execute_cc_file_2():
    # Obter valores dos campos de entrada
    x = entry_x.get()
    y = entry_y.get()
    z = entry_z.get()
    side = entry_side.get()

    # Passando os valores para main.cc como argumentos de linha de comando
    compile_command = "g++ main.cc -o main.exe"
    run_command = f"main.exe {x} {y} {z} {side}"

    # Compilar main.cc
    compile_result = call(compile_command, shell=True)
    if compile_result == 0:
        # Se a compilação for bem-sucedida, executa o programa com os valores fornecidos
        call(run_command, shell=True)
        
    else:
        print("Erreur lors de la compilation du fichier.")

def get_save_values_1():
    x = entry_x.get()
    y = entry_y.get()
    z = entry_z.get()
    radius = entry_radius.get() 

    try:
        # Tente de sauvegarder les valeurs dans le fichier infos_circle.txt
        with open("infos_circle.txt", "w") as fichier:
            fichier.write(f"x: {x}\ny: {y}\nz: {z}\nradius: {radius}")
        print("Valeurs enregistrees dans infos_circle.txt")
    except Exception as e:
        # Imprime toute erreur qui se produit
        print(f"Erreur lors de l'enregistrement du fichier : {e}")

    # Imprime le répertoire courant pour aider à identifier où le fichier devrait être
    print(f"Repertoire actuel : {os.getcwd()}")

    
def get_save_values_2():
    x = entry_x.get()
    y = entry_y.get()
    z = entry_z.get()
    side = entry_side.get() 

    try:
        # Tente de sauvegarder les valeurs dans le fichier infos_circle.txt
        with open("infos_circle.txt", "w") as fichier:
            fichier.write(f"x: {x}\ny: {y}\nz: {z}\nradius: {side}")
        print("Valeurs enregistrées dans infos_circle.txt")
    except Exception as e:
        # Imprime toute erreur qui se produit
        print(f"Erreur lors de l'enregistrement du fichier : {e}")

    # Imprime le répertoire courant pour aider à identifier où le fichier devrait être
    print(f"Répertoire actuel : {os.getcwd()}")


def show_screen_1():
    global entry_x, entry_y, entry_z, entry_radius

    # Limpa a janela principal
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")  # Redefine o tamanho da janela para a tela secundária

    # Carrega o plano de fundo
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Configura os campos de entrada e o botão
    label_x = Label(root, text="X:")
    label_x.place(relx=0.43, rely=0.4, anchor=tk.E)
    entry_x = Entry(root)
    entry_x.place(relx=0.43, rely=0.4, anchor=tk.W)

    label_y = Label(root, text="Y:")
    label_y.place(relx=0.43, rely=0.45, anchor=tk.E)
    entry_y = Entry(root)
    entry_y.place(relx=0.43, rely=0.45, anchor=tk.W)

    label_z = Label(root, text="Z:")
    label_z.place(relx=0.43, rely=0.5, anchor=tk.E)
    entry_z = Entry(root)
    entry_z.place(relx=0.43, rely=0.5, anchor=tk.W)

    label_radius = Label(root, text="R:")
    label_radius.place(relx=0.43, rely=0.55, anchor=tk.E)
    entry_radius = Entry(root)
    entry_radius.place(relx=0.43, rely=0.55, anchor=tk.W)


    button_save = tk.Button(root, text="Save Values", command=get_save_values_1)
    button_save.place(relx=0.43, rely=0.62, anchor=tk.CENTER)  # Ajuste para posicionar à esquerda

    
    button_plot = tk.Button(root, text="Plot View", command=execute_cc_file_1)
    button_plot.place(relx=0.57, rely=0.62, anchor=tk.CENTER)  # Ajuste para posicionar à direita

    button_return = tk.Button(root, text="Menu", command=show_main_menu)
    button_return.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def show_screen_2():
    global entry_x, entry_y, entry_z, entry_side

    # Limpa a janela principal
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")  # Redefine o tamanho da janela para a tela secundária

    # Carrega o plano de fundo
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Configura os campos de entrada e o botão
    label_x = Label(root, text="X:")
    label_x.place(relx=0.43, rely=0.4, anchor=tk.E)
    entry_x = Entry(root)
    entry_x.place(relx=0.43, rely=0.4, anchor=tk.W)

    label_y = Label(root, text="Y:")
    label_y.place(relx=0.43, rely=0.45, anchor=tk.E)
    entry_y = Entry(root)
    entry_y.place(relx=0.43, rely=0.45, anchor=tk.W)

    label_z = Label(root, text="Z:")
    label_z.place(relx=0.43, rely=0.5, anchor=tk.E)
    entry_z = Entry(root)
    entry_z.place(relx=0.43, rely=0.5, anchor=tk.W)

    label_side = Label(root, text="L:")
    label_side.place(relx=0.43, rely=0.55, anchor=tk.E)
    entry_side = Entry(root)
    entry_side.place(relx=0.43, rely=0.55, anchor=tk.W)


    button_save = tk.Button(root, text="Save Values", command=get_save_values_2)
    button_save.place(relx=0.43, rely=0.62, anchor=tk.CENTER)  # Ajuste para posicionar à esquerda

    
    button_plot = tk.Button(root, text="Plot View", command=execute_cc_file_2)
    button_plot.place(relx=0.57, rely=0.62, anchor=tk.CENTER)  # Ajuste para posicionar à direita

    button_return = tk.Button(root, text="Menu", command=show_main_menu)
    button_return.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    
    

# Função para exibir uma tela secundária
def show_screen(screen_number):
    # Limpa a janela principal
    for widget in root.winfo_children():
        widget.destroy()
    
    # Carrega o plano de fundo
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    if(screen_number==1):
        show_screen_1()

    if(screen_number==2):
        show_screen_2()

# Função para exibir o menu principal
def show_main_menu():
    # Limpa a janela principal
    for widget in root.winfo_children():
        widget.destroy()

    # Carrega o plano de fundo
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Cria os botões do menu

    button = tk.Button(root, text=str("Plot"), command=lambda : show_screen(1), font=('Verdana', 12, 'bold'), fg='black', bg='#F5F5DC', relief="groove", highlightbackground='#E3E3E3',  highlightthickness=2, highlightcolor='#B0B0B0')
    button.place(relx=0.5, rely=0.5 , anchor=tk.CENTER)

    button = tk.Button(root, text=str("Quit"), command=lambda : root.destroy(), font=('Verdana', 12, 'bold'), fg='black', bg='#F5F5DC', relief="groove", highlightbackground='#E3E3E3',  highlightthickness=2, highlightcolor='#B0B0B0')
    button.place(relx=0.5, rely=0.65 , anchor=tk.CENTER)

    #button = tk.Button(root, text=str("Plot Sphere et Square"), command=lambda : show_screen(3), font=('Verdana', 12, 'bold'), fg='black', bg='#F5F5DC', relief="groove", highlightbackground='#E3E3E3',  highlightthickness=2, highlightcolor='#B0B0B0')
    #button.place(relx=0.27, rely=0.8, anchor=tk.CENTER)

    #button = tk.Button(root, text=str("Plot N-Sphere"), command=lambda : show_screen(4), font=('Verdana', 12, 'bold'), fg='black', bg='#F5F5DC', relief="groove", highlightbackground='#E3E3E3',  highlightthickness=2, highlightcolor='#B0B0B0')
    #button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Configuração inicial da janela principal
root = tk.Tk()
root.title("Projet Ray Tracing")
root.geometry("800x600")

# Carrega a imagem de fundo
background_image = PhotoImage(file="background.png")

show_main_menu()

root.mainloop()
