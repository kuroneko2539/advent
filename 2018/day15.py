import argparse, numpy as np, re, sys, os

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", type=str, default="./day15Input.txt", help="file containing input key")
args = parser.parse_args()

class Player:
    elfCount = 0
    goblinCount = 0
    elfHP = 0
    goblinHP = 0
    field = None
    IDCount = 0
    turn = 0

    def __init__(self, species, location, HP=200, atk=3):
        self.HP = HP
        self.type = species
        self.location = location
        self.ID = Player.IDCount
        self.atk = atk
        Player.IDCount += 1
        if species == "E": Player.elfCount += 1
        elif species == "G": Player.goblinCount += 1

    @staticmethod
    def getTurnOrder():
        turnOrder = []
        for i in range(Player.field.shape[0]):
            for j in range(Player.field.shape[1]):
                if isinstance(Player.field[i,j], Player):
                    turnOrder.append(Player.field[i,j])
        return turnOrder
    
    @staticmethod
    def getHP():
        sumHP = 0
        for i in range(Player.field.shape[0]):
            for j in range(Player.field.shape[1]):
                if isinstance(Player.field[i,j], Player):
                    if Player.field[i,j].HP > 0:
                        sumHP += Player.field[i,j].HP
        return sumHP
    
    def calculateMove(self, target):
        tempField = Player.field.copy()
        whereToCheck = [self.location]
        value = 0
        targetFound = False
        while not targetFound:
            value += 1
            nextCheck = []
            for check in whereToCheck:
                if tempField[check[0]-1,check[1]] == None:
                    tempField[check[0]-1,check[1]] = value
                    nextCheck.append([check[0]-1,check[1]])
                elif isinstance(tempField[check[0]-1,check[1]], Player):
                    if tempField[check[0]-1,check[1]].type == target:
                        targetLocation = [check[0],check[1]]
                        targetFound = True
                        break
                if tempField[check[0],check[1]-1] == None:
                    tempField[check[0],check[1]-1] = value
                    nextCheck.append([check[0],check[1]-1])
                elif isinstance(tempField[check[0],check[1]-1], Player):
                    if tempField[check[0],check[1]-1].type == target:
                        targetLocation = [check[0],check[1]]
                        targetFound = True
                        break
                if tempField[check[0],check[1]+1] == None:
                    tempField[check[0],check[1]+1] = value
                    nextCheck.append([check[0],check[1]+1])
                elif isinstance(tempField[check[0],check[1]+1], Player):
                    if tempField[check[0],check[1]+1].type == target:
                        targetLocation = [check[0],check[1]]
                        targetFound = True
                        break
                if tempField[check[0]+1,check[1]] == None:
                    tempField[check[0]+1,check[1]] = value
                    nextCheck.append([check[0]+1,check[1]])
                elif isinstance(tempField[check[0]+1,check[1]], Player):
                    if tempField[check[0]+1,check[1]].type == target:
                        targetLocation = [check[0],check[1]]
                        targetFound = True
                        break
            whereToCheck = nextCheck.copy()
            if len(whereToCheck) == 0 and not targetFound: return
        
        while tempField[targetLocation[0],targetLocation[1]] != 1:
            if not isinstance(tempField[targetLocation[0]-1,targetLocation[1]], Player):
                if tempField[targetLocation[0],targetLocation[1]] - 1 == tempField[targetLocation[0]-1,targetLocation[1]]:
                    targetLocation = [targetLocation[0]-1,targetLocation[1]]
                    continue
            if not isinstance(tempField[targetLocation[0],targetLocation[1]-1], Player):
                if tempField[targetLocation[0],targetLocation[1]] - 1 == tempField[targetLocation[0],targetLocation[1]-1]:
                    targetLocation = [targetLocation[0],targetLocation[1]-1]
                    continue
            if not isinstance(tempField[targetLocation[0],targetLocation[1]+1], Player):
                if tempField[targetLocation[0],targetLocation[1]] - 1 == tempField[targetLocation[0],targetLocation[1]+1]:
                    targetLocation = [targetLocation[0],targetLocation[1]+1]
                    continue
            if not isinstance(tempField[targetLocation[0]+1,targetLocation[1]], Player):
                if tempField[targetLocation[0],targetLocation[1]] - 1 == tempField[targetLocation[0]+1,targetLocation[1]]:
                    targetLocation = [targetLocation[0]+1,targetLocation[1]]
                    continue
        Player.field[self.location[0],self.location[1]] = None
        self.location = targetLocation
        Player.field[self.location[0],self.location[1]] = self

    def checkAdjacents(self, target):
        possibleTargets = []
        if isinstance(Player.field[self.location[0]-1,self.location[1]], Player):
            if Player.field[self.location[0]-1,self.location[1]].type == target:
                possibleTargets.append(Player.field[self.location[0]-1,self.location[1]])
        if isinstance(Player.field[self.location[0],self.location[1]-1], Player):
            if Player.field[self.location[0],self.location[1]-1].type == target:
                possibleTargets.append(Player.field[self.location[0],self.location[1]-1])
        if isinstance(Player.field[self.location[0],self.location[1]+1], Player):
            if Player.field[self.location[0],self.location[1]+1].type == target:
                possibleTargets.append(Player.field[self.location[0],self.location[1]+1])
        if isinstance(Player.field[self.location[0]+1,self.location[1]], Player):
            if Player.field[self.location[0]+1,self.location[1]].type == target:
                possibleTargets.append(Player.field[self.location[0]+1,self.location[1]])

        if len(possibleTargets) > 0:
            possibleTargets = sorted(possibleTargets, key=lambda x: x.HP)
            return possibleTargets[0]
        else: return None

    def attack(self, target):
        target.HP -= self.atk
        if target.HP < 1:
            Player.field[target.location[0],target.location[1]] = None
            if target.type == "G": Player.goblinCount -= 1
            if target.type == "E": Player.elfCount -= 1

    def drawStatus(self):
        drawField = Player.field.copy()[self.location[0]-3:self.location[0]+4,self.location[1]-3:self.location[1]+4]
        for i in range(drawField.shape[0]):
            for j in range(drawField.shape[1]):
                if isinstance(drawField[i,j], Player):
                    drawField[i,j] = drawField[i,j].type
                elif not drawField[i,j]: drawField[i,j] = "."
                else: drawField[i,j] = str(drawField[i,j])
        print(drawField)
    
    @staticmethod
    def drawFull(inField):
        os.system('cls')
        drawField = inField.copy()
        for i in range(drawField.shape[0]):
            for j in range(drawField.shape[1]):
                if isinstance(drawField[i,j], Player):
                    sys.stdout.write(drawField[i,j].type)
                elif not drawField[i,j]: sys.stdout.write(".")
                else: sys.stdout.write(str(drawField[i,j]))
            sys.stdout.write("\n")
        sys.stdout.write("\n")
        sys.stdout.flush()

    def executeTurn(self):
        #Player.drawFull()
        if self.HP < 1: return
        if self.type == "E": 
            target = "G"
        elif self.type == "G": 
            target = "E"
        enemy = self.checkAdjacents(target)
        if enemy:
            #print(self.type + str(self.ID) + " attacks " + enemy.type + str(enemy.ID))
            self.attack(enemy)
        else:
            #print(self.type + str(self.ID) + " moves")
            self.calculateMove(target)
            enemy = self.checkAdjacents(target)
            if enemy:
                self.attack(enemy)

