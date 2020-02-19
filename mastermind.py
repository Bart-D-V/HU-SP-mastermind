'''''
play = 1 en play = 2 zijn algoritmen uit het artikel van de universiteit Groningen
'''''

import random
from itertools import compress, product
pinnetjes = [1 , 2 , 3 , 4 , 5 , 6]
codes = []
pogingen = 8
for i in product(*[pinnetjes]*4):
    codes.append(list(i))

# random code picker
def pickcode():
    return random.choice(codes)
# feedback van poging
def feedback(code1, code2):
    fb = [0, 0]
    lst = []
    y = 0
    for i in code2:
        if i == code1[y]:
            lst.append(y)
            fb[0] += 1
        else:
            x = 0
            for j in code1:
                if i == j and x not in lst:
                    lst.append(x)
                    fb[1] += 1
                    break
                x += 1
        y += 1
    return fb
# input code
def codeinput(precode):
    code = []
    for i in precode:
        code.append(int(i))
    return code
# algoritmen1
def algoritmen1(fb):
    trash = []
    for i in codes:
        if feedback(feedbackcode, i) != fb:
            trash.append(i)
    for i in trash:
        codes.remove(i)
play = int(input('kies 0 voor zelf spelen.\nkies 1 voor ai-1. \nkies 2 voor ai-2. '))
# algoritmen2
def algoritmen2(x):
    if x == 1:
        return codeinput('1123')
    else:
        bestcode = [[], 99999999]
        for i in codes:
            score = [i, 0]
            dict = {
                '00': 0, '10': 0, '20': 0, '30': 0, '40': 0, '01': 0, '02': 0, '03': 0, '04': 0, '11': 0, '12': 0, '13': 0, '21': 0, '22': 0, '31': 0
            }
            for j in codes:
                dict[''.join(map(str, feedback(i, j)))] += 1
            for q in dict:
                score[1] += dict[q]**2
            score[1] = score[1] / len(codes)
            if score[1] < bestcode[1]:
                bestcode = score
    return bestcode[0]
# algoritmen3
def algoritmen3(fb):
    lst = []
    for i in codes:
        if feedback(feedbackcode, i) == fb:
            lst.append(i)
    return lst
# zelfspelen
if play == 0:
    secret = pickcode()
    while pogingen > 0:
        print('nog ' + str(pogingen) + ' pogingen')
        poging = (feedback(secret, codeinput(input('geef code: '))))
        if poging == [4, 0]:
            print('je hebt gewonnen!')
            break
        else:
            print('feedback' + str(poging))
        pogingen -= 1
    if pogingen == 0:
        print('je hebt verloren')
# AI-1
elif play == 1:
    secret = codeinput(input('geef secret: '))
    while pogingen > 0:
        print('nog ' + str(pogingen) + ' pogingen')
        feedbackcode = pickcode()
        print(feedbackcode)
        if feedback(secret, feedbackcode) == [4, 0]:
            print('je hebt gewonnen!')
            break
        else:
            algoritmen1(codeinput(input('geef feeback: ')))
        pogingen -= 1
    if pogingen == 0:
        print('je hebt verloren')
# AI-2
elif play == 2:
    secret = codeinput(input('geef secret: '))
    while pogingen > 0:
        print('nog ' + str(pogingen) + ' pogingen')
        feedbackcode = algoritmen2(pogingen)
        print(feedbackcode)
        if feedback(secret, feedbackcode) == [4, 0]:
            print('je hebt gewonnen!')
            break
        else:
            algoritmen1(codeinput(input('geef feeback: ')))
        pogingen -= 1
    if pogingen == 0:
        print('je hebt verloren')
# AI-3
else:
    secret = pickcode()
    lst = []
    while pogingen > 0:
        print('nog ' + str(pogingen) + ' pogingen')
        if pogingen == 1:
            print(max(set(lst), key=lst.count))
            if feedback(secret, (max(set(lst), key=lst.count))) == [4, 0]:
                print('je hebt gewonnen!')
                break
            else:
                pogingen = 0
                break
        feedbackcode = pickcode()
        print(feedbackcode)
        print(feedback(secret, feedbackcode))
        if feedback(secret, feedbackcode) == [4, 0]:
            print('je hebt gewonnen!')
            break
        else:
            lst += algoritmen3(feedback(secret, feedbackcode))
        pogingen -= 1
    if pogingen == 0:
        print('je hebt verloren')