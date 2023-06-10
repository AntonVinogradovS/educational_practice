import math
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def exponentialDistribution(lamb, count):
    x = []
    for i in range(count):
        u = random.random()
        x.append(-math.log(1 - u)/lamb)
    return x
def teorFunc(lamb, data1, numberObservations):
    res1 = []
    data = np.linspace(0, max(data1), 10000)
    for i in range(len(data)):
        res1.append(1 - np.exp(-lamb*data[i]))
    res2 = []
    res2.append(0)
    t = 0

    
    for i in range(len(data1)):
        for j in range(len(data1)):
            if data1[j] <= data1[i]:
                t += 1
        res2.append(t/numberObservations)
        t = 0
    de = max(abs(res2[i+1] - (1 - np.exp(-lamb * res[i]))) for i in range(len(res2)-1))
    # de = list(set(res1) - set(res2))
    # de = abs(de[0] - de[1])
    data1.insert(0,0)
    print(res1, res2)
    plt.show()
    plt.plot(data, res1)
    plt.step(data1, res2, where='mid')
    plt.title(de)
    plt.show()
        
def theoreticalDistributionDensity(lamb, zArr):
    res = []
    for i in zArr:
        res.append(lamb*math.exp(-lamb*i))
    return res
def F(x, la):  # теоретическая функция распределения
    if x < 0:
        return 0
    else:
        return 1 - np.e ** (-la * x)
def n_in_zi(X, N, left, right):
    n = 0
    for i in range(N):
        if X[i] >= left:
            if X[i] < right:
                n += 1
            else:
                return n
    return n

def numericalCharacteristics(data, numberObservations, lambd):
    
    E = 1/lambd
    xMid = 0
    D = 1/lambd**2
    S = 0
    Me = 0
    R = 0
    xMid = sum(data)/numberObservations
    tmp = []
    for i in data:
        tmp.append((i - xMid)**2)
    S = sum(tmp)/numberObservations
    R = data[-1] - data[0]

    k = 0
    if numberObservations % 2 != 0:
        k = numberObservations // 2
        Me = data[k]
    else:
        k = int(numberObservations/2) - 1
        print("K", k, data[k], data[k+1])
        Me = (data[k] + data[k+1])/2
    r1 = abs(E-xMid)
    r2 = abs(D - S)
    dic = {'En': E, 'xMid': [xMid], '|En - xmid|': [r1], 'D': [D], 'S^2': [S], '|D - S^2|' : [r2], "Me^": [Me], 'R^': [R]}
    df3 = pd.DataFrame(dic)
    print(df3)
    return 0


def theoreticalProbability(bin3, lamb):
    res = []
    for i in range(1, len(bin3)):
         res.append(-1*math.exp(-lamb*bin3[i]) + math.exp(-lamb*bin3[i-1]))
    res.append(math.exp(-lamb*bin3[-1]))
    return res
# def R0(nj, qj, n):
#     tmp = []
#     for i in range(len(nj)):
#         tmp.append((nj[i] - n*qj[i])**2/(n*qj[i]))
#     return sum(tmp)
def numberObservationsIntervals(bin3, res):
    dd = {}
    ddArr = []
    for j in range(0, len(bin3)):
        dd[j] = 0
    for i in res:
        for j in range(1, len(bin3)):
            if bin3[j-1] < i <= bin3[j]:
                dd[j-1] += 1
                break
        if i > bin3[-1]:
            dd[len(dd) - 1] += 1
    ddArr = list(dd.values())
    return ddArr


def density(x, r):
    if x <= 0:
        return 0
    else:
        return 2 ** (-r / 2) * (1 / math.gamma(r / 2)) * x ** (r / 2 - 1) * math.exp(-x / 2)


def integral(a, b, r):
    n = 1000
    t = (b - a) / n
    res = 0
    for i in range(n):
        res += (density(a + t * i, r) + density(a + t * (i + 1), r)) * t / 2
    return res


def Function(R_0, r):
    return 1 - integral(0, R_0, r)

def experiment(N, _lambda):
    data = []
    U = np.random.uniform(0, 1, N)
    for u in U:
        sv_unit = -np.log(1 - u) / _lambda
        data.append(sv_unit)
    data.sort()
    return data

lamb = float(input("Введите значение лямбда: "))
numberObservations = int(input("Введите количество наблюдений: "))
res = exponentialDistribution(lamb, numberObservations)
res = sorted(res)
dict = {}
for i in range(numberObservations):
    tmp = 'x' + str(i+1)
    dict[tmp] = res[i]
