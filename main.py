import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

screen = Tk()
screen.title("Pokemon App")
screen.config(padx=30,pady=30)

logo = Image.open("Pokemon.png")
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(screen, image=logo)
logo_label.pack()

def get_pokemon_info():
    pokemon_name = name_entry.get()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"].capitalize()
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        types = [pokemon_type["type"]["name"] for pokemon_type in data["types"]]
        space_label = Label()
        space_label.config(padx=10, pady=10)
        space_label.pack()
        name_desc_label = Label(text="Name:")
        name_desc_label.pack()
        name_showed_label = Label(text=name, bg="black",fg="green")
        name_showed_label.pack()
        ability_title_label = Label(text="Abilities:")
        ability_title_label.pack()
        ability_label = Label(text=f"{", ".join(abilities)}", bg="black",fg="green")
        ability_label.pack()
        type_title_label = Label(text="Types:")
        type_title_label.pack()
        type_label = Label(text=f"{", ".join(types)}", bg="black", fg="green")
        type_label.pack()
    else:
        messagebox.showerror("Error","Pokemon not found!")

    name_entry.delete(0,END)


name_label = Label(text="Enter a pokemon name:")
name_label.pack()
name_entry = Entry()
name_entry.pack()
search_button = Button(text="Search", command=get_pokemon_info)
search_button.pack()

screen.mainloop()

