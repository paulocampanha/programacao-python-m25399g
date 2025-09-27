# Nesse programa vamos estudar os operadores de atribuição. Esses 
# operadores são divididos em dois tipos, operador simples (=) e
# operadores compostos que combinam a operação com o operador 
# simples. Por exemplo (+=).

x = 15
print('x:',x)
x = x + 5  # resultado é 20
print('x:', x)

# operadores compostos
# Soma
x += 10     # equivalente a: x = x + 10
print('x:', x)
# Subtração
x -= 3      # equivalente a: x = x - 3
print('x:', x)
# Multiplicação
x *= 2      # equivalente a: x = x * 2
print('x:', x)
# Divisão
x /= 3      # equivalente a: x = x / 3
print('x:', x)
# Divisão inteira
x //= 2     # equivalente a: x = x // 2
print('x:', x)
# Potência
x **= 5     # equivalente a: x = x ** 5
print('x:', x)
# Modulo
x %= 2      # equivalente a: x = x % 2
print('x:', x)