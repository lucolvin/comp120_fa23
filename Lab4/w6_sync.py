import secrets

def setRandom():
    someNum = secrets.SystemRandom().randrange(1,10)
    return someNum

def setShipLocations(Xs, Ys):
    for i in range(3):
        Xs.append(setRandom())
        Ys.append(setRandom())
   
def attackShip(X, Y, Xs, Ys):
    for i in range(3):
        print("X: ", X, "Y: ", Y, "Xs: ", Xs[i], "Ys: ", Ys[i])
        res = 0
        if X == Xs[i] and Y == Ys[i]:
            print("Hit!")
            res = 1
            Xs[i] = -1
            Ys[i] = -1
    return res
    

def main():
    Xcoord = []
    Ycoord = []
    
    setShipLocations(Xcoord, Ycoord)
    
    # Set our locations to random numbers
    
    #num = setRandom()
    #Xcoord.append(num)
    #num = setRandom()
    #Ycoord.append(num)
    print("Ship location: ", Xcoord, Ycoord)
    Xguess = int(input("Enter X Guess: "))
    Yguess = int(input("Enter Y Guess: "))
   
    totalHits = 0
    
    
    
    while totalHits < 3 and Xguess != -1:
        totalHits = totalHits + attackShip(Xguess, Yguess, Xcoord, Ycoord)
        print("Total Hits: ", totalHits)
        Xguess = int(input("Enter X Guess: "))
        Yguess = int(input("Enter Y Guess: "))
        
    print("You sunk my battleship!")
main()
