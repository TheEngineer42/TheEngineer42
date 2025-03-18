from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

HEIGHT = 500
WIDTH = 800

window = Tk()
window.title('Bubble Blaster')
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
canvas.pack()

shipId = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
shipId2 = canvas.create_oval(0, 0, 30, 30, outline='red')

SHIPR = 15
MIDX = WIDTH / 2
MIDY = HEIGHT / 2
canvas.move(shipId, MIDX, MIDY)
canvas.move(shipId2, MIDX, MIDY)

SHIPSPD = 10

def moveShip(event):
    if event.keysym == 'Up':
        canvas.move(shipId, 0, -SHIPSPD)
        canvas.move(shipId2, 0, -SHIPSPD)
    elif event.keysym == 'Down':
        canvas.move(shipId, 0, SHIPSPD)
        canvas.move(shipId2, 0, SHIPSPD)
    elif event.keysym == 'Left':
        canvas.move(shipId, -SHIPSPD, 0)
        canvas.move(shipId2, -SHIPSPD, 0)
    elif event.keysym == 'Right':
        canvas.move(shipId, SHIPSPD, 0)
        canvas.move(shipId2, SHIPSPD, 0)

canvas.bind_all('<Key>', moveShip)

bubId = []
bubR = []
bubSpd = []

MINBUBR = 10
MAXBUBR = 30
MAXBUBSPD = 10
GAP = 100

def createBubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MINBUBR, MAXBUBR)
    id1 = canvas.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bubId.append(id1)
    bubR.append(r)
    bubSpd.append(randint(1, MAXBUBSPD))

def moveBubbles():
    for i in range(len(bubId)):
        canvas.move(bubId[i], -bubSpd[i], 0)

def getCoords(idNum):
    pos = canvas.coords(idNum)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def delBubble(i):
    del bubR[i]
    del bubSpd[i]
    canvas.delete(bubId[i])
    del bubId[i]

def cleanUpBubs():
    for i in range(len(bubId) - 1, -1, -1):
        x, _ = getCoords(bubId[i])
        if x < -GAP:
            delBubble(i)

def distance(id1, id2):
    x1, y1 = getCoords(id1)
    x2, y2 = getCoords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def collision():
    points = 0
    for bub in range(len(bubId) - 1, -1, -1):
        if distance(shipId2, bubId[bub]) < (SHIPR + bubR[bub]):
            points += (bubR[bub] + bubSpd[bub])
            delBubble(bub)
    return points

canvas.create_text(50, 30, text='TIME', fill='white')
canvas.create_text(150, 30, text='SCORE', fill='white')
timeText = canvas.create_text(50, 50, fill='white')
scoreText = canvas.create_text(150, 50, fill='white')

def showScore(score):
    canvas.itemconfig(scoreText, text=str(score))

def showTime(timeLeft):
    canvas.itemconfig(timeText, text=str(timeLeft))

BUBCHANCE = 10
TIMELIMIT = 30
BONUSSCORE = 1000

score = 0
bonus = 0
end = time() + TIMELIMIT

# MAIN LOOP
while time() < end:
    if randint(1, BUBCHANCE) == 1:
        createBubble()
    moveBubbles()
    cleanUpBubs()
    score += collision()
    if (int(score / BONUSSCORE)) > bonus:
        bonus += 1
        end += TIMELIMIT
    showScore(score)
    showTime(int(end - time()))
    window.update()
    sleep(0.01)

canvas.create_text(MIDX, MIDY, text='GAME OVER', fill='white', font=('Helvetica', 30))
canvas.create_text(MIDX, MIDY + 30, text='Score: ' + str(score), fill='white')
canvas.create_text(MIDX, MIDY + 45, text='Bonus time: ' + str(bonus * TIMELIMIT), fill='white')
