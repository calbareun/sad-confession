import tkinter 

window = tkinter.Tk()
window.geometry("500x500")
window.title("asking")

text_long = tkinter.StringVar()
text_long.set("Jennifer is a young woman in her mid-20s, with a warm and inviting personality that instantly puts people at ease. She has a contagious enthusiasm for life, always approaching each day with a positive outlook. Jennifer has a radiant smile that lights up her face and a twinkle in her eyes that reflects her sense of humor. Physically, Jennifer is of average height, with a slender and athletic build. Her wavy chestnut hair falls gracefully around her shoulders, and she often pulls it back into a ponytail when she's on the go. She has a few freckles scattered across her nose, giving her a playful and approachable appearance.")

# Create Text widget
dumb_message = tkinter.Text(window, wrap="word")
dumb_message.pack()

# Insert the initial content of text_long into the Text widget
dumb_message.insert(tkinter.END, text_long.get())

# Define functions
def button_no():
    if button_no["text"] == "no":
        text_long.set("can i date her?")
        update_text()
        button_yes.config(state=tkinter.DISABLED)

def button_yes():
    if button_yes["text"] == "yes":
        text_long.set("i'll help she's my bets friend ")
        update_text()
        button_no.config(state=tkinter.DISABLED)

# Update the Text widget content based on text_long
def update_text():
    dumb_message.delete("1.0", tkinter.END)  # Clear existing content
    dumb_message.insert(tkinter.END, text_long.get())  # Insert updated content

# Create buttons with their respective functions
button_no = tkinter.Button(window, text="no", command=button_no)
button_no.pack()

button_yes = tkinter.Button(window, text="yes", command=button_yes)
button_yes.pack()

window.mainloop()
