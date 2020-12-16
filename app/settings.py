# Settings - Form containing Supreme form
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_form()

    def create_form(self):
        tk.Label(self, text='Name').grid(row=0, column=0)
        self.name = tk.Entry(self).grid(row=0, column=1)

        tk.Label(self, text='Email').grid(row=1, column=0)
        self.email = tk.Entry(self).grid(row=1, column=1)

        tk.Label(self, text='Telephone').grid(row=2, column=0)
        self.tele = tk.Entry(self).grid(row=2, column=1)

        tk.Label(self, text='Address 1').grid(row=3, column=0)
        self.add1 = tk.Entry(self).grid(row=3, column=1)

        tk.Label(self, text='Address 2').grid(row=4, column=0)
        self.add2 = tk.Entry(self).grid(row=4, column=1)

        tk.Label(self, text='Address 3').grid(row=5, column=0)
        self.add3 = tk.Entry(self).grid(row=5, column=1)

        tk.Label(self, text='City').grid(row=6, column=0)
        self.city = tk.Entry(self).grid(row=6, column=1)

        tk.Label(self, text='Postcode').grid(row=7, column=0)
        self.postcode = tk.Entry(self).grid(row=7, column=1)

        tk.Label(self, text='Card Details').grid(row=8, column=0)

        tk.Label(self, text='Card Number').grid(row=9, column=0)
        self.card_no = tk.Entry(self).grid(row=9, column=1)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()