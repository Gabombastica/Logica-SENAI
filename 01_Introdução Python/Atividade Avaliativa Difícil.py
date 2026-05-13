#  Atividade Avaliativa Difícil custo e combustível

distancia_total = 800
distancia_percorrida = 90
gasto_total_km = 7
tanque_atual = 10
preco_combustivel = 6.90
km_falta = distancia_total - distancia_percorrida
litros_necessarios = km_falta / 7
litro_final = litros_necessarios - tanque_atual
custo_final = litro_final * preco_combustivel
print(f"Para realizar uma viagem com {distancia_total} km, será necessário utilizar {litro_final} litros e será necessário gastar R${custo_final} reais.")