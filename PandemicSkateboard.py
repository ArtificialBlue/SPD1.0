#Augmented Reality Board Games Software Schedule
#First Board Game: "Pandemic" by Z-Man games
import random
#import pygame

redCounter = 24
yellowCounter = 24
blueCounter = 24
blackCounter = 24

#Implement Graph System 
currentCity = "Atlanta"
#Properties of Each City: Connecting Cities, Infection Level, Virus Color, and Research Station Established

graph = { "Atlanta" :      [["Miami","Washington","Chicago"],0,"Blue",True],
          "Chicago" :      [["San Francisco", "Montreal","Atlanta"],0,"Blue",False],
          "Washington" :   [["Atlanta", "New York", "Montreal", "Miami"],0,"Blue",False],
          "Montreal" :     [["Chicago","New York","Washington"],0,"Blue",False],
          "New York" :     [["Montreal", "Washington", "London", "Madrid"],0,"Blue",False],
          "San Francisco": [["Los Angeles", "Chicago","Tokyo","Manila"],0,"Blue",False],
          "London":        [["New York","Madrid","Paris","Essen",],0,"Blue",False],
          "Paris":         [["Madrid","London","Essen","Milan","Algiers"],0,"Blue",False],
          "Madrid":        [["New York","London","Paris","Algiers","Sao Paulo"],0,"Blue",False],
          "Essen":         [["London","Paris","Milan","St.Petersburg"],0,"Blue",False],
          "Milan":         [["Essen","Paris","Istanbul"],0,"Blue",False],
          "St.Petersburg": [["Essen","Istanbul","Moscow"],0,"Blue",False],
          "Los Angeles":   [["San Francisco","Chicago","Mexico City","Sydney"],0,"Yellow",False],
          "Mexico City":   [["Los Angeles","Chicago","Miami","Bogota","Lima"],0,"Yellow",False],
          "Miami":         [["Washington","Atlanta","Mexico City","Bogota"],0,"Yellow",False],
          "Bogota":        [["Mexico City","Miami","Lima","Buenos Aires","Sao Paulo"],0,"Yellow",False],
          "Lima":          [["Mexico City","Bogota","Santiago"],0,"Yellow",False],
          "Santiago":      [["Lima"],0,"Yellow",False],
          "Buenos Aires":  [["Bogota","Sao Paulo"],0,"Yellow",False],
          "Sao Paulo":     [["Buenos Aires","Bogota","Madrid","Lagos"],0,"Yellow",False],
          "Lagos":         [["Sao Paulo","Kinshasa","Khartoum"],0,"Yellow",False],
          "Kinshasa":      [["Lagos","Khartoum","Johannesburg"],0,"Yellow",False],
          "Johannesburg":  [["Kinshasa","Khartoum"],0,"Yellow",False],
          "Khartoum":      [["Johannesburg","Kinshasa","Lagos","Cairo"],0,"Yellow",False],
          "Cairo":         [["Algiers","Istanbul","Baghdad","Riyadh","Khartoum"],0,"Yellow",False],
          "Algiers":       [["Madrid","Paris","Istanbul","Baghdad","Riyadh","Khartoum"],0,"Black",False],
          "Istanbul":      [["Milan","St.Petersburg","Algiers","Cairo","Baghdad","Moscow"],0,"Black",False],
          "Moscow":        [["St.Petersburg","Istanbul","Tehran"],0,"Black",False],
          "Baghdad":       [["Istanbul","Tehran","Karachi","Riyadh","Cairo"],0,"Black",False],
          "Riyadh":        [["Cairo","Baghdad","Karachi"],0,"Black",False],
          "Tehran":        [["Moscow","Baghdad","Karachi","Delhi"],0,"Black",False],
          "Karachi":       [["Baghdad","Tehran","Delhi","Mumbai","Riyadh"],0,"Black",False],
          "Mumbai":        [["Karachi","Delhi","Chennai"],0,"Black",False],
          "Delhi":         [["Tehran","Karachi","Mumbai","Chennai","Kolkata"],0,"Black",False],
          "Chennai":       [["Mumbai","Delhi","Kolkata","Bangkok","Jakarta"],0,"Black",False],
          "Kolkata":       [["Delhi","Chennai","Bangkok","Hong Kong"],0,"Black",False],
          "Hong Kong":     [["Kolkata","Bangkok","Ho Chi Minh","Manila","Taipei","Shanghai"],0,"Red",False],
          "Bangkok":       [["Kolkata","Chennai","Jakarta","Ho Chi Minh","Hong Kong"],0,"Red",False],
          "Jakarta":       [["Chennai","Bangkok","Ho Chi Minh","Sydney"],0,"Red",False],
          "Ho Chi Minh":   [["Jakarta","Bangkok","Hong Kong","Manila"],0,"Red",False],
          "Manila":        [["Ho Chi Minh","Hong Kong","Taipei","San Francisco","Sydney"],0,"Red",False],
          "Sydney":        [["Jakarta","Manila","Los Angeles"],0,"Red",False],
          "Taipei":        [["Shanghai","Hong Kong","Osaka","Manila"],0,"Red",False],
          "Shanghai":      [["Beijing","Seoul","Tokyo","Taipei","Hong Kong"],0,"Red",False],
          "Beijing":       [["Seoul","Shanghai"],0,"Red",False],
          "Seoul":         [["Beijing","Shanghai","Tokyo"],0,"Red",False],
          "Tokyo":         [["Seoul","Shanghai","Osaka","San Francisco"],0,"Red",False],
          "Osaka":         [["Tokyo","Taipei"],0,"Red",False]
        }

