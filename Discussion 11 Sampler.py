
import csv
import random

if __name__ == "__main__":

    x = []
    with open('../stat/Discussion 11 data.csv', 'r') as stuff:
        data = csv.reader(stuff)
        next(data)
        for line in data:
            x.append(line)

        tmpList = []

        with open('results.txt', 'w') as results:
            for z in range(0, 10):
                noCount = 0
                yesCount = 0
                for y in range(0, 40):
                    if x[random.randint(0, 1599)] == x[0]:
                        noCount = noCount + 1
                    else:
                        yesCount = yesCount + 1
                results.write('Sample ' + str(z+1) + ' had ' + str(noCount) + " No's and " + str(yesCount) + " Yes's\n" )



'''
#Test to see if I can read the data in, this works
    x = []
    with open('Discussion 11 data.csv', 'r') as stuff:
        data = csv.reader(stuff)
        next(data)
        for line in data:
            x.append(line)

    print(x[1599])
    print(len(x))
    print(random.randint(0,1599))
    '''

