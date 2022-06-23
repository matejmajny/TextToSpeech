import pyttsx3
import tkinter as tk
engine = pyttsx3.init()

def button1():
    x1 = entry1.get()
    x2 = value_inside.get()
    
    match x2:
        case "Select speed":
            warning = tk.Tk()
            warning.title("Warning!")
            canvas2 = tk.Canvas(warning, width=250, height=80)
            canvas2.pack()
            t = tk.Label(warning, text="Please enter valid speed")
            t.config(font=("helvetica", 15), fg="Red")
            canvas2.create_window(125, 40, window=t)
        case "Fast":
            speed = 270
        case "Medium":
            speed = 135
        case "Slow":
            speed = 50
    
    engine.setProperty("rate", speed)
    engine.say(x1)
    engine.runAndWait()

root = tk.Tk()
root.title("TTS by Matt v1.0")
canvas1 = tk.Canvas(root, width=400, height=200)
canvas1.pack()

entry1 = tk.Entry(root, width=45)
canvas1.create_window(250, 130, window=entry1)

label1 = tk.Label(root, text="Enter text: ")
canvas1.create_window(60, 130, window=label1)

label2 = tk.Label(root, text="TextToSpeech")
label2.config(font=("helvetica", 20))
canvas1.create_window(200, 50, window=label2)

button1 = tk.Button(root, text="Say the text! ", command=button1, width=15, fg="white", bg="green")
canvas1.create_window(115, 175, window=button1)

#option menu

options = ["Fast", "Slow", "Medium", "Select speed"]
value_inside = tk.StringVar(root)
value_inside.set(options[3])
variable = tk.StringVar()
option_menu = tk.OptionMenu(root, value_inside, *options)
option_menu.config(bg="orange", fg="black", width=15)
canvas1.create_window(265, 175, window=option_menu)

root.mainloop()