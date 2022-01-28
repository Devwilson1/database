from tkinter import *
from tkinter import ttk

#ROOT Setup
root = Tk()
root.title("Stipends")

#MainFrame Window 
window = ttk.Frame(root, padding="3 3 12 12", width=400, height=250)
window.grid(column=0, row=0, sticky=(N, W, E, S))

#Input Variables
name_var = StringVar()
assignment_var = StringVar()
date_var = StringVar()
credit_var = StringVar()
debit_var = StringVar()
comment_var = StringVar()

#Input Fields[Left Side]
name_lbl = ttk.Label(window, text="name: ")
name_lbl.grid(column=1, row=0, sticky=W)
name = ttk.Entry(window, textvariable=name_var)
name.grid(column=1, row=1, sticky='we',columnspan=3)

assignment_lbl = ttk.Label(window, text="assigment: ")
assignment_lbl.grid(column=1, row=2, sticky=W)
assignment = ttk.Entry(window, textvariable=assignment_var)
assignment.grid(column=1, row=3, sticky='we',columnspan=3)

date_lbl = ttk.Label(window, text="date: ")
date_lbl.grid(column=1, row=4, sticky=W)
date = ttk.Entry(window, textvariable=date_var)
date.grid(column=1, row=5, sticky='we',columnspan=3)

credit_lbl = ttk.Label(window, text="credit: ")
credit_lbl.grid(column=1, row=6, sticky=W)
credit = ttk.Entry(window, textvariable=credit_var)
credit.grid(column=1, row=7, sticky='we',columnspan=3)

debit_lbl = ttk.Label(window, text="debit: ")
debit_lbl.grid(column=1, row=8, sticky=W)
debit = ttk.Entry(window, textvariable=debit_var)
debit.grid(column=1, row=9, sticky='we',columnspan=3)

comment_lbl = ttk.Label(window, text="comment: ")
comment_lbl.grid(column=1, row=10, sticky=W)
comment = ttk.Entry(window, textvariable=comment_var)
comment.grid(column=1, row=11, sticky='we',columnspan=3)
