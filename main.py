import tkinter as tk
import style as st
import databaseColor as db
import MenuBar as menuBar


class Window:
    def __init__(self, master):
        self.master = master
        st.Style(self.master)
        menuBar.starting(self.master)


if __name__ == '__main__':
    db.systemColor()
    root = tk.Tk()
    app = Window(root)
    root.overrideredirect(True)
    root.mainloop()
