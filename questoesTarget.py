#QUESTAO 2
def fibonacci(num):
  fibon = [0,1]
  i = 0
  while(num != fibon[i]):
    if(num < fibon[i]):
      return False
    else:
      x = len(fibon)
      f = fibon[x-2] + fibon[x-1]
      fibon.append(f)
      i +=1
  return True

fib = fibonacci(14)
if(fib):
  print("O numero esta na sequencia de fibonacci")
else:
  print("O numero nao pertence a sequencia de fibonacci")



#QUESTAO 3
import json
import pandas as pd

# r => leitura de dados do arquivo importado dados.json
with open("dados.json", "r") as arquivo:
      vet_fatur = json.load(arquivo)

dt = pd.json_normalize(vet_fatur)

def menorValor(distri):
  lowerIncome = 99999999
  stopPoint = len(distri)
  index = -1
  for i in range(stopPoint):
    if(distri[i] < lowerIncome and distri[i] != 0):
      lowerIncome = distri[i]
      index = i
  return [lowerIncome , index+1]

def maiorValor(distri):
  BIncome = -1
  stopPoint = len(distri)
  index = -1
  for i in range(stopPoint):
    if(distri[i] > BIncome and distri[i] != 0):
      BIncome = distri[i]
      index = i
  return [BIncome , index+1]

def mediaSup(distri):
  numDias = 0
  media = 0
  stopPoint = len(distri)
  dTrabalhados = 0
  for i in range(stopPoint):
    if(distri[i] != 0):
      media += distri[i]
      dTrabalhados += 1
  media /= dTrabalhados
  for j in range(stopPoint):
    if(distri[j] > media):
      numDias += 1
  return numDias

x = menorValor(dt['valor'])
y = maiorValor(dt['valor'])
z = mediaSup(dt['valor'])

print("Menor valor de faturamento:", x[0], "(dia:", x[1], ")")
print("Maior valor de faturamento:", y[0], "(dia:", y[1], ")")
print("Quantidade de dias que faturaram mais que a media mensal:", z)




# QUESTAO 4
sp = 67_836.43
rj = 36_678.66
mg = 29_229.88
es = 27_165.48
outros = 19_849.53
totalMensal = sp + rj +mg +es + outros
def calculoPercentual(estado, total):
  return round(((estado / total) * 100), 3)
print(calculoPercentual(sp, totalMensal))


#QUESTAO 5
def inversaoStr(palav):
  inv = []
  tam = len(palav) -1
  while(tam >= 0):
    inv.append(palav[tam])
    tam -= 1
  return inv

print(inversaoStr(input("insira uma palavra para ser invertida: ")))
