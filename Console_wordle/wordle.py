import random, os, time

class bcolors:
    ENDC = "\033[0m"
    Bold = "\033[1m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    White        = "\033[97m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundWhite        = "\033[107m"
    BackgroundLightRed     = "\033[101m"

class letter:
    def __init__(self, value, state="fail"):
        self.value = value
        self.state = state

    def __str__(self):
        colour = {"notIn":bcolors.BackgroundLightGray, "positionCorrect":bcolors.BackgroundGreen, "letterPresent":bcolors.BackgroundYellow, "fail":bcolors.BackgroundLightRed}[self.state]
        return bcolors.Bold + colour + f" {self.value} " + bcolors.ENDC

    def displaySelf(self):
        colour = {"notIn":bcolors.BackgroundLightGray, "positionCorrect":bcolors.BackgroundGreen, "letterPresent":bcolors.BackgroundYellow, "fail":bcolors.BackgroundLightRed}[self.state]
        return bcolors.Bold + colour + f" {self.value} " + bcolors.ENDC

def flipDisplay(attempts, its=0):
    os.system("clear")
    for attempt in attempts:
        for attemptLetter in attempt:
            print(attemptLetter, end="")
        print("")

loss = True
print(bcolors.ENDC)
words = eval(open("words.csv", 'r').readline())
word = list(words[random.randint(0, len(words)-1)])
words = []
maxAttemps = 6
attempts = []

while len(attempts) < maxAttemps:
    flipDisplay(attempts)
    for i in range(maxAttemps-len(attempts)):
        print(f"{bcolors.BackgroundDarkGray} □ "*5)
    newGuess = input(bcolors.Bold + bcolors.BackgroundDarkGray).lower()
    while not len(newGuess) == 5:
        print(bcolors.Bold + bcolors.BackgroundLightRed + "MUST BE 5 LETTERS" + bcolors.ENDC)
        newGuess = input(bcolors.Bold + bcolors.BackgroundDarkGray).lower()
    newAttempt = [letter(x) for x in list(newGuess)]
    allCorrect = True
    for i,let in enumerate(newAttempt):
        if let.value == word[i]:
            let.state = "positionCorrect"
        elif let.value in word:
            let.state = "letterPresent"
            allCorrect = False
        else:
            let.state = "notIn"
            allCorrect = False
    attempts.append(newAttempt)
    print(bcolors.ENDC)

    if allCorrect:
        loss = False
        flipDisplay(attempts)
        break

flipDisplay(attempts)
print(f"\n{bcolors.BackgroundLightRed}{''.join([letter(x).displaySelf() for x in list(word)])}" if loss else f"\n{bcolors.BackgroundGreen} GAME WON in {len(attempts)} "+bcolors.ENDC)
