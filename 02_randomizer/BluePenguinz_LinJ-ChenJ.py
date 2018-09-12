#Jiayang Chen, Jason Lin
#SoftDev1 pd7
#K02 -- NO-body expects the Spanish Inquisition!
#2018-09-07

from random import randint

KREWES = {

        'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],

        'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],

        'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']

}
# Returns a random name from a given team
def random_name_team(team):
    students = KREWES[team] # List of students from selected team
    person = students[randint(0,len(students)-1)] # A random student is chosen from the selected team
    return person

# Without a given team
def random_name():
    team = "wmx"[randint(0,2)] # Chooses a random team name
    return random_name_team(team) # Calls the rando_name_team function with the randomly selected team

choice = input("Would you like to choose a team? (y/n): ")

# User's input cannot be empty or more than 1 character
# User's input has to be "y" or "n"
while ("yn".count(choice)!=1 or len(choice) != 1):
    print("Sorry fam, that is not a valid input. Type either 'y' for yes or 'n' for no\nand then press ENTER")
    choice = input("Would you like to choose a team? (y/n): ")

# User wants to choose a team
if choice == "y":
    team = input("Pick a team (w/m/x): ")

    # User's input should be a valid team name
    while ("wmx".count(team)!=1 or len(team) != 1):
        print("Sorry fam, that team does not exist. Please type either 'w', 'm', or 'x'\nand then press ENTER")
        team = input("Pick a team (w/m/x): ")
    print(random_name_team(team))

# User wants a random team
elif choice == "n":
    print(random_name())
