# Nesse programa vamos estudar algumas formas para impressão de
# dados usando a função print()

print('Olá, mundo!')        # saida Olá, mundo!
print("=" * 30)             # saida ==========================
print()                     # imprime linha em branco
print('Nome:' + 'Gaspar')
print('Numero:', 13)
# sep: Separador
print('Gaspar','Jorge','Anabela', sep='-')  
print(10, 15, 25, sep=' -> ')
# end: final do print
# 'end' tem como padrão a quebra de linha. 
# o caracter de que de linha é o 'n', usado com a '\'
print(5, end='...')
print(4, end='...')
print(3, end='...')
print(2, end='...')
print(1, end='...')
print("F O G O !!!")
print('=' * 30)

# Formatação de string para saidas do print
nome = "Gaspar"
idade = 18
altura = 1.75
 # f-string
print(f'O nome do aluno é {nome}. Ele tem {idade} anos e mede {altura} metros.')
mensagem = f'{nome} mede {altura} metros'
print(mensagem)
