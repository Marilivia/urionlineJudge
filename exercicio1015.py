"""

Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""
from math import sqrt

def calcular_distacia_entre_dois_pontos(x1,x2,y1,y2):

   d1 = ((x2-x1)**2 + (y2-y1)**2)
   print(d1)
   raiz = sqrt(d1)
   return raiz

if __name__ == '__main__':
    x1 = float(input())
    x2 = float(input())
    y1 = float(input())
    y2 = float(input())
    print(calcular_distacia_entre_dois_pontos(x1,x2,y1,y2))
