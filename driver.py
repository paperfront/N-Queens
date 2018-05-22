from Queen import Queen
import math

# def runtime(n, i):
    
    
    
  #  currentResults = checkRow(queenList, i, n)
    
  #  rankedResults = []
  #  
  #  rankedResults = heuristic1(currentResults, i, n)
    
    
    
    
 #   for a in rankedResults:
 #       queenList.append(Queen(a, i))
  #      print("Now testing x = " + str(a))
  #      if(len(queenList) == n):
 #           print("Working Configuration of Queens Found When Starting Position = " + queenList[0].printQueen() + "! Sequence: ")
  #          for a in queenList:
  #              print(a.printQueen())
  #          print("")
  #          return True
  #      
  #      
  #      if(runtime(n, i + 1) == True):
  #          return True
 #       print("popped " +  str(queenList[-1].x) + "!")
  #      queenList.pop()     
  #      
#
  #      
  #  if(len(queenList) == 1):
  #      print("No Working Configuration of Queens Found When Starting Position = " + queenList[0].printQueen())
   #     return False
        

def checkRow(queens, row, n):
    results = []
    newqueens = queens
    for a in newqueens:
        results.append((a.x, row))
    for b in newqueens:
        if(b.x + (row - b.y) <= n - 1):
            if((row - b.y + b.x, row) not in results):
                results.append((row - b.y + b.x, row))
    newqueens.reverse()
    for b in newqueens:
        if(b.x - (row - b.y) >= 0):
            if((b.x - (row - b.y), row) not in results):
                results.append((b.x - (row - b.y), row))
    newqueens.reverse()
    
    actualresults = []
    
    for g in range(n):
        if((g, row) not in results):
            actualresults.append(g)
    
    return actualresults          


def heuristic1(actualResults, i, n):
    print("Actual Results: ")
    print(actualResults)

    if(len(actualResults) >= 2):
        if(abs(actualResults[0] - queenList[i - 1].x) < abs(actualResults[-1] - queenList[i-1].x)):
            actualResults.reverse()
    return actualResults



def newMethod(n, cranks, crow, qlist):
    
    if(len(qlist) == n):
        print("Working Configuration of Queens Found When Starting Position = " + queenList[0].printQueen() + "! Sequence: ")
        for a in queenList:
            print(a.printQueen())
        print("")
        return True
    if(len(cranks) == 0):
        qlist.pop()
        return False
    qlist.append(Queen(cranks[0], crow))
    print("Now testing x = " + str(cranks[0]))
    nextranks = checkRow(qlist, crow + 1, n)
    if(newMethod(n, heuristic1(nextranks, crow + 1, n), crow + 1, qlist) == True):
        return True
    else:  
        cranks.pop(0)
        newMethod(n, cranks, crow, qlist)
        
    if(len(qlist) == n):
        return True
   

   
    
    




n = int(input("Enter a number: "))
queenList = []
for x in range(math.ceil(n/2)):
    i = 1
    print("Testing for starting queen at (" + str(x) + ", 0)")
    queenList.append(Queen(x, 0))
    startranks = checkRow(queenList, i, n)
    if(newMethod(n, heuristic1(startranks, i, n), 1, queenList) != True):
        print("No Working Config Found")
   # runtime(n, i)
    queenList.clear()
    print("")
    print("")
    print("")
    print("")


