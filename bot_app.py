import tkinter as tk
from PIL import Image, ImageTk
import finalsearch

def search_query():
    search_query = search_var.get()
    print(search_query)
    finalsearch.main(search_query)
    


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3 , rowspan=5)

logo = Image.open("TKLogo.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

instructions = tk.Label(root, text="Enter Your Query" , font="Raleway")
instructions.grid(columnspan=3,column=0,row=1)


search_var = tk.StringVar()

search_entry = tk.Entry(root,textvariable = search_var, font="Raleway")
search_entry.grid(columnspan=3,column=0,row=2)
search_box = tk.StringVar()
search_btn = tk.Button(root, command=lambda:search_query() ,textvariable=search_box , font="Raleway" , bg='#20bebe' , fg='white' , height=2,width=50)
search_box.set("Search")
search_btn.grid(column=1,row=3)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()

