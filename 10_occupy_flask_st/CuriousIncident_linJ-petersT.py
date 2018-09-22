#CuriousIncident -- Theodore Peters, Jason Lin
#SoftDev1 pd07
#K10 -- Jinja Tuning
#2018-09-22

from flask import Flask,render_template
import csv
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, there! Click <a href='/occupations'> here</a> to go to where you want to go."

@app.route("/occupations")
def occupation_generator():
    csvDict = makeDict("./data/occupations.csv")
    return render_template("occupationPage.html",
                           dict=csvDict,
                           randomJob=randOccupation(csvDict))

def makeDict(file):

    someDict = {}

    # Open csv file
    with open(file, newline='') as csvfile:

        # A reader object iterates through
        # and separates each row by comma into a string array
        csvfile = csv.reader(csvfile, delimiter=',')

        # For each row, assign string 0 as the key, and
        # string 1 in int (percentage*10) form as the value
        # exclude the first and the "Total" row
        rowNum = 0
        for row in csvfile:
            if rowNum != 0:
                someDict[row[0]] = float(row[1])
            rowNum += 1
        someDict.pop('Total')

    return someDict

def randOccupation(occupationDict):

    # num is a random int from 0 - 998
    num = randint(0, 1000)/10
    print(num)

    # Sum the percentages of the occupations until
    # you get to a sum greater than num
    # (the interval between sums is your percentage)
    # Break once this is true
    Sum = 0
    for occupation in occupationDict:
        Sum += occupationDict[occupation]
        if Sum >= num:
            return occupation
            break
    return "None"

if __name__ == "__main__":
    app.debug = True
    app.run()
