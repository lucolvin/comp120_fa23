import secrets

def setRandom():
    someNum = secrets.SystemRandom().randrange(1,10)
    return someNum



def main():
    Xcoord = []
    Ycoord = []
    
    # Set our locations to random numbers
    num = setRandom()
    Xcoord.append(num)
    num = setRandom()
    Ycoord.append(num)
    print("Ship location: ", Xcoord[0], Ycoord[0])

main()
