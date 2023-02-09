from msilib import Table
import random
deckCardsList = ["AceSpades", "TwoSpades", "ThreeSpades", "FourSpades", "FiveSpades", "SixSpades", "SevenSpades", "EightSpades", "NineSpades", "TenSpades", "JackSpades", "QueenSpades", "KingSpades", "AceClubs", "TwoClubs", "ThreeClubs", "FourClubs", "FiveClubs", "SixClubs", "SevenClubs", "EightClubs", "NineClubs", "TenClubs", "JackClubs", "QueenClubs", "KingClubs", "AceDiamonds", "TwoDiamonds", "ThreeDiamonds", "FourDiamonds", "FiveDiamonds", "SixDiamonds", "SevenDiamonds", "EightDiamonds", "NineDiamonds", "TenDiamonds", "JackDiamonds", "QueenDiamonds", "KingDiamonds", "AceHearts", "TwoHearts", "ThreeHearts", "FourHearts", "FiveHearts", "SixHearts", "SevenHearts", "EightHearts", "NineHearts", "TenHearts", "JackHearts", "QueenHearts", "KingHearts"]
shuffledDeck = []
shuffledDeck2 = []
shuffledDeck3 = []
shuffledDeck4= []
shuffledDeck5 = []
shuffledDeck6 = []
shuffledDeck7 = []
shuffledDeck8 = []
shuffledDeck9 = []
shuffledDeck10 = []
shuffledDeck11 = []
shuffledDeck12 = []
shuffledDeck13 = []
shuffledDeck14 = []
shuffledDeck15 = []
shuffledDeck16 = []
shuffledDeck17 = []
shuffledDeck18 = []
shuffledDeck19 = []
shuffledDeck20 = []
lencards = len(deckCardsList)
player1win = False
player2win = False
p1allin = False
p2allin = False
p1fold = False
p2fold = False
TableCards = []
def ShuffleDeck1():
    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = deckCardsList[cardnum]    
        shuffledDeck.append(card)
        deckCardsList.remove(card)
        
    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck[cardnum]    
        shuffledDeck2.append(card)
        shuffledDeck.remove(card)
        
    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck2[cardnum]    
        shuffledDeck3.append(card)
        shuffledDeck2.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck3[cardnum]    
        shuffledDeck4.append(card)
        shuffledDeck3.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck4[cardnum]    
        shuffledDeck5.append(card)
        shuffledDeck4.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck5[cardnum]    
        shuffledDeck6.append(card)
        shuffledDeck5.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck6[cardnum]    
        shuffledDeck7.append(card)
        shuffledDeck6.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck7[cardnum]    
        shuffledDeck8.append(card)
        shuffledDeck7.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck8[cardnum]    
        shuffledDeck9.append(card)
        shuffledDeck8.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck9[cardnum]    
        shuffledDeck10.append(card)
        shuffledDeck9.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck10[cardnum]    
        shuffledDeck11.append(card)
        shuffledDeck10.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck11[cardnum]    
        shuffledDeck12.append(card)
        shuffledDeck11.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck12[cardnum]    
        shuffledDeck13.append(card)
        shuffledDeck12.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck13[cardnum]    
        shuffledDeck14.append(card)
        shuffledDeck13.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck14[cardnum]    
        shuffledDeck15.append(card)
        shuffledDeck14.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck15[cardnum]    
        shuffledDeck16.append(card)
        shuffledDeck15.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck16[cardnum]    
        shuffledDeck17.append(card)
        shuffledDeck16.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck17[cardnum]    
        shuffledDeck18.append(card)
        shuffledDeck17.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck18[cardnum]    
        shuffledDeck19.append(card)
        shuffledDeck18.remove(card)

    for index in range(lencards):
        cardnum = random.randint(0, (lencards) -index -1)
        card = shuffledDeck19[cardnum]    
        shuffledDeck20.append(card)
        shuffledDeck19.remove(card)


