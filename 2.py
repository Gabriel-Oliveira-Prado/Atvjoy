def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    else:
        return 0

print(calculadora(10, 5, 1))
print(calculadora(10, 5, 2))
print(calculadora(10, 5, 3))
print(calculadora(10, 5, 4))
print(calculadora(10, 5, 5))
