import tkinter as tk

def button_pushed():
    print('button has been pushed')
    name = entry.get()
    print(name)
    #text.insert("I AM A VAMPIRE BAT")
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

text = tk.Text(master=window)
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