PlayerCards = ["Lagos","Los Angeles","Lima","Miami","Sao Paulo","Johannesburg","Santiago","Buenos Aires","Mexico City","Bogota","Khartoum","Kinshasa",
"Milan","Atlanta","Washington","San Francisco","Madrid","St.Petersburg","Paris","Essen","Montreal","London","Chicago","New York",
"Mumbai","Delhi","Kolkata","Chennai","Tehran","Baghdad","Moscow","Istanbul","Cairo","Algiers","Riyadh","Karachi",
"Osaka","Seoul","Tokyo","Beijing","Shanghai","Jakarta","Manila","Bangkok","Sydney","Taipei","Ho Chi Minh","Hong Kong",
"(Event)One Quiet Night","(Event)Forecast","(Event)Airlift","(Event)Government Grant","(Event)Resilient Population",
"Epidemic","Epidemic","Epidemic","Epidemic","Epidemic","Epidemic"]

PlayerCardsDiscarded = []

player1Hand = []
player2Hand = []
player3Hand = []
player4Hand = []

def drawPCards():
    for i in range(2):
        cardDrawn = PlayerCards[random.randint(0,len(PlayerCards)) - 1]
        player1Hand.append(cardDrawn)
        print(cardDrawn + " has been added to your hand")
        PlayerCards.remove(cardDrawn)
    print(player1Hand)

InfectionCards = ["Lagos","Los Angeles","Lima","Miami","Sao Paulo","Johannesburg","Santiago","Buenos Aires","Mexico City","Bogota","Khartoum","Kinshasa",
"Milan","Atlanta","Washington","San Francisco","Madrid","St.Petersburg","Paris","Essen","Montreal","London","Chicago","New York",
"Mumbai","Delhi","Kolkata","Chennai","Tehran","Baghdad","Moscow","Istanbul","Cairo","Algiers","Riyadh","Karachi",
"Osaka","Seoul","Tokyo","Beijing","Shanghai","Jakarta","Manila","Bangkok","Sydney","Taipei","Ho Chi Minh","Hong Kong"]

InfectionCardsDiscarded = []

def initialInfection():
    addThreeCards = []
    addTwoCards = []
    addOneCards = []
    for i in range(3):
        cardDrawn = InfectionCards[random.randint(0,len(InfectionCards)) - 1]
        addThreeCards.append(cardDrawn)
        InfectionCardsDiscarded.append(cardDrawn)
        graph[cardDrawn][1] = graph[cardDrawn][1] + 3
        InfectionCards.remove(cardDrawn)

        cardDrawn = InfectionCards[random.randint(0,len(InfectionCards)) - 1]
        addTwoCards.append(cardDrawn)
        InfectionCardsDiscarded.append(cardDrawn)
        graph[cardDrawn][1] = graph[cardDrawn][1] + 2
        InfectionCards.remove(cardDrawn)

        cardDrawn = InfectionCards[random.randint(0,len(InfectionCards)) - 1]
        addOneCards.append(cardDrawn)
        InfectionCardsDiscarded.append(cardDrawn)
        graph[cardDrawn][1] = graph[cardDrawn][1] + 1
        InfectionCards.remove(cardDrawn)

    print("Cities with Infection Level 3: " + '||'.join(map(str, addThreeCards)))
    print("Cities with Infection Level 2: " + '||'.join(map(str, addTwoCards)))
    print("Cities with Infection Level 1: " + '||'.join(map(str, addOneCards)))

def ongoingInfection():
    for i in range(2):
        cardDrawn = InfectionCards[random.randint(0,len(InfectionCards)) - 1]
        graph[cardDrawn][1] = graph[cardDrawn][1] + 1
        InfectionCardsDiscarded.append(cardDrawn)
        print(cardDrawn + " has been infected to Level " + str(graph[cardDrawn][1]))
        InfectionCards.remove(cardDrawn)


initialInfection()


while True:
    print("You are currently in " + currentCity + ". Infection Level is " + str(graph[currentCity][1]))
    moveNext = raw_input("You can move to the following Cities: " + ', '.join(map(str, graph[currentCity][0])) + ": ")
    if moveNext in graph[currentCity][0]:
        currentCity = moveNext
    elif moveNext == "break":
        break
    else:
        print("Sorry. That wasn't recognized as one of the options. Try again.")

    drawPCards()
    ongoingInfection()




RoleCards = ["Researcher","Medic","Dispatcher","Quarantine Specialist","Contingency Planner","Operations Expert","Scientist"]
#Implement Way to Draw Cards from the PC and IC lists and add to "Discarded Pile" list for the two piles
#Implement the Players "Hand" and a command to check your hand
#Implement Way to Draw from Role Cards and a way to check your role and your special abilities
#Implement Function To check Actions available according to the cards your on.
#---------------------------------




#Implement Outbreak Counter
#Implement Infection Rate Counter
#Implement Cure/Eradication Status Check
#Implement Dictionary to Replace Lists in order to implement the colors of the card/Description.
#------------------------------------


