print("QUESTÃO 1")
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K
    
print('Valor da varíavel é: ', SOMA)

print('\n================================================================================================\n')

print("QUESTÃO 2")
def fibonacci(n):
  if n <= 1:
    return [0] * n
  else:
    fib_seq = [0, 1]
    while len(fib_seq) < n + 1:
      next_num = fib_seq[-1] + fib_seq[-2]
      fib_seq.append(next_num)
    return fib_seq

def main():
  numero = int(input("Digite um número: "))
  fib_seq = fibonacci(numero)
  if numero in fib_seq:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
  else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()

print('\n================================================================================================\n')

print("QUESTÃO 3")
print("RESPOSTA: 9, 128, 49, 100, 13, 200")
#1, 3, 5, 7, ___ -> 9

#2, 4, 8, 16, 32, 64, ____ -> 128

#0, 1, 4, 9, 16, 25, 36, ____ -> 49

#4, 16, 36, 64, ____ -> 100 

#1, 1, 2, 3, 5, 8, ____ -> 13

#2,10, 12, 16, 17, 18, 19, ____ -> 200

print('\n================================================================================================\n')

print("QUESTÃO 4")
print('Ligo o 1° interruptor por 5 minutos e desligo, não ligo o 2° interruptor e ligo o 3° interruptor!') 
print('A lampada que estiver acesa, é o 3° interruptor') 
print('A lampada que estiver desligada e fria, é o 2° interruptor')
print('A lampada que estiver desligada e quente, é o 1° interruptor') 

print('\n================================================================================================\n')

print("QUESTÃO 5")
def inverter_string(texto):
  return texto[::-1]

texto = "Olá, mundo!"
texto_invertido = inverter_string(texto)
print(texto_invertido) 