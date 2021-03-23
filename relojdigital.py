import tkinter as tk
from tkinter import ttk
import time


class RelojDigital(tk.Tk):
    def __init__(self):
        super().__init__()


        #configurar la ventana
        self.title("Reloj Digital")
        self.resizable(0,0)
        self.geometry("250x80")
        self["bg"] = "black"


        #cambiamos color de fondo
        self.style = ttk.Style(self)
        self.style.configure(
            "TLabel",
            background="Black",
            foreground="red")

        #Label
        self.label = ttk.Label(
            self,
            text=self.tiempo_string(),
            font=("Digital-7", 40))

        self.label.pack(expand=True)

        self.label.after(1000, self.update)

    def tiempo_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):

        self.label.configure(text=self.tiempo_string())

        self.label.after(1000, self.update)



if __name__ == "__main__":
    reloj = RelojDigital()
    reloj.mainloop()
            

        

        