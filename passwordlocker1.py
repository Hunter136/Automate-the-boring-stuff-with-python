#!
#this is a password manager program
def makeDicti(lyst, lyste):
    dicti = dict(zip(lyste, lyst))
    return dicti

def printdicti(lysten):
    for k, v in lysten.items():
        print('Password: '+ str(k) + ' Password #: '+ v)

def prinlist(lyst, lyste):
    print(lyst, lyste)

def createPasswordlist(lyst, word):
    wo = 0
    while wo < word:
        print("post your password")
        name = input()
        lyst.append(name)
        wo = wo + 1
    return lyst

def createNumberlist(lyst, lyste):
    for i in range(len(lyst)):
        lyste.append(i)
    return lyste
def getlist(lyst, number):
        print(lyst[number])

def main():
    lyst = []
    lyste = []
    lysten = {}
    print("input passwords into this doc, type the number of passwords you want to add")
    word = int(input())
    lyst = createPasswordlist(lyst,word)
    lyste = createNumberlist(lyst,lyste)
    #prinlist(lyst, lyste)
    lysten = makeDicti(lyst, lyste)
    printdicti(lysten)
    print('What password number are you looking to see')
    number = int(input())
    getlist(lyst, number)

main()