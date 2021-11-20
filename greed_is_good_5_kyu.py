#Greed is Good 5 kyu
#Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point


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
#lst = [1, 1, 1, 3, 1]
#lst = [2, 4, 4, 5, 4]
#lst = [4, 4, 4, 3, 3]
#lst = [1, 1]

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

#It is not my solution, but i like it
#from collections import Counter as count

#def score(dice):
#    threes, ones, c = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}, {1: 100, 5: 50}, count(dice)
#    return sum((c[v]//3)*threes[v] + (c[v]%3)*ones.get(v, 0) for v in c)
