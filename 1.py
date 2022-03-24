#Faça um algoritmo que troque o valor de duas variáveis. Por exemplo, o algoritmo lê n1 igual a 3 e n2 a 17, e mostra n1 igual a 17 e n2 a 3.

n1 = 3
n2 = 17
print(n1,n2)
variavelTemporaria = n1
n1 = n2
n2 = variavelTemporaria 
print(n1,n2)