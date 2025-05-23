
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def Media():


       img=cv2.imread('Juego.png',0)
       A=img.copy()/255
       
       m,n=A.shape
       B=np.zeros((m,n));
       i=2
       j=2
       
       for i in range(m-1):
           for j in range(n-1):
               B[i,j]=(A[i-j,j-1]   +A[i-1,j]  +A[i-1,j+1]
                       +A[i,j-1]    +A[i,j]    +A[i,j+1]
                       +A[i+1,j+1]  +A[i+1,j]  +A[i+1,j+1])
               B[i,j]=B[i,j]/9;
       
       cv2.imshow('Original',img)
       cv2.imshow('Filtro de media',B)
       
       cv2.waitKey(0)
       cv2.destroyAllWindows()

       plt.show()
       

def Mediana():
    #con=True
    #while con:
       
        img = cv2.imread('Juego.png')
        median = cv2.medianBlur(img,5)#calcula la mediana 
        blur = cv2.blur(img,(3,3))
 
        plt.subplot(121),plt.imshow(img),plt.title('Original') #permite subdividir la ventana. muestra la imagen en escala de grises
        plt.xticks([]), plt.yticks([]) #establece los valores en el eje x

        plt.subplot(122),plt.imshow(median),plt.title('Filtro de mediana')
        plt.xticks([]), plt.yticks([])
        plt.show()

        

def Laplaciano():

  
        img=cv2.imread('Taj.jpg',0)
        A=img.copy()/255
        
        m,n=A.shape
        B=np.zeros((m,n));
        i=2
        j=2
        
        h=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        for i in range(m-1):
            for j in range(n-1):
                B[i,j]=(h[0,0]*A[i-1,j-1] +h[0,1]*A[i-1,j] +h[0,2]*A[i-1,j+1]
                       +h[1,0]*A[i,j-1]   +h[1,1]*A[i,j]   +h[1,2]*A[i,j+1]
                       +h[2,0]*A[i+1,j+1] +h[2,1]*A[i+1,j] +h[2,2]*A[i+1,j+1])
        
                B[i,j]=abs(B[i,j])
        
        
        cv2.imshow('Original',img)
        cv2.imshow('Filtro de laplaciano',B)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        

def Sobel():
   

         def filtro_sobel(imagen):
         # Convertir la imagen a escala de grises
           imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
           
           # Aplicar el filtro Sobel en el eje X y Y
           sobel_x = cv2.Sobel(imagen_gris, cv2.CV_64F, 1, 0)
           sobel_y = cv2.Sobel(imagen_gris, cv2.CV_64F, 0, 1)
           
           # Calcular la magnitud del gradiente
           magnitud = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
           magnitud = np.uint8(magnitud)
           
           # Devolver la imagen con el filtro aplicado
           return magnitud
         
         # Cargar la imagen
         imagen = cv2.imread("Taj.jpg")
         
         # Aplicar el filtro sobel
         imagen_filtrada = filtro_sobel(imagen)
         
         # Mostrar la imagen original y la imagen filtrada
         cv2.imshow("Original", imagen)
         cv2.imshow("Filtro Sobel", imagen_filtrada)
         
         cv2.waitKey(0)
         cv2.destroyAllWindows()

         


def Menu():
   print("\t=======================================================================")
   print("\t=========================FILTRADO DE IMAGENES==========================")
   print("\t=======================================================================")
   print("\n\t\t-:MENU.-")
   print("\t[1].Filtrado de la media")
   print("\t[2].Filtrado de la mediana")
   print("\t[3].Filtrado con el  Laplaciano")
   print("\t[4].Filtrado con el Sobel")

   opc=int(input("\nElija una de las opciones de filtrado:"))
   return opc


def main():
    continuar=True
   
    while continuar:
        os.system('cls')
        opc= Menu()
        if opc==1:
            Media()
         
        if opc==2:
            Mediana()
          
        if opc==3:
            Laplaciano()
     
        if opc==4:
            Sobel()

        continuar=input("Deseas continuar(S/N):")=='S'
        

main()
