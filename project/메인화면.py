import tkinter
import tkinter.font
from login_window import LoginWindow  # Import the LoginWindow class
from word_description_window import WordDescriptionWindow
import customtkinter
from customtkinter import *
from PIL import Image

# 기본 색상
bgColor = "#FFDFB9"
fgColor = "#A4193D"
hoverColor = "#C850C0"

# 메인 화면 창 생성
window = customtkinter.CTk()
window.title("TOEICVOCAMACA")
window.geometry("400x500+100+100")
window.resizable(False, False)
window.config(background=bgColor)

font = tkinter.font.Font(family="맑은 고딕", size=24, weight="bold")

img = customtkinter.CTkImage(light_image=Image.open("title3_wine.png"),
                             dark_image=Image.open("title3_wine.png"),
                             size=(300, 300))
title_label = customtkinter.CTkLabel(window, text="", bg_color=bgColor, image=img)
title_label.pack()

# 로그인 버튼
login_window_instance = LoginWindow(window)  # Create an instance of LoginWindow
button_login = customtkinter.CTkButton(master=window, text="로그인", 
                                       bg_color=bgColor, fg_color=fgColor, 
                                       hover_color=hoverColor, 
                                       corner_radius=32, 
                                       command=login_window_instance.open_login_window)
button_login.place(relx=0.5, rely=0.5, anchor="center")

# 단어장 설명 버튼
description_window_instance = WordDescriptionWindow(window)  # Create an instance of WordDescriptionWindow
button_description = customtkinter.CTkButton(master=window, 
                                             text="단어장 설명", 
                                             bg_color=bgColor, 
                                             fg_color=fgColor, 
                                             hover_color=hoverColor, 
                                             corner_radius=32, command=description_window_instance.open_description_window)
button_description.place(relx=0.5, rely=0.6, anchor="center")

window.mainloop()
