# I wrote this program as a demo of the Secretary problem with a modern twist.
# https://en.wikipedia.org/wiki/Secretary_problem

from random import randint, shuffle

class Applicant:

    def __init__(self, name, timeOnMarket):

        self.name = name
        self.price = randint(1,10)
        self.skills = randint(0,10)
        self.interview = randint(0,10)
        self.score = (self.interview * self.skills)
        self.timeOnMarket = randint(1,10)

    def iterate(self):
        self.timeOnMarket = self.timeOnMarket - 1

class Requirement:

    def __init__(self):

        self.honesty = input("Will you post the salary in the job posting? y/n:  ")
        print("10 = +100%")
        print("9  = +75%")
        print("8  = +50%")
        print("7  = +25%")
        print("6  = +10%")
        print("5  = market value")
        print("4  = -10%")
        print("3  = -25%")
        print("2  = -50%")
        print("1  = -75%")
        self.price = int(input("Where does the offered salary compare to market value?:  "))
        self.start = 0

def buildApplicantList():

    applicants = []

    with open('teddyNames.txt','r') as nameList:
        for index,name in enumerate(nameList.readlines()):
            if index == 0:
                pass
            else:
                applicants.append(Applicant(name.strip(), 10))

    shuffle(applicants)
    return applicants

def screenApplicants(applicants, requirements):

    screenedApplicants = []
    outpricedApplicants = []

    for each in applicants:
        if each.price <= requirements.price:
            screenedApplicants.append(each)
        else:
            outpricedApplicants.append(each)

    print("Removed " + str(len(applicants) - len(screenedApplicants)) + " from candidate pool due to price.")

    return (screenedApplicants, outpricedApplicants)

def hire(hire, applicants, outpricedApplicants):
    print("Congratulations! You have hired " + hire.name + " with an employee score of " + str(hire.score) + " out of a possible 100.")
    location = applicants.index(hire)

    priceHire = 0
    earlyHire = 0
    lateHire = 0

    try:
        for each in applicants[location:]:
            if hire.score < each.score:
                earlyHire = earlyHire + 1

        if priceHire > 0:
            print("There were " + str(earlyHire) + " better candidates outside your price range.")
    except Exception as E:
        pass

    for each in applicants[:location]:
        if hire.score < each.score:
            lateHire = lateHire + 1

    for each in outpricedApplicants:
        if hire.score > each.score:
            priceHire = priceHire + 1

    if earlyHire > 0:
        print("There were " + str(earlyHire) + " better candidates, but you hired too early.")

    if lateHire > 0:
        print("There were " + str(lateHire) + " better candidates, but you hired too late.")

def main():

    print("100 people are job hunting, and some will apply for your position.  \nPlease answer the following questions to see if you can hire the best applicant.")
    requirements = Requirement()

    applicants = buildApplicantList()
    outpricedApplicants = []
    candidates = []

    iteration = int(input("How many interviews do you want to do a day?  "))

    if requirements.honesty == "y":
        applicants, outpricedApplicants = screenApplicants(applicants,requirements)

    while True:

        if (len(applicants) - requirements.start) > 0:
            print("You have " + str(len(applicants) - requirements.start) + " applicants left.")
        else:
            break

        for each in applicants[requirements.start:requirements.start + iteration]:
            if each.price <= requirements.price:
                candidates.append(each)
            else:
                print("You interviewed " + each.name + " and were too far apart on expected salary.")

        print("Your top " + str(iteration) + " applicants are: ")
        candidates = sorted(candidates, key=lambda x: x.score, reverse=True)

        for each in candidates[:iteration]:
            print(each.name)


        answer = input("Make an offer to " + candidates[0].name + "?  y/n:  " )
        if answer == "y":
            break

        for index, each in enumerate(candidates):
            each.iterate()
            if each.timeOnMarket <= 0:
                missedOpportunity = candidates.pop(index)
                print(missedOpportunity.name + " has found another position.")

        print("=============================================================")

        requirements.start = requirements.start + iteration

    hire(candidates[0],applicants,outpricedApplicants)

main()