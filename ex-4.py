peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))

imc = peso/(altura**2)
print(f"seu peso eh: {imc}")

if imc < 18.5:
	print("vc esta abaixo do peso!")
    
elif imc < 25:
	print("vc esta no peso normal!")
    
elif imc >= 25:
	print("vc esta acima do peso!")
