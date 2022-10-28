import cv2
import matplotlib.pyplot as plt

foto = cv2.imread("kopek.jpeg",0) 
h = [0] * 256
for x in range(foto.shape[0]):      #histogram hesaplaması yapıyoruz
    for y in range(foto.shape[1]):
        i = foto[x, y]
        h[i] = h[i] + 1

x = []
for i in range(0,256):
    x.append(i)

plt.stem(x, h)
plt.xlabel('Renk Tonları')
plt.ylabel('Piksel Sayısı')
plt.title('Görüntünün Histogramı')
plt.show()
