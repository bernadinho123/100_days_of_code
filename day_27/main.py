import tkinter

# window = tkinter.Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=300)
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)
#
#
# # Button
# def button_clicked():
#     new_text = input.get()
#
#     my_label["text"] = new_text
#
#
# button = tkinter.Button(text="click me", command=button_clicked)
# button.grid(column=1, row=1)
# # Entry
# input = tkinter.Entry(width=10)
# input.grid(column=3, row=2)
#
# new_button = tkinter.Button(text="hello", command = button_clicked)
# new_button.grid(column=2, row=0)
# window.mainloop()
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(pady=20,padx=20)

equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)
equal.config(padx=10, pady=10)
miles = tkinter.Label(text="miles")
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)
km = tkinter.Label(text="km")
km.grid(column=2, row=1)
km.config(padx=10, pady=10)


def answer():
    new_text = float(num_toconvert.get())*1.60934
    result["text"] = new_text


num_toconvert = tkinter.Entry()
num_toconvert.grid(column=1, row=0)
# num_toconvert.config(padx=10, pady=10)
calculate = tkinter.Button(text="Calculate", command=answer)
calculate.grid(column=1, row=2)
calculate.config(padx=10, pady=10)
result = tkinter.Label(text=0)
result.grid(column=1, row=1)
result.config(padx=10, pady=10)
window.mainloop()
