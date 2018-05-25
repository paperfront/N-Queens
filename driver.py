from Queen import Queen
import math
import timeit

# def testQueens(n, i):
    
######################################
# Deprecated Original Testing Method #
######################################

##################################################################################################################
      
    
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
        


##################################################################################################################  




#############################################################
# Returns a list of spaces that are blocked for a given row #
#############################################################



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


def heuristic1(actualResults, i, n, qlist):
    
#############################################
# Maximum Distance Between Consecutive Rows #
#############################################
    
#    print("Actual Results: ")
#    print(actualResults)

    if(len(actualResults) >= 2):
        if(abs(actualResults[0] - qlist[i - 1].x) < abs(actualResults[-1] - qlist[i-1].x)):
            actualResults.reverse()
    return actualResults


def heuristic2(results, row, n, qlist):

#############################################################################
# Scan All Future Rows and Return Option With Least Amount of Cells Blocked #
#############################################################################

    
#    print("Actual Results: ")
#    print(results)
    
    scores = []
    finalscores = []
    for r in results:
        scores.append(0)
        qlist.append(Queen(r, row))
        for i in range(row, n):
            tempresults = checkRow(qlist, i, n)
            scores[results.index(r)] += len(tempresults)
            tempresults.clear()
        qlist.pop()
    counter = len(scores)
#    print("Results:")
#    print(results)
    for j in range(counter):
        maxval = 0
        for i in scores:
            if(i > maxval):
                maxval = i
        currentindex = scores.index(maxval)
        finalscores.insert(0, results[currentindex])
        scores.pop(currentindex)
        results.pop(currentindex)
    return finalscores   



def heuristic3(results, row, n, qlist):

################################################
# Scan Next Row and Return Least Cells Blocked #
################################################
    scores = []
    finalscores = []
    for r in results:
        scores.append(0)
        qlist.append(Queen(r, row))
        tempresults = checkRow(qlist, row, n)
        scores[results.index(r)] += len(tempresults)
        tempresults.clear()
        qlist.pop()
    counter = len(scores)
#    print("Results:")
#    print(results)
    for j in range(counter):
        maxval = 0
        for i in scores:
            if(i > maxval):
                maxval = i
        currentindex = scores.index(maxval)
        finalscores.insert(0, results[currentindex])
        scores.pop(currentindex)
        results.pop(currentindex)
    return finalscores


        

def testingAlgorithm(n, cranks, crow, qlist):
    
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

    
#    print("Now testing x = " + str(cranks[0]))


    nextranks = checkRow(qlist, crow + 1, n)

#    inranks = heuristic1(nextranks, crow + 1, n, qlist)
#    inranks = heuristic2(nextranks, crow + 1, n, qlist)
    inranks = heuristic3(nextranks, crow + 1, n, qlist)
    
    if(testingAlgorithm(n, inranks, crow + 1, qlist) == True):
        return True
    else:  
        cranks.pop(0)
        return testingAlgorithm(n, cranks, crow, qlist)
  
   

   
    
    




n = int(input("Enter a number: "))

# n = 4

timeslist = []



start = timeit.default_timer()

queenList = []
for x in range(math.ceil(n/2)):
    i = 1
    print("Testing for starting queen at (" + str(x) + ", 0)")
    queenList.append(Queen(x, 0))
    startranks = checkRow(queenList, i, n)

#   inranks = heuristic1(startranks, i, n, queenList)
#   inranks = heuristic2(startranks, i, n, queenList)
    inranks = heuristic3(startranks, i, n, queenList)

    
    if(testingAlgorithm(n, inranks, 1, queenList) != True):
        print("No Working Config Found")
   # runtime(n, i)
    queenList.clear()
    print("")
    print("")
    print("")
    print("")

stop = timeit.default_timer()
print(stop - start)
timeslist.append(stop - start)
quitprog = input("Type in a value and hit enter to close program ")



