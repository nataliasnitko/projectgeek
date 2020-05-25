import math

# Functions declaration
def calculateQAAmount(currentTeamSize):
    return round(currentTeamSize / 3)

def calculateDevAmount(teamSize, pmAmount, qaAmount):
    return teamSize - pmAmount - qaAmount

def calculatePMAmount(teamSize):
    return round(teamSize / 10)

def calculateRMAmount(teamSize):
    rmCriteriaNumber = 20

    # Ternary operator in Python
    return 1 if teamSize <= rmCriteriaNumber else math.ceil(teamSize / rmCriteriaNumber)

def calculateDesignerAmount(teamSize):
    desCriteriaNumber = 18

    return 1 if teamSize <= desCriteriaNumber else math.ceil(teamSize / desCriteriaNumber)

# Main code block
print("I welcome you at ProjectGeek calculator, my Master!\nI can set up your team!\n")

setUpATeam = True
while setUpATeam:
    incomingValue = input("Please, enter total number of your team size: ")
    
    try:
        teamSize = int(incomingValue)
    except:
        print("Your team size must be a number. Please, try again\n", )
        continue

    rmAmount = designerAmount = 0

    if (teamSize < 1):
        print("Please, enter a positive number\n")
        continue
    elif (teamSize >= 8):
        if teamSize > 100:
            print("WOW! You wanna build a big company!")
            
        rmAmount = calculateRMAmount(teamSize)

        designerQuestion = input("Do you also need a designer? (Y/N): ")
        print("Input: ", designerQuestion)
        if designerQuestion.lower() in ('y', 'yes'):
            designerAmount = calculateDesignerAmount(teamSize)
        elif designerQuestion.lower() != 'n':
            print("I\'ve accepted your answer like NO, so let\'s set up without a designer\n")

    pmAmount = calculatePMAmount(teamSize)
    qaAmount = calculateQAAmount(teamSize - pmAmount - rmAmount - designerAmount)
    devAmount = calculateDevAmount(teamSize - designerAmount - rmAmount, pmAmount, qaAmount)

    print("Your team may consist of:")
    print("    PMs needed: ", pmAmount)
    print("    Developers needed: ", devAmount)
    print("    QAs needed: ", qaAmount)

    if (rmAmount >= 1):
        print("    RMs/BAs needed: ", rmAmount)

    if (designerAmount >= 1):
        print("    Designers needed: ", designerAmount)

    setUpAgain = input("Do you wanna try again? (Y/N): ")
    if not setUpAgain.lower() in ('y', 'yes'):
        setUpATeam = False
        print("It was fun! Come back later. I\'m always ready to help! Bye-bye!")