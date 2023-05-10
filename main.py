#===============================================================================
# Trabalho 1
#-------------------------------------------------------------------------------
# Autor: Eduarda Simonis Gavião
# UNICAMP
#===============================================================================
# Importando bibliotecas
import sys
import numpy as np
import cv2

#importando a Imagem
BABOON_IMAGE =  'baboon.png'
BUTTERFLY_IMAGE =  'butterfly.png'
DUCK_IMAGE =  'gesonel.png'


# Exercicio 1.1
def mosaic_grid(img):
    (h, w) = img.shape[:2] #obtem as dimensões da imagem
   
    (cX, cY)=(w//4,h//4) ## define as dimensões das "fatias"
    copia =img.copy()
    
    cv2.imshow("Original",img)

    # desenha o grid
    img[0:h:cY]=1
    img[:,0:w:cX]=1

    cv2.imshow("Grid",img)
    embaralha = []
    # gerando a lista das imagens recortadas

    #percorre a imgem dividindo ela
    for j in range(4):
        for i in range(4):
            embaralha.append(copia[j*cY:(j+1)*cY,i*cX:(i+1)*cX]) ## salva a nova imagem em uma lista
    ## concatenando horizontalmente
    new_img1= cv2.hconcat([embaralha[0],embaralha[10],embaralha[12],embaralha[2]])
    new_img2= cv2.hconcat([embaralha[7],embaralha[15],embaralha[0],embaralha[8]])
    new_img3= cv2.hconcat([embaralha[11],embaralha[13],embaralha[1],embaralha[6]])
    new_img4= cv2.hconcat([embaralha[3],embaralha[14],embaralha[9],embaralha[4]])
    
    ## cacatenando verticalmente
    embaralhada= cv2.vconcat([new_img1,new_img2,new_img3,new_img4])
    cv2.imshow('Embaralhada',embaralhada)    

## Exercicio 1.2   
def combination(img1, img2): # para esse exercicio é necessario a entrada de duas imagens
    
    alpha=0.5 #passando o parametro de peso a ser aplicado na primeira imagem
    beta= 0.5 #passando o parametro de peso a ser aplicado na segunda imagem
    img = cv2.addWeighted(img1,alpha,img2,beta,0) # cv2.addWeighted utiliza dos parametros passados acima, das imagens e um valor gama (valor escalar adicionado a cada soma)
    
    cv2.imshow('Combinação 1',img)
    #cv2.imwrite("nome_da_imagem.png", img)

## Exercicio 1.3
def intensity(img):
    negative= abs(255-img) # subtrai de cada valor de cor 255
    cv2.imshow('Negativa',negative)

    baixo= np.where(img<=100,100,img) ## valores abaixo do minimo requerido passam a ter valor 100
    alto= np.where(baixo>=200,200,baixo) ##valores acima do máximo requerido passam a ter valor 200

    image=  (alto-np.min(alto))/(np.max(alto)-np.min(alto)) ##formula de normalização de imagem

   
    cv2.imshow('Mudanca no intervalo de intensidade',image)
    #cv2.imwrite("nome_da_imagem.png", image)

    copia =img.copy() #cria uma cópia da imagem
    copia=copia[:,::-1] #inverte as linhas

    (h, w) = img.shape[:2]
    pares= img.copy()

    #percorrendo a imagem pixel a pixel onde linhas pares sofrem inversão
    for y in range(0,h):
        for x in range(0,w):
            if(y%2==0):
                pares[y,x]=copia[y,x]
            else:
                pares[y,x]=img[y,x]
    
    cv2.imshow("Linhas Invertidas",pares)
    #cv2.imwrite("nome_da_imagem.png", pares)

    reflexao= img.copy() #cria uma copia da imagem
    ref=reflexao[::-1,:]  #inverte as colunas
    
    #percorrendo a imagem pixel a pixel onde metade sofre reflexão
    for y in range(0,h):
        for x in range(0,w):
            if(y<=h/2):
                reflexao[y,x]=img[y,x]
            else:
                reflexao[y,x]=ref[y,x]
    
    cv2.imshow("Reflexão da Metade",reflexao)
    #cv2.imwrite("nome_da_imagem.png", reflexao)

    espelho_vertical=img.copy()
    espelho_vertical=espelho_vertical[::-1,:]
    cv2.imshow("Espelhamento Vertical",espelho_vertical)

    #cv2.imwrite("nome_da_imagem.png", espelho_vertical)

#Exercicio 1.4 a
def img_coloridas(img):
    
    ##(b, g, r)
    (h, w) = img.shape[:2]
    (azul,verde,vermelho)=cv2.split(img) ##obtem os canais da imagem
    B_linha= azul.copy() #cria uma cópia do canal azul
    G_linha= verde.copy() #cria uma cópia do canal verde
    R_linha= vermelho.copy() #cria uma cópia do canal vermelho

    
    ## verificando os canais separadamente
    cv2.imshow("R", R_linha)
    cv2.imshow("B", B_linha)
    cv2.imshow("G", G_linha)

    #percorrendo a imagem pixel a pixel fazendo a manipulação dos canais
    for j in range(h):
        for i in range(w):
            B= (0.131 * azul[j][i] + 0.534* verde[j][i]+ 0.272 * vermelho[j][i])
            if(B>255):
                B_linha[j][i]=255 # valor limitado em 255
            else:
                B_linha[j][i]=B
            G = (0.168 * azul[j][i] + 0.686 * verde[j][i] + 0.349 * vermelho[j][i])
            if(G>255):
                G_linha[j][i]=255 # valor limitado em 255
            else:
                G_linha[j][i]=G
            R=(0.189 * azul[j][i] + 0.769 * verde[j][i]+ 0.393 * vermelho[j][i])
            if(R>255):
                R_linha[j][i]=255 # valor limitado em 255
            else:
                R_linha[j][i]=R  
    
    img_final=cv2.merge([B_linha,G_linha,R_linha]) #une os canais

    
    cv2.imshow("RGB final",img_final)
    
    #cv2.imwrite("nome_da_imagem.png", img_final)
    cv2.imshow("Original",img)
    

#Exercicio 1.4 b
def colorida_cinza(img):
    (h, w) = img.shape[:2] ##tamanho da imagem

    (azul,verde,vermelho)=cv2.split(img)#separação dos canais

    I_linha= img = np.zeros((h,w,1), dtype=np.uint8)

    #percorrendo a imagem pixel a pixel fazendo a manipulação
    for j in range(h):
        for i in range(w):
            I= (0.1140 * azul[j][i] + 0.5870* verde[j][i]+ 0.2989 * vermelho[j][i])
            if(I>255):
                I_linha[j][i]=255
            else:
                I_linha[j][i]=I
    cv2.imshow("Canal unico", I_linha)
    
    print(I_linha.shape)   ## print das dimensões das camadas provando a existência de um único canal         
    #cv2.imwrite("nome_da_imagem.png", I_linha)
 
#Exercicio 1.5

def ajuste_brilho(img):
    gama=3.5
    numpydata = np.array(img/255)# normalização para 0 e 1
    img_gama=np.array((numpydata**(1/gama))) ## Aplicando a correção gama

    cv2.imshow("Gama",img_gama)

#Exercicio 1.6
def quantizacao(img):
   K=2 ## refere-se aos níveis de cinza
   image=np.amax(img)+1 ## retorna o máximo valor da imagem
   
   #operações de Quantização
   a = np.uint8(img/(image/(K))) 
   quantizado= np.uint8((a/(K-1.))*255)

   cv2.imshow('Imagem quantizada',quantizado)

#Exercicio 1.7
def bit_plane(img):
    # criando uma lista vazia
    n=7 ## valor do plano de bit
    out = []
    
    plane = np.full((img.shape[0], img.shape[1]), 2 ** (n), np.uint8) #plano de bits
    res = cv2.bitwise_and(plane, img) ## utilizando bitwise com o plano e a imagem
    
    x = res * 255 

    # Guardando o resultado em um lista
    out.append(x)

    cv2.imshow("PLano de Bits", np.hstack(out))

#Exercicio 1.8
def filtragem(img,img_rgb):

    ##filtros para imagens monocromáticas
    kernel_h1 = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
    kernel_h11= np.array([[-1,-1,0],[-1,0,1],[0,1,1]])

    filtro_h1= cv2.filter2D(img,ddepth=-1, kernel=kernel_h1)
    filtro_h11= cv2.filter2D(img,ddepth=-1, kernel=kernel_h11)

    cv2.imshow("Imagem Original", img)
    cv2.imshow('Filtro h1',filtro_h1)
    cv2.imshow('Filtro h11',filtro_h11)

    ## demais filtros
    kernel_h2 = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
    kernel_h3= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    kernel_h4= np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    kernel_h5= np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

    kernel_h6= np.array([[1,1,1],[1,1,1],[1,1,1]])
    kernel_h7= np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
    kernel_h8= np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
    kernel_h9= np.array([[1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],
                               [0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1]])
    
    kernel_h10= np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])
    
    kernel_h3_h4= (((kernel_h3)**2)+((kernel_h4)**2))**(1/2)
    filtro_h2= cv2.filter2D(img_rgb,ddepth=-1, kernel=(1/256)*kernel_h2)    
      
    filtro_h6= cv2.filter2D(img_rgb,ddepth=-1, kernel=(1/9)*kernel_h6)
    filtro_h9= cv2.filter2D(img_rgb,ddepth=-1, kernel=(1/9)*kernel_h9)
    filtro_h10= cv2.filter2D(img_rgb,ddepth=-1, kernel=(1/8)*kernel_h10)
    filtro_h3=cv2.filter2D(img_rgb,ddepth=-1, kernel=kernel_h3)
    filtro_h4=cv2.filter2D(img_rgb,ddepth=-1, kernel=kernel_h4)
    filtro_h3_h4=cv2.filter2D(img_rgb,ddepth=-1, kernel=kernel_h3_h4)
    
    filtro_hn= cv2.filter2D(img_rgb,ddepth=-1, kernel=kernel_h5)## para alterar o filtro basta alterar a variavel kernel, para o kernel desejado

    #apresentação em visor dos filtros
    cv2.imshow("Imagem Original", img_rgb)
    cv2.imshow('Filtro h2',filtro_h2)
    cv2.imshow('Filtro h6',filtro_h6)
    cv2.imshow('Filtro h9',filtro_h9)
    cv2.imshow('Filtro h10',filtro_h10)
    cv2.imshow('Filtro h3',filtro_h3)
    cv2.imshow('Filtro h4',filtro_h4)
    cv2.imshow('Filtro h3_h4',filtro_h3_h4)


