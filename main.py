#! WMIC HDD SN Converter
from tkinter import *
import re


def convert():
    to_dec = str(whats_decode.get())
    dec_res = bytearray.fromhex(to_dec).decode()
    dec_len = len(dec_res)
    ltr1 = 0
    ltr2 = 2
    dec_changed = []

    for count in range(dec_len):
        if ltr1 >= dec_len:
            break
        two_ltr = dec_res[ltr1:ltr2:1]
        a = two_ltr[0]
        b = two_ltr[1]
        mix_res = b, a
        dec_changed.append(mix_res)

        ltr1 += 2
        ltr2 += 2

    # (!) try 2 find another way of cutter
    dec_changed = str(dec_changed).strip('[]')
    dec_changed = re.sub(r'\(', '', dec_changed)  # (
    dec_changed = re.sub(r'\)', '', dec_changed)  # )
    dec_changed = re.sub(r'\'', '', dec_changed)  # '
    dec_changed = re.sub(r',', '', dec_changed)  # ,
    dec_changed = re.sub(r' ', '', dec_changed)  # space
    view_res(dec_changed)


def view_res(dec_changed):
    result_dec_entry = Entry()
    result_dec_entry.insert(0, dec_changed)
    result_dec_entry.configure(state='readonly')
    result_dec_entry.place(relx=.1, rely=.54, height=25, width=230)


root = Tk()
root.title("WMIC HDD SN Converter")
root.geometry("300x300+100+100")

help_label = Label(text="Enter WMIC disk drive serial number")
help_label.place(relx=.08, rely=.0, height=60, width=250)

whats_decode = StringVar()
whats_decode_entry = Entry(textvariable=whats_decode)
whats_decode_entry.place(relx=.1, rely=.15, height=25, width=230)

conv_but = Button(text='Convert', height=1, width=20, command=convert)
conv_but.place(relx=.1, rely=.26, height=25, width=230)

view_label = Label(text="Result:")
view_label.place(relx=.07, rely=.45, height=30, width=250)

result_dec_entry = Entry()
result_dec_entry.configure(state='readonly')
result_dec_entry.place(relx=.1, rely=.54, height=25, width=230)

root.mainloop()
