from turtle import color
from PIL import Image
import numpy as np
####
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib as mpl
import cv2


###tser4_t0003.BMP    https://ru.stackoverflow.com/questions/1145128/Как-преобразовать-jpg-в-массив-numpy

i = Image.open('diplom/imagePage/tser4_t0000.bmp')#.convert('RGB')
#print(i)
iar = np.asarray(i)
img = iar.copy()
print(iar[1].shape)
print(iar.dtype)
cv2.imwrite("filearr2.png", iar)
#print(img)
#img[img < 100 ] = 0
#img[img >= 100 ] = 1
#print(np.shape(iar))
pdf = PdfPages("cletka.pdf")
plt.axis ("off")
plt.imshow(img[35:53,120:139])
pdf.savefig()
pdf.close()
plt.show()

x= np.unique(iar).size
print(iar.size)
pdf = PdfPages("Figures.pdf")
plt.axis ("off")
b = plt.imshow(img, cmap= 'gray')
pdf.savefig()
pdf.close()
plt.colorbar(b, ticks = [0,1])
plt.show()
pdf = PdfPages("Gist2.pdf")
plt.yscale("log")
per = np.percentile(iar, 100)
#print(per)
plt.axvline(per, color = "black")
plt.semilogy()
z = plt.hist(iar.ravel(),256, [0,256])
plt.xlabel('индекс цвета пикселя в палитре', fontsize=16)
plt.ylabel('частота', fontsize=16)

pdf.savefig()
pdf.close()
plt.show()


