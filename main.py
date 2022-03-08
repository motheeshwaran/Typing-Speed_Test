# Using Tkinter and what you have learnt about building GUI applications with Python,
# Gives the user how many words they can type per minute.
#
# The average typing speed is 40 words per minute. But with practice,
# you can speed up to 100 words per minute.
#
# You can try out a web version here: https://typing-speed-test.aoeu.eu/
#
from tkinter import *
from PIL import ImageTk, Image

tex="The journey of life may not always be smooth but we must keep going and\nstay positive all the times. Life is the most precious asset on this planet\nand must be protected irrespective of its form and appearance Every\nspecies not only humans, have a fundamental right to live their life, I\nwhatever way they desire Life is a gift of God to humanity and any attempt\nto disrupt or damage it will have undesirable consequences. Challenges\nare a part of life. We face different challenges at different points in life.\nWhile some people look at these challenges as an opportunity to learn \nsomething new others get disheartened \nand succumb to them. We learn many new things as we take \non different challenges."
new_text = ""
for i in tex:
    if i != " " and i !='\n' :
        new_text += i

def start_test():
    entry_text.config(state="normal")
    entry_text.delete(0,END)
    entry_text.focus_set()
    window.after(60000, result)

def result():
    entry_text.config(state="disabled")
    word=entry_text.get()
    count=0
    entered_text=""
    for i in word:
        if i != " ":
            entered_text += i
    for i in range(0,len(entered_text)):
        if new_text[i]==entered_text[i]:
            count+=1
    # Close window funtion
    bgc="#FFF89A"
    def close():
        new.destroy()
    new = Toplevel(window)
    new.config(padx=90,pady=10,bg=bgc)
    new.title("Result")
    # Create a Label in New window
    Label(new, text="Your Result", font=('Helvetica 20 bold'),bg=bgc).pack(pady=10)
    Label(new, text=f"You scored {count} CPM \nYou typed {int(count/5)} WPM\nTotal CPM is {len(entered_text)} ", font=('Helvetica 16 bold'),bg=bgc).pack(pady=10)
    Button(new,image=exit_img,command=close,border=0,bg=bgc,activebackground=bgc).pack()

# ------------------------ Creating Window -----------------------------

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=1000,height=600)
window.config(padx=30,bg="#B8E4F0")
window.resizable(FALSE,FALSE)

heading = Label(text="TYPING SPEED TEST",font=("Helvetica",36,"bold"),bg="#B8E4F0",pady=30)
heading.pack()

para=Label(text="How fast are your fingers? Do the one-minute typing test to find out!\n "
                "Press the space bar after each word. At the end, you'll get your typing speed in WPM.\n"
                "Good luck!")
para.config(font=("Times", 16,"italic"),bg="#B8E4F0")
para.pack()

canvas=Canvas(width=700,height=200)

word=Label(text=tex)
canvas.create_text(353,137,text=tex,font=("Helvetica",16))
canvas.pack(pady=20)

text=Label(text="Type here: ",bg="#B8E4F0",font=("Times", 12))
text.pack()

entry_text=Entry(width=48,font=('Arial 20'))
entry_text.insert(0,"Type the above paragraph here")
entry_text.config(state="disabled")
entry_text.pack()

# Open Image
img= Image.open("start_button.png")
e_img= Image.open("Exit.png")
# Resize Image
new_img=img.resize((130,60),Image.ANTIALIAS)
ex_img=e_img.resize((130,60),Image.ANTIALIAS)
# converting to TKinter supported format
start_img = ImageTk.PhotoImage(new_img)
exit_img = ImageTk.PhotoImage(ex_img)
# Adding Image to button

start = Button(image=start_img,command=start_test,border=0,bg="#B8E4F0",activebackground="#B8E4F0")
start.pack(pady=30)

window.mainloop()
