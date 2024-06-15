import style as st
import tkinter as tk


def starting(master):
    # self.master = master

    def move_app(e):
        master.geometry(f'+{e.x_root}+{e.y_root}')


    # $___---___$  Create Menu Bar for the System $___---___$
    # ======================================================

    Menu = tk.Menu(master)
    Menu.bind('<B1-Motion>', move_app)
    master.config(menu=Menu)
    Menu.config(font=('Courier', 18))

    file = tk.Menu(Menu, tearoff=0)
    Menu.add_cascade(label="File", menu=file)
    file.add_command(label='Go Back To Dashboard')
    file.add_command(label="Create New Seller")
    file.add_command(label="Create New Products")
    file.add_separator()
    file.add_command(label="Save")
    file.add_command(label="Save As")
    file.add_command(label="Export")
    file.add_separator()
    file.add_command(label="Exit", command=lambda: master.destroy())

    edit = tk.Menu(Menu, tearoff=0)
    Menu.add_cascade(label="Edit", menu=edit)
    edit.add_command(label="Edit Seller")
    edit.add_separator()
    edit.add_command(label="Edit Products")

    style = tk.Menu(Menu, tearoff=0)
    Menu.add_cascade(label="Style", menu=style)

    dark_style = tk.Menu(style, tearoff=0)
    style.add_cascade(label="Dark Style", menu=dark_style)
    dark_style.add_command(label='Cyborg', command=lambda: cyborg(master))
    dark_style.add_command(label='Darkly', command=lambda: darkly(master))
    dark_style.add_command(label='Solar', command=lambda: solar(master))
    dark_style.add_command(label='SuperHero', command=lambda: superhero(master))
    dark_style.add_command(label='Vapor', command=lambda: vapor(master))

    style.add_separator()

    light_style = tk.Menu(style, tearoff=0)
    style.add_cascade(label="Light Style", menu=light_style)
    light_style.add_command(label='Cerulean', command=lambda: cerulean(master))
    light_style.add_command(label='Cosmo', command=lambda: cosmo(master))
    light_style.add_command(label='Flatly', command=lambda: flatly(master))
    light_style.add_command(label='Journal', command=lambda: journal(master))
    light_style.add_command(label='Liter', command=lambda: liter(master))
    light_style.add_command(label='Lumen', command=lambda: lumen(master))
    light_style.add_command(label='Minty', command=lambda: cosmo(master))
    light_style.add_command(label='Morph', command=lambda: minty(master))
    light_style.add_command(label='Pulse', command=lambda: pulse(master))
    light_style.add_command(label='Sandstone', command=lambda: sandstone(master))
    light_style.add_command(label='Simplex', command=lambda: simplex(master))
    light_style.add_command(label='United', command=lambda: united(master))
    light_style.add_command(label='Yeti', command=lambda: yeti(master))

    Help = tk.Menu(Menu, tearoff=0)
    Menu.add_cascade(label="Help", menu=Help)
    Help.add_command(label="Helps")
    Help.add_separator()
    Help.add_command(label="Check for Update")

    about = tk.Menu(Menu, tearoff=0)
    Menu.add_cascade(label="About", menu=about)
    about.add_command(label="About Us")

    quit = tk.Menu(Menu, tearoff=0)
    Menu.add_cascade(label="Quit", menu=quit)
    quit.add_command(label="Quit", command=lambda: master.destroy())


def cerulean(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('cerulean')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def cosmo(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('cosmo')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def flatly(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('flatly')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def journal(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('journal')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def liter(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('liter')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def lumen(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('lumen')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def minty(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('minty')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def morph(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('morph')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def pulse(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('pulse')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def sandstone(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('sandstone')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def simplex(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('simplex')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def united(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('united')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def yeti(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('yeti')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def cyborg(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('cyborg')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def darkly(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('darkly')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def solar(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('solar')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def superhero(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('superhero')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


def vapor(master):
    with open("colorSystem.txt", "w") as file1:
        file1.write('vapor')

    with open("colorSystem.txt", "r") as file2:
        ThemesName = file2.read()

    st.Style(master)


