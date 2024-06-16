import tkinter as tk

def button_pushed():
    print('button has been pushed')
    name = entry.get()
    entry.selection_clear()
    entry.delete(0, tk.END)
    print(name)
    text.insert("1.0", name + "\n")
    #text.pack()
    #exit()

window = None
window = tk.Tk()
assert window != None

window.title = ''
window.geometry('640x480')

label = tk.Label(master=window,
                 text="Welcome to this magnificent piece of software!!")
label.pack()

text = tk.Text(master=window,
               )
text.pack()

label = tk.Label(master=window,
                 text="What is going on?!")
label.pack()

entry = tk.Entry(master=window,
                 width=48)
entry.pack()

button = tk.Button(master=window,
                   text='⚠️Click Me If You Dare!!⚠️',
                   command=button_pushed)
button.pack()

window.mainloop()
