from os import listdir
from os.path import isfile, join
import numpy
from scipy.stats import kendalltau
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import seaborn as sns
import pandas as pd
import networkx as nx
from scipy.stats import gaussian_kde
from statsmodels.nonparametric.kernel_density import KDEMultivariate
import sys


def kdedensity(i1, i2, j1, j2, iter):
    cellOver = arr3D[:100, i1:i2, j1:j2]
    D = np.empty((cellOver.shape[0], cellOver.shape[1], cellOver.shape[2]), dtype='float')
    for x in range(cellOver.shape[1]):
        for y in range(cellOver.shape[2]):  
            for t in range(cellOver.shape[0]):
                if t == 0:
                    D[0,x,y] = cellOver[0,x,y]
                else:
                    D[t, x, y] = np.abs(cellOver[t,x,y] - cellOver[t-1,x,y])
    #print(D)
    if iter == 1:
        i1, i2, j1, j2 = 0,10,10,20 #вне
        nameTitle = "KDE Вне клетки(эксперимент1)"
        nameFile = "./diplom/myImage/KDE Вне клетки(эксперимент1).png"
    elif iter == 2:
        i1, i2, j1, j2 = 21,32,37,45 # право
        nameTitle = "KDE Правая клетка(эксперимент)"
        nameFile = "./diplom/myImage/KDE Правая клетка(эксперимент1).png"
    elif iter == 3:
        i1, i2, j1, j2 = 38,48,0,10 # низ
        nameTitle = "KDE Нижняя клетка(эксперимент1)"
        nameFile = "./diplom/myImage/KDE Нижняя клетка(эксперимент1).png"
    elif iter == 4:
        i1, i2, j1, j2 = 14,25,14,28 # верх
        nameTitle = "KDE Верхняя клетка(эксперимент1)"
        nameFile = "./diplom/myImage/KDE Верхняя клетка(эксперимент1).png"
    else:
        i1, i2, j1, j2 = 27,36,16,28 # центр
        nameTitle = "KDE Центральная клетка(эксперимент1)"
        nameFile = "./diplom/myImage/KDE Центральная клетка(эксперимент1).png"
    
    
    cellOver1 = D[:,i1:i2, j1:j2].copy()
    #cellOver1 = cellOver[:,i1:i2, j1:j2].copy()
    cellOver1 = cellOver1.astype(float)
    intens = list(cellOver1.reshape(100 * (i2 - i1) * (j2 - j1),))
    #intens = [(i%(cellOver1.shape[1]*cellOver1.shape[2]) / cellOver1.shape[1]*cellOver1.shape[2]) + intensOld[i] for i in range(len(intensOld))]
    #intens = [intensOld[i]+np.random.uniform(-0.5, 0.5) for i in range(len(intensOld))]

    timeOld = list(np.repeat(np.arange(100), (i2 - i1) * (j2 - j1)).astype(float))
    time = [i +np.random.uniform(-0.5, 0.5) for i in timeOld]
    
    #time = [(i/len(timeOld)) + timeOld[i] for i in range(len(timeOld))]
    
    #time += np.random.uniform(-0.5, 0.5, time.shape)
    #yedges = np.linspace(0, np.amax(cellOver1), 100)  # 53
    yedges = np.linspace(0, np.amax(cellOver1), 100)
    yedges_new = np.linspace(0, np.amax(cellOver1), 3 * len(yedges))
    bw = [0.5, 3]  # Ширина полосы для каждой оси

    
    kde = KDEMultivariate(data=[time, intens], var_type='cc', bw=bw)

    
    #x = np.arange(100)
    x = np.arange(100)
    x_new = np.linspace(0, 100, 10 * len(x))
    grid = np.array(np.meshgrid(x_new, yedges_new)).T.reshape(-1, 2)

    
    z = kde.pdf(grid).reshape(x_new.shape[0], yedges_new.shape[0])
    z = z.T
    ##
    # zNew = np.zeros((z.shape[0], z.shape[1]))
    # for i in range(z.shape[0]):
    #     for j in range(z.shape[1] - 1):
    #         if i == 0 and j == 0:
    #             zNew[0][0] = z[0][0]
    #         elif i == z.shape[0] - 1 and j == z.shape[1] - 1:
    #             zNew[-1][-1] = z[-1][-1]
    #         else:
    #             zNew[i][j+1] = np.abs(z[i][j+1] - z[i][j])
    ##
 
    
    extent = [x_new[0], x_new[-1], yedges_new[0], yedges_new[-1]]
    fig, ax = plt.subplots()
    fig.set_size_inches(16, 9)
    im = ax.imshow(z, origin='lower', cmap=plt.cm.jet, interpolation='nearest', extent=extent, aspect='auto')
    plt.axhline(0, color='black', linestyle='--')
    cbar = fig.colorbar(im)
    #ax2 = fig.add_axes([0.15, 0.55, 0.3, 0.3])
    #ax2.imshow(cellOver1[0,:,:])
    #ax2.axis('off')
    #plt.imshow(z, origin='lower', cmap=plt.cm.jet, interpolation='nearest', extent=extent, aspect='auto')
    plt.title(nameTitle)
    plt.savefig(nameFile)
    #fig.savefig("./KDE Вне клетки.png")
    plt.show()

    



mypath='C:/Users/rusan/AppData/Local/Programs/Python/Python311/work/diplom/imagePage'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
arr3D = np.empty((1200,512,512), dtype='float')
for n in range(0, len(onlyfiles)):
    tmp = cv2.imread(join(mypath,onlyfiles[n]), 0)
    arrTmp = np.asarray(tmp)
   #arrTmp = cv2.GaussianBlur(arrTmp, (3, 3),0) #19,19
    images[n] = arrTmp
    arr3D[n] = images[n]
iter = sys.argv[1]
kdedensity(390,448,15,60, int(iter))