data = [dict]
df = pd.DataFrame(data)
df = df.to_string(index=False)
print(df)
if True:
    xMax = res[-1]
    xMin = res[0]
    p = (xMax-xMin)/10
    bin = list(np.arange(xMin,xMax, p))
    bin.append(xMax)
    #print(bin)
    #counts, bins, patches  = plt.hist(res, bins = bin, density= True)
    #plt.show()

    # высота столбцов
    dd = {}
    for j in range(0, len(bin) - 1):
                dd[j] = 0
    for i in res:
        for j in range(1, len(bin)):
            if bin[j-1] < i <= bin[j]:
                dd[j-1] += 1
                break
    ddArr = list(dd.values())
    for i in range(1, len(bin)):
        leng = (bin[i] - bin[i-1])
        ddArr[i - 1] = ddArr[i-1]/ (bin[i] - bin[i-1] ) / numberObservations
    #b, c, n = plt.hist(res,  bins= bin, density= True)
    #plt.show()

    #print(b)
    z = []
    for i in range(1, len(bin)):
        z.append((bin[i-1]+bin[i])/2)
    distributionDensity = theoreticalDistributionDensity(lamb, z)
    # plt.plot(res)
    # plt.show()
    # print(z)
    # print(distributionDensity)
    # print(ddArr[-1]) # высота столбцов
    # print(bin[-1])
    df2 = pd.DataFrame({'zj': z, 'f(zj)': distributionDensity, 'nj/n|len|': ddArr})
    print(df2)

    q = []
    for i in range(len(ddArr)):
        q.append(abs(ddArr[i] - distributionDensity[i]))
        #q.append(abs(counts[i] - distributionDensity[i]))
    print("Максимальное отклонение = ", max(q))
numericalCharacteristics(res, numberObservations, lamb)
teorFunc(lamb, res, numberObservations)
## ТРЕТЬЯ ЛАБА

# bin3 = list(np.arange(xMin,xMax, 0.15))
# bin3.append(xMax)
# qj = []
# qj = theoreticalProbability(bin3, lamb)
# nj = numberObservationsIntervals(bin3, res)
#R = R0(nj, qj, numberObservations)






alpha = float(input('Введите уровень значимости: '))
count_intervals = int(input('Введите число отрезков разбиения:'))
accepted = 0
denied = 0
N = numberObservations
n_in = []
for i in range(count_intervals):
    n_in.append(0)
for k in range(100):
    intervals = [0] * (count_intervals - 1)
    data = experiment(N, lamb)
    ppp = 1 / count_intervals
    for i in range(count_intervals - 1):
        intervals[i] = np.log(1 - (i + 1) * ppp) / (-lamb)
    q = [0] * count_intervals
    q[0] = F(intervals[0], lamb)
    q[count_intervals - 1] = 1 - F(intervals[count_intervals - 2], lamb)
    for i in range(1, count_intervals - 1):
        q[i] = F(intervals[i], lamb) - F(intervals[i - 1], lamb)

    R0 = (n_in_zi(data, N, -10000, intervals[0]) - N * q[0]) ** 2 / (N * q[0])
    n_in[0]=n_in_zi(data, N, -10000, intervals[0])
    for i in range(1, count_intervals - 1):
        R0 += (n_in_zi(data, N, intervals[i - 1], intervals[i]) - N * q[i]) ** 2 / (N * q[i])
        n_in[i] = n_in_zi(data, N, intervals[i - 1], intervals[i])
    R0 += (n_in_zi(data, N, intervals[count_intervals - 2], 10900) - N * q[count_intervals - 1]) ** 2 / (
                N * q[count_intervals - 1])
    n_in[-1]=n_in_zi(data, N, intervals[count_intervals - 2], 10900)
    value_list3 = [n_in]
    column_list3 = ["( -infinity; " + str(intervals[0]) + ")"]
    for i in range(1, count_intervals - 1):
        column_list3 += ["[ " + str(intervals[i - 1]) + "; " + str(intervals[i]) + ")"]
    column_list3 += ["[ " + str(intervals[count_intervals - 2]) + "; +infinity)"]
    #print("RO - ", R0)
    FR0 = Function(R0, count_intervals - 1)
    #print("F(RO) - ", FR0)

    if FR0 > alpha:
        accepted+=1
    else:
        denied+=1
print(f'Из {100} опытов гипотеза принята {accepted} раз')










#print(R)
#F_R0 = np.exp(-lamb*R)
# print("F_R0 ", F_R0)
# alfa = float(input("Введите уровень значимости: "))
# if F_R0 >= alfa:
#     print("H0 отвергается")
# else:
#     print("H0 принимается") 