p1 = []
p2 = []
p1sorted = []
p2sorted = []
def SortDeck():
    sortlist = ["Ace", "Two", "Thr", "Fou", "Fiv", "Six", "Sev", "Eig", "Nin", "Ten", "Jac", "Que", "Kin"]
    for i in range(len(sortlist)):
        for index in range(5):
            player1card = p1[index]
            if player1card[0:3] == sortlist[i]:
                card = player1card
                p1sorted.append(card)

    #sorting second player
    for i in range(len(sortlist)):
        for index in range(5):
            player2card = p2[index]
            if player2card[0:3] == sortlist[i]:
                card = player2card
                p2sorted.append(card)

def RoyalFlush():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    suitlist = ["e", "t", "d", "b"]
    for index in range(len(suitlist)):
        if p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == suitlist[index]:
            if p1c1[0:3] == "Ace" and p1c2[0:3] == "Ten" and p1c3[0:3] == "Jac" and p1c4[0:3] == "Que" and p1c5[0:3] == "Kin":
                player1win = True
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    for index in range(len(suitlist)):
        if p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == suitlist[index]:
            if p2c1[0:3] == "Ace" and p2c2[0:3] == "Ten" and p2c3[0:3] == "Jac" and p2c4[0:3] == "Que" and p2c5[0:3] == "Kin":
                player2win = True

def StraightFlush():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(9):
        if p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "e" or p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "t" or p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "d" or p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "b":
            if p1c1[0:3] == numlist[-8 + index] and p1c2[0:3] == numlist[-9 + index] and p1c3[0:3] == numlist[-10 + index] and p1c4[0:3] == numlist[-11 + index] and p1c5[0:3] == numlist[-12 + index]:
                player1win = True
        if p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "e" or p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "t" or p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "d" or p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "b":
            if p2c1[0:3] == numlist[-8 + index] and p2c2[0:3] == numlist[-9 + index] and p2c3[0:3] == numlist[-10 + index] and p2c4[0:3] == numlist[-11 + index] and p2c5[0:3] == numlist[-12 + index]:
                player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighCard()

def FourOfAKind():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index] or p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]:
            player1win = True
        if p2c1 == numlist[index] and p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == numlist[index] or p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == numlist[index] and p2c5 == numlist[index]:
            player2win = True
        if player1win == True and player2win == True:
            break

    if player1win == True and player2win == True:
        HighCard()
    
