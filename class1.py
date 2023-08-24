print("tá rodando, calma") # indicar quando está rodando
peso = float(input("digite seu peso em (kg):"))
altura = float(input("digite sua altura em (m):"))
IMC = peso/(altura**2)

print("seu IMC é:", IMC)
print("estou muito abaixo do peso?", IMC<17) #indicar a entrada
print("estou abaixo do peso?", IMC>=17 and IMC<18.5)

#IF condicionais
if IMC<17:
    print("situação: muito abaixo do peso")
elif IMC>=17 and IMC<18.5:
    print("situação: abaixo do peso")
else:
    print ("situação: IMC normal")
