from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import subprocess
import os

window = Tk()
window.title("CodeQuest")
window.geometry("1102x618")
window.configure(bg="#162334")
window.minsize(1102, 618)
window.maxsize(1102, 618)

bg_photo = ImageTk.PhotoImage(file="images/settingsbg.png")

window.bg_label = Label(window, image=bg_photo)
window.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
logo = ImageTk.PhotoImage(file="images/logo.png")

window.iconphoto(False, logo)

def show_audio_settings():
    clear_settings_frame()

    audio_label = Label(settings_frame, text="Audio Settings", font=("Arial", 18, "bold"), bg="#2F4D62", fg="#00E69A")
    audio_label.pack(padx=100, pady=50)

    overall_volume_label = Label(settings_frame, text="Overall Volume", font=("Arial", 18, "bold"), bg="#2F4D62", fg="white")
    overall_volume_label.pack(padx=100, pady=30)

def show_language_settings():
    clear_settings_frame()

    language_label = Label(settings_frame, text="Language Settings", font=("Arial", 18, "bold"), bg="#2F4D62", fg="#00E69A")
    language_label.pack(padx=100, pady=50)

    tagalog_disabled_var = BooleanVar()
    tagalog_label_checkbutton = Checkbutton(settings_frame, text="English", font=("Arial", 18, "bold"), bg="#2F4D62", fg="white", variable=tagalog_disabled_var)
    tagalog_label_checkbutton.pack(padx=100, pady=30)

def show_info_settings():
    clear_settings_frame()

    info_label = Label(settings_frame, text="Info Settings", font=("Arial", 18, "bold"), bg="#2F4D62", fg="#00E69A")
    info_label.pack(padx=100, pady=50)

    infobg_label = Label(settings_frame, text="A group of three people, Jim Hernandez, Carl Villanueva, and Denelle Ocsena, created the game CodeQuest. One of the most challenging subjects to take, according to some, is programming. Therefore, our aim was to develop an educational game that teaches programming while allowing players to have fun and be delighted.", font=("Arial", 15), bg="#2F4D62", fg="#00F3FA", wraplength=700)
    infobg_label.pack(pady=30)


def clear_settings_frame():
    for widget in settings_frame.winfo_children():
        widget.destroy()

def back():
    window.destroy()
    subprocess.call(['python', 'menu.py'])

audio_image = PhotoImage(file="images/audiob.png")
language_image = PhotoImage(file="images/languageb.png")
info_image = PhotoImage(file="images/infob.png")
back_image2 = PhotoImage(file="images/backb.png")

parent_frame = Frame(window, bg="#162334")
parent_frame.pack(fill=BOTH, expand=True)

buttons_frame = Frame(parent_frame, bg="#162334")
buttons_frame.pack(side=LEFT, fill=Y)

title = Label(buttons_frame, text="Settings", bg="#162334", fg="#FFBD59", font=("Arial", 24, "bold"))
title.pack(padx=50, pady=30)

button1 = Button(buttons_frame, image=audio_image, bg="#162334", bd=0, activebackground="#162334", command=show_audio_settings)
button1.pack(padx=50, pady=10)

button2 = Button(buttons_frame, image=language_image, bg="#162334", bd=0, activebackground="#162334", command=show_language_settings)
button2.pack(padx=50, pady=10)

button3 = Button(buttons_frame, image=info_image, bg="#162334", bd=0, activebackground="#162334", command=show_info_settings)
button3.pack(padx=50, pady=10)

button4 = Button(buttons_frame, image=back_image2, bg="#162334", bd=0, activebackground="#162334", command=back)
button4.pack(padx=50, pady=10)

settings_frame = Frame(parent_frame, bg="#2F4D62", width=800, height=500)
settings_frame.pack(side=RIGHT, fill=BOTH, expand=True)

window.mainloop()
