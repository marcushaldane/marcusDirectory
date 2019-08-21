#creating the map and storing data
import random
from tkinter import *

# Build the game window
window = Tk()
window.title("Welcome to Europa")
window.geometry('375x393')


# list of colors to go onto random map
list = ["green","green","green","green","green","blue","green","blue","green","blue","green","blue","green","blue","black"]
# Build the random game map
mapData = []
tempList = []
for i in range(0,15):
    tempList = []
    for u in range(0,15):
        randColor = list[random.randint(0,len(list)-1)]
        map = Label(window, text="     ", bg=randColor)
        map.grid(column=u, row=i)
        if (randColor == "green"):
            tempList.append('L')
        elif (randColor == "blue"):
            tempList.append('W')
        else:
            tempList.append('R')
    mapData.append(tempList)
# terminal map
for v in range(0,len(mapData)-1):
    print (mapData[v])

window.mainloop()
