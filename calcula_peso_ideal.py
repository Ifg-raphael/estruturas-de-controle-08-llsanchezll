# Sua solução aqui
H = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo (M/F): ")
if sexo == "M": #sexo == "M"
    peso_ideal = (72.7 * H) - 58   
else: # sexo == "F"
    peso_ideal = (62.1 * H) - 44.7

print(f"Seu peso ideal e: {peso_ideal:.2f} ")