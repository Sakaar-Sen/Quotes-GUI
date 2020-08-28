import requests
from tkinter import *
from tkinter import messagebox
import random
import os


i = 0
def fetch():
    global i
    global data
    global text
    global author 
    try:
        response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&json=?')
        data = response.json()
    except:
        messagebox.showinfo("Error", "Could not get a quote. Please try again!")
    text = data["quoteText"]
    author = data["quoteAuthor"]
    messagebox.showinfo(author, text)

def savequote():
    f = open("Saved Quotes.txt", "a")
    f.write("\n\n\nQuote: {} \nAuthor: {}".format(text, author))
    f.close()


master = Tk()
master.title("v1.0.0")

label1 = Label(master, text = "Quotes Application", font =("Helvetica" , 28, "bold")).grid(row = 0, column = 0, padx = 30, pady=30)
button1 = Button(master, text ="Generate quote", command= fetch).grid(row = 1, column = 0, columnspan = 1, ipadx = 40, ipady=20, padx = 20, pady=10)
button2 = Button(master, text ="Save", command= savequote).grid(row = 2, column = 0, columnspan = 1, ipadx = 40, ipady=20, padx = 20, pady=10)
button3 = Button(master, text = "Exit", command = master.quit).grid(row = 3, column = 0, columnspan = 1, ipadx = 40, ipady=20, padx = 20, pady =10)


master.mainloop()