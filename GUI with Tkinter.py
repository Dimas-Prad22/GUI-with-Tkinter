import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text=" Attack !!!")
    label2.pack()

label = tkinter.Label(main_window, text="Hello World War 3 !\n")

tombol = tkinter.Button(main_window,text="Start War", command=event_tekan)

label.pack()

tombol.pack()

main_window.mainloop()