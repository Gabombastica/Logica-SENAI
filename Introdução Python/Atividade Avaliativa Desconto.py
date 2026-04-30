# Atividade Avaliativa Desconto

nome_produto = str(input("Olá, seja bem-vindo ao Supermercado Sakashita, digite o nome do produto que você deseja: "))
preco_produto = float(input("Agora, digite o preço atual desse produto: "))
desconto = preco_produto / 20
preco_produto_final = preco_produto - desconto
print(f"O preço final do seu produto com o valor do desconto aplicado será de R${preco_produto_final} reais.")
print(f"Seu produto teve o preço reduzido em 5%, ou seja, R${desconto} reais.")
print(f"Muito obrigada pela sua compra cliente! Volte sempre!")