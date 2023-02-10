import random

import Range as Range


def FirstPhase():

    MaxTries = 10000000
    totalTries = 0
    failedTries = 0

    decisionChangeProvideWin = 0
    decisionChangingProvideLose = 0

    dontChangeProvideLose = 0
    dontChangeProvideWin = 0

    i = 0
    while i < MaxTries:
        carDoorIndex = random.randint(0, 2)  #Car
        selectedDoor = random.randint(0, 2)  #Challanger
        openedDoor = random.randint(0, 2)    #Host


        while selectedDoor == openedDoor:
            openedDoor = random.randint(0, 2)
            if openedDoor != selectedDoor:
                break

        # ---------------If Host Selects Goat On Purpose-------------------------------
        while openedDoor == carDoorIndex:
            openedDoor = random.randint(0, 2)
            if openedDoor != carDoorIndex:
                break
        # _____________________________________________________________________________

        if openedDoor == carDoorIndex:
            failedTries += 1
            totalTries += 1
            print(str(totalTries) + ". Iteration failed")
            i += 1
            continue
        else:
            decision = random.randint(0, 1)
            if decision == 0:
                if carDoorIndex == selectedDoor:
                    dontChangeProvideWin += 1
                    totalTries += 1
                    print(str(totalTries) + ". Iteration Success | " + "Stability Win: " + str(dontChangeProvideWin))
                else:
                    dontChangeProvideLose += 1
                    totalTries += 1
                    print(str(totalTries) + ". Iteration Success | " + "Stability Lose: " + str(dontChangeProvideLose))
            else:
                if carDoorIndex != selectedDoor:
                    decisionChangeProvideWin += 1
                    totalTries += 1
                    print(str(totalTries) + ". Iteration Success | " + "Changing Win: " + str(decisionChangeProvideWin))
                else:
                    decisionChangingProvideLose += 1
                    totalTries += 1
                    print(str(totalTries) + ". Iteration Success | " + "Changing Lose: " + str(decisionChangingProvideLose))
            i += 1
            continue

    else:
        print()
        print("Iterations Complated! Here is the results:")
        print("______________________________________________")
        print("Iteration Count: " + str(totalTries))
        print("Successful Tries: " + str(totalTries - failedTries))
        print("Failed Tries: " + str(failedTries))
        print()
        print("Stability Win: " + str(decisionChangeProvideWin))
        print("Stability Lose: " + str(dontChangeProvideLose))
        print()
        print("Changing Win: " + str(decisionChangeProvideWin))
        print("Changing Lose: " + str(decisionChangingProvideLose))

        print("ChanginWin / StabilityWin: " + str(decisionChangeProvideWin / dontChangeProvideWin))
        print("ChanginLose / StabilityLose: " + str(decisionChangingProvideLose / dontChangeProvideLose))
        print("______________________________________________")


if __name__ == "__main__":
    FirstPhase()


