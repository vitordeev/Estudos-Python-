"""11) Receba o preço de um produto e um valor de desconto (ex:
10%). Exiba o novo preço do produto com o desconto aplicado."""
produto = float(input("Digite o valor do produto: "))
porcetagem = int(input("Digite o valor da porcetagem: "))
cal01 =  produto - (produto * porcetagem ) / 100 
print(f"o valor final com o descont aplicado e de {cal01}")