"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.




"""


n = input().split()
x = int(n[0])
y = int(n[1])
z = float(n[2])

print(x,y,'%5.2f'%(z))

n1 = input().split()
a = int(n1[0])
b = int(n1[1])
c = float(n1[2])
print(a,b,'%5.2f'%(c))
print('VALOR A PAGAR: R$ %5.2f '%((y*z)+(b*c)))