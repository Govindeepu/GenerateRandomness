import random

def triad_check(string):
    triad_dic = {
        '000': [0, 0],
        '001': [0, 0],
        '010': [0, 0],
        '011': [0, 0],
        '100': [0, 0],
        '101': [0, 0],
        '110': [0, 0],
        '111': [0, 0]
    }
    for i in range(len(string)-3):
        if string[i + 3] == '0':
            triad_dic[string[i:i + 3]][0] +=1
        else:
            triad_dic[string[i:i + 3]][1] += 1
    return triad_dic

lst = []
print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")
while True:
    _input = input('Print a random string containing 0 or 1:\n').strip()
    for i in _input:
        if i == '0' or i == '1':
            lst.append(i)
    if len(lst) >= 100:
        string = ''.join(lst)
        print(f"\nFinal data string:\n{string}")
        break
    else:
        print(f'Current data length is {len(lst)}, {100 - len(lst)} symbols left')

def prediction(triad_dic):
    sa = ["0", "1"]
    d = [random.choice(sa), random.choice(sa), random.choice(sa)]
    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!""")
    money = 1000
    while True:
        print("")
        test = input("Print a random string containing 0 or 1:\n")
        if test == "enough":
            print("Game over!")
            break
        elif "0" not in test or "1" not in test:
            test = input("Print a random string containing 0 or 1:\n")
        if "0" in test or "1" in test:
            for i in range(len(test) - 3):
                g = triad_dic[f'{test[i]}{test[i + 1]}{test[i + 2]}']
                if g[0] > g[1]:
                    d.append("0")
                else:
                    d.append("1")
            print("prediction:")
            prediction1 = "".join(d)
            print(prediction1)
            e = []
            for i in range(3, len(test)):
                if test[i] == prediction1[i]:
                    e.append("T")
                else:
                    e.append("F")
            t = e.count("T")
            u = len(test) - 3
            perce = t / u
            perce1 = perce * 100
            perce2 = round(perce1, 2)
            money -= t
            money += (u - t)
            print("")
            print(f'Computer guessed right {t} out of {u} symbols ({perce2} %)')
            print(f'Your capital is now ${money}')
            print("")
            d = [random.choice(sa), random.choice(sa), random.choice(sa)]

tr = triad_check(string)
prediction(tr)