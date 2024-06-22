from tkinter import *
from PIL import Image,ImageTk
from random import randint

# Main Window
root = Tk()
root.title('ROCK-PAPER-SCISSOR GAME')
root.configure(background="Grey20")

# Picture
rock_img = ImageTk.PhotoImage(Image.open("Rock paper Scissor/Rock_user.jpg"))
paper_img = ImageTk.PhotoImage(Image.open("Rock paper Scissor/Paper_user.jpg"))
scissor_img = ImageTk.PhotoImage(Image.open("Rock paper Scissor/Scissor_user.jpg"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Rock paper Scissor/Rock_comp.jpg"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Rock paper Scissor/Paper_comp.jpg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Rock paper Scissor/Scissor_comp.jpg"))

# insert Pictur
user_label = Label(root,image=scissor_img,bg='Green')
comp_label = Label(root,image=scissor_img_comp,bg='Red')
user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)

# scores
playerScore = Label(root,text=0,font=100,bg='Grey20',fg='Green')
computerscore = Label(root,text=0,font=100,bg='Grey20',fg='Red')
playerScore.grid(row=1,column=1)
computerscore.grid(row=1,column=3)

# Indicators
user_indicator = Label(root,font=50,text="USER",
                       bg='grey20',fg='Green').grid(row=0,column=1)
comp_indicator = Label(root,font=50,text="COMPUTER",
                       bg='Grey20',fg='Red').grid(row=0,column=3)

# Messages
msg = Label(root, font=50, bg='Grey20', fg='white')
msg.grid(row=3,column=2)

# Update Message 
def updateMessages(x) :
    msg['text'] = x
    
    
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore['text'] = str(score)
def updateComuterScore():
    score = int(computerscore["text"])
    score += 1
    computerscore['text'] = str(score)

# check Winner
def checkWinner(player,computer) :
    if player == computer:
        updateMessages("TIE")
    elif player == 'rock':
        if computer == 'paper' :
            updateMessages("YOU LOOSE")
            updateComuterScore()
        else:
            updateMessages("YOU WIN")
            updateUserScore()
    elif player == 'paper' :
        if computer == 'scissor':
            updateMessages("YOU LOOSE")
            updateComuterScore()
        else :
            updateMessages("YOU WIN")
            updateUserScore()
    elif player == 'scissor':
        if computer == 'rock':
            updateMessages("YOU LOOSE")
            updateComuterScore()
        else :
            updateMessages("YOU WIN")
            updateUserScore()
    
    
# Update Choices
choices = ["rock","paper","scissor"]
def updateChoice(x) :
    # Comp --------
    compChoice = choices[randint(0,2)]
    if compChoice == "rock" :
        comp_label.configure(image=rock_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else :
        comp_label.configure(image=scissor_img_comp)
    
    # User --------
    if x == 'rock' :
        user_label.configure(image=rock_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else :
        user_label.configure(image=scissor_img)
        
    checkWinner(x,compChoice)

# Buttons
rock = Button(root,width=20,height=3,text="ROCK",command= lambda : updateChoice("rock"),
              bg='Grey20',fg='white').grid(row=2,column=1)
paper = Button(root,width=20,height=3,text="PAPER",command= lambda : updateChoice("paper"),
               bg='Grey20',fg='white').grid(row=2,column=2)
Scissor = Button(root,width=20,height=3,text="SCISSOR",command= lambda : updateChoice("scissor"),
                 bg='Grey20',fg='white').grid(row=2,column=3)


root.mainloop()