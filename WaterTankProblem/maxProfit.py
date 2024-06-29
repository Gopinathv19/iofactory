candidates = [2, 3, 4, 7]
target = 7
list1 = []
ans = []

def findCombination(i, l, sum):
    if i == len(candidates):
        if sum == 0:
            ans.append(l.copy())
        return
    if sum >= candidates[i]:
        l.append(candidates[i])
        findCombination(i, l, sum - candidates[i])
        l.pop()
    findCombination(i + 1, l, sum)

findCombination(0, list1, target)
print(ans)