def main ():

    # Abre a imagem em escala de cinza.
    img1 = cv2.imread (BABOON_IMAGE,0)
    img2 = cv2.imread (BUTTERFLY_IMAGE,0)
    color1=cv2.imread(DUCK_IMAGE)
    
    
    ##menu
    print('Qual problema deseja resolver?')
    print('Para 1.1 digite 1')
    print('Para 1.2 digite 2')
    print('Para 1.3 digite 3')
    print('Para 1.4-a digite 4a')
    print('Para 1.4-b digite 4b')
    print('Para 1.5 digite 5')
    print('Para 1.6 digite 6')
    print('Para 1.7 digite 7')
    print('Para 1.8 digite 8')
    op = input("Indique a operação ")

    #tratamento de opções
    if op == "1":
        mosaic_grid(img1) #1.1
    elif op =="2":
        combination(img1,img2) #1.2
    elif op == "3":
        intensity(img1) #1.3
    elif op =="4a":
        img_coloridas(color1) #1.4 a
    elif op == "4b":
        colorida_cinza(color1) #1.4 b
    elif op =="5":
        ajuste_brilho(img1) #1.5
    elif op =="6":
        quantizacao(img1) #1.6
    elif op =="7":
        bit_plane(img1) #1.7
    elif op =="8":
        filtragem(img1,color1)
    else: 
        print('Opção inválida')

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
