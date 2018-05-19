# import the modules
import tkinter
import random

# lists of English words and Chinese translations which you defined
wordstr='salad,jammy,pastry,blender,mustard,doughnut,crust,onion,ketchup,pudding,aperitif,caviar,pie,broth,cheese'
hzstr='色拉，涂果酱的，酥皮点心，搅拌机，芥茉，甜甜圈，面包皮，洋葱，番茄酱，布丁，开胃酒，鱼子酱，馅饼，肉汤，乳酪'
wronglst=[]
wordlst=wordstr.split(',')
hzlst=hzstr.split('，')

score = 0
# the location of the 2 lists.
R=0
# the game time left, initially 60 seconds.
timeleft = 60

# function that will start the game.
def startGame(event):
    if timeleft == 60:
        # start the countdown timer.
        countdown()

    # run the function to
    # choose the next colour.
    nextWord()

# Function to choose and
# display the next colour.
def nextWord():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
    global R

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        if e.get().lower() == wordlst[R].lower():
            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        R=random.randint(0,len(wordlst)-1)
        label.config(fg=str('red'), text=str(hzlst[R]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: "
                              + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)

# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("TYPING GAME")

# set the size
root.geometry("375x250")

# add an instructions label
instructions = tkinter.Label(root, text="", font=('Helvetica', 12))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",fg=str('red'),
                           font=('Helvetica', 24))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), fg=str('blue'),font=('Helvetica', 12))
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 48))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()