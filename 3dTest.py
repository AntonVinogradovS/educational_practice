from os import listdir
from os.path import isfile, join
from signal import signal
import numpy
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import seaborn as sns
#from NumbaLSODA C:\Users\rusan\AppData\Local\Programs\Python\Python311\work — копия\work — копия\diplom\3dTest.py
#mypath='C:/Users/rusan/AppData/Local\Programs/Python/Python311/work — копия/work — копия/diplom/imagePage'
mypath='C:/Users/rusan/AppData/Local/Programs/Python/Python311/work/diplom/imagePage'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
arr3D = np.empty((1200,512,512), dtype='uint8')
for n in range(0, len(onlyfiles)):
    tmp = Image.open(join(mypath,onlyfiles[n]))
    images[n] = np.asarray(tmp)
    arr3D[n] = images[n]
    

print(arr3D[0])

t = arr3D[0]
print(t.size)
cv2.imwrite("cletka.png", t)
cell = t[35:53, 120:139]
print(cell.shape)


cellOver = arr3D[:,35:53,120:139]
print(cellOver.shape)
signal = cellOver[0:1200,5,12]

signal2 = cellOver[0:1200,6,12]
signal3 = cellOver[0:1200,2,3]
#print(signal.shape)
arrCount = []
tm = range(1200)
xx = 0
#intens = cellOver.ravel(order='F')

intens = cellOver.reshape(410400,)
intens2 = intens[:120000]
#plt.plot(intens[:1200])
#plt.plot(cellOver[:,0,0])

time = []
cell1D = []
index = 0
for i in range(18):
    for j in range(19):
        t = cellOver[:100, i,j]
        m = np.delete(t, np.where(t > 100)[0])
        for cell in range(int(m.shape[0])):
            cell1D.append(m[cell])
            time.append(cell)    
        index += 1

pdf = PdfPages("2dhist1.pdf")
plt.hist2d(time,cell1D, bins = 50, cmap=plt.cm.jet)
plt.xlabel("время")
plt.ylabel("интенсивность")
plt.colorbar(label = "скопление точек")
pdf.savefig()
pdf.close()

#time = []
#for i in range(1200):
#    for j in range(100):
#        time.append(i)
#
#plt.hist2d(time,intens2, bins=50,cmap=plt.cm.jet)
#plt.colorbar()



       
        








plt.show()