elfAttack = 17

with open(args.inFile, "r") as f:
    rows = [x.strip() for x in f.readlines()]

Player.field = np.full((len(rows), len(rows[0])), None)

for row in range(len(rows)):
    for col in range(len(rows[row])):
        if rows[row][col] == "E":
            Player.field[row,col] = Player("E", [row,col], atk=elfAttack)
        elif rows[row][col] == "G":
            Player.field[row,col] = Player("G", [row,col])
        elif rows[row][col] == "#":
            Player.field[row][col] = "#"

print(Player.elfCount, Player.goblinCount)
while Player.elfCount > 0 and Player.goblinCount > 0:
    turnOrder = [x for x in Player.getTurnOrder()]
    Player.turn += 1
    for turn in turnOrder:
        turn.executeTurn()
        if Player.elfCount == 0:
            print("Goblins ({}) win with {}HP in {} turns giving score: {}".format(Player.goblinCount,Player.getHP(), Player.turn-1, Player.getHP()*(Player.turn-1)))
            break
        elif Player.goblinCount == 0:
            print("Elves ({}) win with {}HP in {} turns giving score: {}".format(Player.elfCount,Player.getHP(), Player.turn-1, Player.getHP()*(Player.turn-1)))
            break
    #Player.drawFull(Player.field)