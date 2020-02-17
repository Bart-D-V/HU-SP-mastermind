import random
from itertools import compress, product
pinnetjes = [1 , 2 , 3 , 4 , 5 , 6]
codes = []
pogingen = 1
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
    print(lst)
    return fb
# input code
def codeinput(precode):
    code = []
    for i in precode:
        code.append(int(i))
    return code

play = 0 #int(input('kies 0 voor zelf spelen.\nkies 1 voor pc. \n'))
if play == 0:
    secret = pickcode()
    while pogingen <= 10:
        print(secret)
        print('je ' + str(pogingen) + ' poging')
        poging = (feedback(secret, codeinput(input('geef code: '))))
        if poging == [4, 0]:
            print('je hebt gewonnen!')
            break
        else:
            print('feedback' + str(poging))
        pogingen += 1
    if pogingen == 10:
        print('je hebt verloren')

else:
    secret = codeinput(input('geef secret: '))
    while pogingen <= 10:
        print('je ' + str(pogingen) + ' poging')

        pogingen += 1