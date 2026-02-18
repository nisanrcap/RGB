import cv2
import numpy as np

resim=cv2.imread("kusresmi.jpg")  #imread bir resim okuyacağını belirtir.
cv2.imshow("KUS RESMI",resim) #ilk parametre resmin köşesinde yazacak olan yazı ikincisi imshow komutunun göstereceği resim

print(resim) #her bir pikselin matriksel görünümünü verir

cv2.waitKey(0) #pencere açıldıktan sonra herhangi bir tuşa basılması için bekler
cv2.destroyAllWindows() #opencv ye bağlı tüm pencereleri kapat