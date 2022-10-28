import cv2

foto = cv2.imread("cicek.jpg",0)
foto_max=0

for i in range(foto.shape[0]):  #fotoğraftaki en büyük değeri bulma
    for j in range(foto.shape[1]):
        if(foto[i,j]>foto_max):
            foto_max=foto[i,j]
print(foto_max)

cv2.imshow("normal",foto)        #fotoğrafı tersleme
cv2.waitKey()
for i in range(foto.shape[0]):
    for j in range(foto.shape[1]):
        foto[i,j] = foto_max-foto[i,j]


cv2.imshow("terslenmis",foto)
cv2.waitKey()