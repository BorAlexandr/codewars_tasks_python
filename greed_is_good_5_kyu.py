#Greed is Good task
#Description
#Greed is a dice game played with five six-sided dice.You will always be given an array with five six-sided dice values.
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point

#A single die can only be counted once in each roll.
#For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.


d = {(1, 1, 1): 1000,
     (6, 6, 6): 600,
     (5, 5, 5): 500,
     (4, 4, 4): 400,
     (3, 3, 3): 300,
     (2, 2, 2): 200,
     (1,): 100,
     (5,): 50
     }

lst = [5, 1, 3, 4, 1]

def score(lst):
    num = [min(lst)]
    score = 0
    for i in sorted(lst)[1:]:
        if i in num and len(num) < 3:
            num.append(i)
        else:
            if tuple(num) in d:
                score += d[tuple(num)]
                num.clear()
                num = [i]
            else:
                if num == [1, 1]:
                    score += 200
                    num.clear()
                    num = [i]
                elif num == [5, 5]:
                    score += 100
                    num.clear()
                    num = [i]
                else:
                    num.clear()
                    num = [i]
    if tuple(num) in d:
        score += d[tuple(num)]
    elif num == [1, 1]:
        score += 200
    elif num == [5, 5]:
        score += 100


    return score

print(score(lst))

