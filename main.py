from tkinter import *
from question_model import Question1
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
import html
import sys
from tkinter import ttk
THEME_COLOR = "#1e2324"


win = Tk() #creating an Tkinter frame
win.geometry("600x600")#the size of the window when launched
win.title("Fun quiz main menu") #title of the application when launched
button = ttk.Button(win, text = "start", command= win.destroy, width = 50) #start button
button.pack()

button2= ttk.Button(win,text= "quit", command= quit) #quit button
button2.pack()

#to make the system close when user clicks quit
def quit():
    sys.exit()
    

win.mainloop()
    
#these codes will manage and link the other python scripts into one to form as my main quiz
question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question1(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