def FullHouse():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == p1c5) or (p1c1 == p1c2 and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            player1win = True
        if (p2c1 == numlist[index] and p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == p2c5) or (p2c1 == p2c2 and p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            player2win = True
        if player1win == True or player2win == True:
            break

    if player1win == True and player2win == True:
        HighCard()

def Flush():
    global player1win, player2win
    samesuitp1 = False
    samesuitp2 = False
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    if (p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "e") or (p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "t") or (p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "d") or (p1c1[-2] == p1c2[-2] == p1c3[-2] == p1c4[-2] == p1c5[-2] == "b"):
        samesuitp1 = True
    if (p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "e") or (p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "t") or (p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "d") or (p2c1[-2] == p2c2[-2] == p2c3[-2] == p2c4[-2] == p2c5[-2] == "b"):
        samesuitp2 = True
    for index in range(len(numlist)):
        if samesuitp1 == True:
            if p1c1[0:3] == numlist[index] or p1c2[0:3] == numlist[index] or p1c3[0:3] == numlist[index] or p1c4[0:3] == numlist[index] or p1c5[0:3] == numlist[index]:
                player1win = True
        if samesuitp2 == True:        
            if p2c1[0:3] == numlist[index] or p2c2[0:3] == numlist[index] or p2c3[0:3] == numlist[index] or p2c4[0:3] == numlist[index] or p2c5[0:3] == numlist[index]:
                player2win = True
        if player1win == True or player2win == True:
            break

    if player1win == True and player2win == True:
        HighCard()

def Straight():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(9):
        if p1c1 == numlist[index - 8] and p1c2 == numlist[index - 9] and p1c3 == numlist[index - 10] and p1c4 == numlist[index - 11] and p1c5 == numlist[index - 12]:
            player1win = True
        if p2c1 == numlist[index - 8] and p2c2 == numlist[index - 9] and p2c3 == numlist[index - 10] and p2c4 == numlist[index - 11] and p2c5 == numlist[index - 12]:
            player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighCard()

def ThreeOfAKind():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and p1c3 == numlist[index]) or (p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == numlist[index]) or (p1c3 == numlist[index] and p1c4 == numlist[index] and p1c5 == numlist[index]):
            player1win = True
        if (p2c1 == numlist[index] and p2c2 == numlist[index] and p2c3 == numlist[index]) or (p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == numlist[index]) or (p2c3 == numlist[index] and p2c4 == numlist[index] and p2c5 == numlist[index]):
            player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighCard()

def TwoPair():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if (p1c1 == numlist[index] and p1c2 == numlist[index] and (p1c3 == p1c4 or p1c4 == p1c5)) or (p1c2 == numlist[index] and p1c3 == numlist[index] and p1c4 == p1c5) or (p1c3 == numlist[index] and p1c4 == numlist[index] and p1c1 == p1c2) or (p1c4 == numlist[index] and p1c5 == numlist[index] and (p1c1 == p1c2 or p1c2 == p1c3)):
            player1win = True
        if (p2c1 == numlist[index] and p2c2 == numlist[index] and (p2c3 == p2c4 or p2c4 == p2c5)) or (p2c2 == numlist[index] and p2c3 == numlist[index] and p2c4 == p2c5) or (p2c3 == numlist[index] and p2c4 == numlist[index] and p2c1 == p2c2) or (p2c4 == numlist[index] and p2c5 == numlist[index] and (p2c1 == p2c2 or p2c2 == p2c3)):
            player2win = True
        if player1win == True or player2win == True:
            break
    if player1win == True and player2win == True:
        HighCard()
    
def Pair():
    global player1win, player2win
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if p1c1 == p1c2 == numlist[index] or p1c2 == p1c3 == numlist[index] or p1c3 == p1c4 == numlist[index] or p1c4 == p1c5 == numlist[index]:
            player1win = True
        if p2c1 == p2c2 == numlist[index] or p2c2 == p2c3 == numlist[index] or p2c3 == p2c4 == numlist[index] or p2c4 == p2c5 == numlist[index]:
            player2win = True
        if player1win == True and player2win == True:
            break
    if player1win == True and player2win == True:
        HighCard()

def HighCard():
    global player1win, player2win
    player1win = False
    player2win = False
    p1c1 = p1sorted[0]
    p1c2 = p1sorted[1]
    p1c3 = p1sorted[2]
    p1c4 = p1sorted[3]
    p1c5 = p1sorted[4]
    p2c1 = p2sorted[0]
    p2c2 = p2sorted[1]
    p2c3 = p2sorted[2]
    p2c4 = p2sorted[3]
    p2c5 = p2sorted[4]
    p1c1 = p1c1[0:3]
    p1c2 = p1c2[0:3]
    p1c3 = p1c3[0:3]
    p1c4 = p1c4[0:3]
    p1c5 = p1c5[0:3]
    p2c1 = p2c1[0:3]
    p2c2 = p2c2[0:3]
    p2c3 = p2c3[0:3]
    p2c4 = p2c4[0:3]
    p2c5 = p2c5[0:3]
    numlist = ["Ace", "Kin", "Que", "Jac", "Ten", "Nin", "Eig", "Sev", "Six", "Fiv", "Fou", "Thr", "Two"]
    for index in range(len(numlist)):
        if p1c1 == numlist[index] or p1c2 == numlist[index] or p1c3 == numlist[index] or p1c4 == numlist[index] or p1c5 == numlist[index]:
            player1win = True
        if p2c1 == numlist[index] or p2c2 == numlist[index] or p2c3 == numlist[index] or p2c4 == numlist[index] or p2c5 == numlist[index]:
            player2win = True
        if player1win == True or player2win == True:
            break

def DecideWinner():
    global p1money, p2money, pot
    if player1win == True and player2win == True:
        print("You split the pot")
        p1money = p1money + pot/2
        p2money = p2money + pot/2
        pot = 0
    elif player1win == True:
        print("Player 1 gets the pot")
        p1money = p1money + pot
        pot = 0
    elif player2win == True:
        print("Player 2 gets the pot")
        p2money = p2money + pot
        pot = 0

def Picking_Winner():

    RoyalFlush()
    if player1win == False and player2win == False:
        StraightFlush()
    if player1win == False and player2win == False:
        FourOfAKind()
    if player1win == False and player2win == False:
        FullHouse()
    if player1win == False and player2win == False:
        Flush()
    if player1win == False and player2win == False:
        Straight()
    if player1win == False and player2win == False:
        ThreeOfAKind()
    if player1win == False and player2win == False:
        TwoPair()
    if player1win == False and player2win == False:
        Pair()
    if player1win == False and player2win == False:
        HighCard()

def Start_Game():
    
    cards = 0
    while cards < 2:
        card = shuffledDeck20[0]
        p1.append(card)
        shuffledDeck20.remove(card)
        card = shuffledDeck20[0]
        p2.append(card)
        shuffledDeck20.remove(card)
        cards = cards + 1
    for index in range(3):
        card = shuffledDeck20[0]
        TableCards.append(card)
        shuffledDeck20.remove(card)


p1money = 1000
p2money = 1000
pot = 0
def TheBetting():
    global p1money, p2money, pot, p1allin, p2allin, p1fold, p2fold, p1, p2, TableCards, shuffledDeck20
    print(p1)
    print(TableCards)
    print("player 1 has", p1money, "chips")
    p1bet = input("How much does player 1 bet?")
    print("-" * 10000)
    print(p2)
    print(TableCards)
    print("player 2 has", p2money, "chips")
    p2bet = input("How much does player 2 bet?")
    print("-" * 10000)
    while True:
        if p1bet.isnumeric() and p2bet.isnumeric():
            p1bet = int(p1bet)
            p2bet = int(p2bet)
            if p1bet == p2bet:
                pot = p1bet + p2bet
                p1money = p1money - p1bet
                p2money = p2money - p2bet
                break
            elif p1bet > p2bet:
                p2bet = input("player 2 must match player 1:")
            elif p2bet < p1bet:
                p1bet = input("player 1 must match player 2:")
        elif (p1bet == "all in" and p2bet == "all in") or (p1bet == "all-in" and p2bet == "all-in"):
            pot = pot + p1money + p2money
            p1money = 0
            p2money = 0
            p1allin = True
            p2allin = True
            break
        elif p1bet == "all in":
            pot = pot + p1money
            p1bet = p1money
            p1money = 0
            p1allin = True
            if p1bet > int(p2bet):
                p2bet = input("player 2 must match player 1's bet or go all in")
            else:
                break
        elif p2bet == "all in":
            pot = pot + p2money
            p2bet = p1money
            p2money = 0
            p2allin = True
            if p2bet > int(p1bet):
                p1bet = input("player 1 must match player 2's bet or go all in")
            else:
                break
        elif p1bet == "fold":
            print("Player 1 chooses to fold. Player 2 wins!")
            p2money = p2money + pot
            p1fold = True
            break
        elif p2bet == "fold":
            print("Player 2 chooses to fold. Player 1 wins!")
            p1money = p1money + pot
            p2fold = True
            break
    if p1fold == False and p2fold == False and p1allin == False and p2allin == False:
        TableCards.append(shuffledDeck20[0])
        shuffledDeck20.remove(shuffledDeck20[0])
        print("The pot is", pot)
        print("These are the new TableCards:", TableCards)
        print("player 1 has", p1money, "chips")
        p1bet2 = input("How much does player 1 bet?")
        print("player 2 has", p2money, "chips")
        p2bet2 = input("How much does player 2 bet?")
        while True:
            if p1bet2.isnumeric() and p2bet2.isnumeric():
                if p1bet2 == p2bet2:
                    p1bet2 = int(p1bet2)
                    p2bet2 = int(p2bet2)
                    pot = pot + p1bet2 + p2bet2
                    p1money = p1money - p1bet2
                    p2money = p2money - p2bet2
                    break
                elif p1bet2 > p2bet2:
                    p2bet2 = input("player 2 must match player 1:")
                elif p2bet2 < p1bet2:
                    p1bet2 = input("player 1 must match player 2:")
            elif (p1bet2 == "all in" and p2bet2 == "all in") or (p1bet2 == "all-in" and p2bet2 == "all-in"):
                pot = pot + p1money + p2money
                p1money = 0
                p2money = 0
                p1allin = True
                p2allin = True
                break
            elif p1bet2 == "all in":
                pot = pot + p1money
                p1bet2 = p1money
                p1money = 0
                p1allin = True
                if p1bet2 > int(p2bet2):
                    p2bet2 = input("player 2 must match player 1's bet or go all in")
                else:
                    break
            elif p2bet2 == "all in":
                pot = pot + p2money
                p2bet2 = p1money
                p2money = 0
                p2allin = True
                if p2bet2 > int(p1bet2):
                    p1bet2 = input("player 1 must match player 2's bet or go all in")
                else:
                    break
            elif p1bet2 == "fold":
                print("Player 1 chooses to fold. Player 2 wins!")
                p2money = p2money + pot
                p1fold = True
                break
            elif p2bet2 == "fold":
                print("Player 2 chooses to fold. Player 1 wins!")
                p1money = p1money + pot
                p2fold = True
                break
    
    if p1fold == False and p2fold == False and p1allin == False and p2allin == False:
        print("The pot is", pot)
        TableCards.append(shuffledDeck20[0])
        print("These are the final Table Cards:", TableCards)
        print("player 1 has", p1money, "chips")
        p1bet3 = input("How much does player 1 bet?")
        print("player 2 has", p2money, "chips")
        p2bet3 = input("How much does player 2 bet?")
        while True:
            if p1bet3.isnumeric() and p2bet3.isnumeric():
                if p1bet3 == p2bet3:
                    p1bet3 = int(p1bet)
                    p2bet3 = int(p2bet)
                    pot = pot + p1bet3 + p2bet3
                    p1money = p1money - p1bet3
                    p2money = p2money - p2bet3
                    break
                elif p1bet3 > p2bet3:
                    p2bet3 = input("player 2 must match player 1:")
                elif p2bet3 < p1bet3:
                    p1bet3 = input("player 1 must match player 2:")
            elif (p1bet3 == "all in" and p2bet3 == "all in") or (p1bet3 == "all-in" and p2bet3 == "all-in"):
                pot = pot + p1money + p2money
                p1money = 0
                p2money = 0
                p1allin = True
                p2allin = True
                break
            elif p1bet3 == "all in":
                pot = pot + p1money
                p1bet3 = p1money
                p1money = 0
                p1allin = True
                if p1bet3 > int(p2bet3):
                    p2bet3 = input("player 2 must match player 1's bet or go all in")
                else:
                    break
            elif p2bet3 == "all in":
                pot = pot + p2money
                p2bet3 = p1money
                p2money = 0
                p2allin = True
                if p2bet3 > int(p1bet3):
                    p1bet3 = input("player 1 must match player 2's bet or go all in")
                else:
                    break
            elif p1bet3 == "fold":
                print("Player 1 chooses to fold. Player 2 wins!")
                p2money = p2money + pot
                p1fold = True
                break
            elif p2bet3 == "fold":
                print("Player 2 chooses to fold. Player 1 wins!")
                p1money = p1money + pot
                p2fold = True
                break
    if p1fold == False and p2fold == False and p1allin == False and p2allin == False:
        print("When picking your table cards to make your final hand, there can be no repeats in each player's hand, but both players can pick the same card to add to their hand")
        while True:
            p1t = int(input("player 1, pick one table card(number)"))
            p1t2 = int(input("player 1, pick another table card(number)"))
            p1t3 = int(input("player 1, pick your final card(number)"))
            if p1t != p1t2 and p1t != p1t3 and p1t2 != p1t3:
                break
        while True:
            p2t = int(input("player 2, pick one table card(number)"))
            p2t2 = int(input("player 2, pick another table card(number)"))
            p2t3 = int(input("player 2, pick your final card(number)"))
            if p2t != p2t2 and p2t != p2t3 and p2t2 != p2t3:
                break
        p1.append(TableCards[p1t - 1])
        p1.append(TableCards[p1t2 - 1])
        p1.append(TableCards[p1t3 - 1])
        p2.append(TableCards[p2t - 1])
        p2.append(TableCards[p2t2 - 1])
        p2.append(TableCards[p2t3 - 1])
    if p1allin == True or p2allin == True:
        tablelength = len(TableCards)
        while tablelength < 5:
            card = shuffledDeck20
            TableCards.append(card)
            shuffledDeck20.remove(card)
            tablelength = len(TableCards)
        print("The table cards are", TableCards)
        print("When picking your table cards to make your final hand, there can be no repeats in each player's hand, but both players can pick the same card to add to their hand")
        while True:
            p1t = int(input("player 1, pick one table card(number)"))
            p1t2 = int(input("player 1, pick another table card(number)"))
            p1t3 = int(input("player 1, pick your final card(number)"))
            if p1t != p1t2 and p1t != p1t3 and p1t2 != p1t3:
                break
        while True:
            p2t = int(input("player 2, pick one table card(number)"))
            p2t2 = int(input("player 2, pick another table card(number)"))
            p2t3 = int(input("player 2, pick your final card(number)"))
            if p2t != p2t2 and p2t != p2t3 and p2t2 != p2t3:
                break
        p1.append(TableCards[p1t - 1])
        p1.append(TableCards[p1t2 - 1])
        p1.append(TableCards[p1t3 - 1])
        p2.append(TableCards[p2t - 1])
        p2.append(TableCards[p2t2 - 1])
        p2.append(TableCards[p2t3 - 1])

while True:
    
    ShuffleDeck1()
    Start_Game()
    TheBetting()
    if p1fold == False and p2fold == False:
        SortDeck()
        Picking_Winner()
        DecideWinner()
    p1_again = input("Would player 1 like to play again?")
    p2_again = input("Would player 2 like to play again?")
    if p1_again == "yes" and p2_again == "yes":
        pot = 0
        p1 = []
        p2 = []
        p1sorted = []
        p2sorted = []
        deckCardsList = ["AceSpades", "TwoSpades", "ThreeSpades", "FourSpades", "FiveSpades", "SixSpades", "SevenSpades", "EightSpades", "NineSpades", "TenSpades", "JackSpades", "QueenSpades", "KingSpades", "AceClubs", "TwoClubs", "ThreeClubs", "FourClubs", "FiveClubs", "SixClubs", "SevenClubs", "EightClubs", "NineClubs", "TenClubs", "JackClubs", "QueenClubs", "KingClubs", "AceDiamonds", "TwoDiamonds", "ThreeDiamonds", "FourDiamonds", "FiveDiamonds", "SixDiamonds", "SevenDiamonds", "EightDiamonds", "NineDiamonds", "TenDiamonds", "JackDiamonds", "QueenDiamonds", "KingDiamonds", "AceHearts", "TwoHearts", "ThreeHearts", "FourHearts", "FiveHearts", "SixHearts", "SevenHearts", "EightHearts", "NineHearts", "TenHearts", "JackHearts", "QueenHearts", "KingHearts"]
        shuffledDeck = []
        shuffledDeck2 = []
        shuffledDeck3 = []
        lencards = len(deckCardsList)
        player1win = False
        player2win = False
        TableCards = []
        
    else:
        break
    
    


'''
gives each player 2 cards
puts three on table
has to match
check means no raise
if someone raises, they everyone has to match the raise
bet each time cards are laid on the table(3 times)
if all in, player can stay in
'''