# First of all we should import math module to start working with digits.
import math

# Here we declare functions.
# Calculation of QAs will be performed by this function.
def calculateQAAmount(currentTeamSize):
    return round(currentTeamSize / 3)

# Calculation of devs will be performed by this function.
def calculateDevAmount(teamSize, pmAmount, qaAmount):
    return teamSize - pmAmount - qaAmount

# Calculation of PMs will be performed by this function.
def calculatePMAmount(teamSize):
    return round(teamSize / 10)

# Calculation of RMs/BAs will be performed by this function.
def calculateRMAmount(teamSize):
    rmCriteriaNumber = 20

    if (teamSize <= rmCriteriaNumber):
        return 1
    else:
        return math.ceil(teamSize / rmCriteriaNumber)

# Calculation of designers will be performed by this function.
def calculateDesignerAmount(teamSize):
    desCriteriaNumber = 18

    # Ternary operator is used.
    return 1 if teamSize <= desCriteriaNumber else math.ceil(teamSize / desCriteriaNumber)

# Main code block
# Welcoming a user
print("I welcome you at ProjectGeek calculator, my Master!\nI can set up your team!\n")

setUpATeam = True
while setUpATeam:
    # Requesting a user to enter a team size.
    incomingValue = input("Please, enter total number of your team size: ")

# Application of try...catch structure to catch errors if any and respond to user behavior.    
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
        # Asking a user if he/she needs also a designer.
        designerQuestion = input("Do you also need a designer? (Y/N): ")
        print("Input: ", designerQuestion)
        # Lower string method returns a copy of the string in which all case-based characters have been lowercased.
        if designerQuestion.lower() in ('y', 'yes'):
            designerAmount = calculateDesignerAmount(teamSize)
        elif designerQuestion.lower() != 'n':
            print("I\'ve accepted your answer like NO, so let\'s set up without a designer\n")
    # Values of team members.
    pmAmount = calculatePMAmount(teamSize)
    qaAmount = calculateQAAmount(teamSize - pmAmount - rmAmount - designerAmount)
    devAmount = calculateDevAmount(teamSize - designerAmount - rmAmount, pmAmount, qaAmount)

    # Returning calculated result to a user.
    print("Your team may consist of:")
    print("    PMs needed: ", pmAmount)
    print("    Developers needed: ", devAmount)
    print("    QAs needed: ", qaAmount)

    if (rmAmount >= 1):
        print("    RMs/BAs needed: ", rmAmount)

    if (designerAmount >= 1):
        print("    Designers needed: ", designerAmount)

    # Proposing user to try again.        
    setUpAgain = input("Do you wanna try again? (Y/N): ")
    if not setUpAgain.lower() in ('y', 'yes'):
        setUpATeam = False
        # Bye-bye message when finished.
        print("It was fun! Come back later. I\'m always ready to help! Bye-bye!")