ans = []
list1 = []
time = [5, 4, 10]
cost = [1500, 1000, 3000]
unit = 7
def findMax(ind, currentTime, profit, l):
    if ind == len(time):
        if currentTime == 0:
            curProfit = 0
            if currentTime != 0:
                rem = unit - currentTime
                
                for i in range(rem):
                    k = 0
                    for j in l:
                        curProfit += j*cost[k]
                        k += 1
            ans.append(curProfit + profit)
        return
    
    if currentTime - time[0] >= 0 or currentTime - time[1] >= 0 or currentTime - time[2] >= 0:
        l.append(ind)
        findMax(ind, currentTime - time[ind], profit+cost[ind], l)
        l.pop()
    findMax(ind+1, currentTime, profit, l)

findMax(0, 7, 0, list1) 
print(ans)



