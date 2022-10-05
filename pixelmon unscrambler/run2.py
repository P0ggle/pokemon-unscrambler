import time

logpath = input("Filepath: ")

with open('pnames.txt') as biglist:
    pokelist = biglist.read().splitlines()

def readlatest():
    with open(logpath) as x:
        lines = x.read().splitlines()
        return lines[-1]

latest = readlatest()

while True:
    lastline = readlatest()
    if lastline != latest:
        latest = lastline
        print(lastline)
        if "[CHAT] [Chat Games] Unscramble the word: " in str(lastline):
            print("\n#####FOUND#####\n")
            scramble = lastline
            scramblearray = scramble.split()
            scramble = scramblearray[-1]
            print(scramble + "\n")
            for i in pokelist:
                if sorted(scramble) == sorted(i):
                    print("==========")
                    print(i)
                    print("==========")
    time.sleep(0.1)