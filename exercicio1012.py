"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
PI = 3.14159
n1 = input().split()
a = float(n1[0])
b = float(n1[1])
c = float(n1[2])
trap = ((a+b)*c)/2
print(a,b,c)
print('TRIANGULO: %5.3f'%((a*c)/2))
print('CIRCULO: %5.3f'%((c**2)*PI))
print('TRAPEZIO: %5.3f'%(trap))
print('QUADRADO: %5.3f'%(b**2))
print('RETANGULO: %5.3f'%(a*b))

"""
PI = 3.14159
def areaTri(x, y, z):
    tri = (a*c)/2
    return tri
def areaCir(x, y, z):
    cir=  (c**2)*PI
    return cir
def areaTrap(x, y, z):
    trap = ((a + b) * c) / 2
    return trap
def areaQuad(x, y, z):
    quad = (b**2)
    return quad
def areaRet(x, y, z):
    ret = (a*b)
    return ret
n1 = input().split()
a = float(n1[0])
b = float(n1[1])
c = float(n1[2])
print(a,b,c)
print('TRIANGULO: %5.3f'%(areaTri(a,b,c)))
print('CIRCULO: %5.3f'%(areaCir(a,b,c)))
print('TRAPEZIO: %5.3f'%(areaTrap(a,b,c)))
print('QUADRADO: %5.3f'%(areaQuad(a,b,c)))
print('RETANGULO: %5.3f'%(areaRet(a,b,c)))
