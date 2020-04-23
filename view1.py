'''
  Created on 2020/04/19
  @author wlabagnara

  View1 Class
'''


print("View1 run as: {}".format(__name__))


import tkinter as tk      # ** GUI MODULES **
from tkinter import ttk


class View1(tk.Tk):  # Inherits from tkinter (tkinter is view's base class)

    # Class variables
    PAD = 40

    def __init__(self, controller):  # View is aware of the Controller
        super().__init__()  # b/c inheriting from tkinter, this insures tkinter's constructor is called

        self.controller = controller     # initialize class properties
        self.value_var = tk.StringVar()  # will use for Entry text

        # Initialize view
        self.title('Gizmo1.0')
        self.geometry('250x200')
        self._make_main_frame()

        self._make_entry()
        self._make_button()

    def main(self):
        print('View1.main executed...')

        self.mainloop()  # Main GUI Infinite Loop (inherited from tkinter)

    def update_button(self):
        if self.btn['text'] == "CLICK HERE":
            self.btn['text'] = "CLICKED"
        elif self.btn['text'] == "CLICKED":
            self.btn['text'] = "CLICKED AGAIN"
        elif self.btn['text'] == "CLICKED AGAIN":
            self.btn['text'] = "CLICKED"

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_button(self):
        self.btn = ttk.Button(self.main_frm, text="CLICK HERE", width=20,
                              command=self.controller.on_button_click  # binding button click event
                              )
        self.btn.pack()

    def _make_entry(self):
        self.value_var.set("0")
        ent = ttk.Entry(self.main_frm, textvariable=self.value_var, justify='right', state='disabled')
        ent.pack(fill='x')


