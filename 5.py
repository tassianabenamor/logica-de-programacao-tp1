#Faça um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste. O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%.

salarioInicial = float(input("Insira seu salário aqui: "))
aumento = float(input("Insira seu reajuste aqui: "))
salarioNovo = salarioInicial + (salarioInicial * aumento/100)

print("Seu novo salário é:", salarioNovo)