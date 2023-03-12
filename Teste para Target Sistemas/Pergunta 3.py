#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Carregando os dados do faturamento mensal a partir de um arquivo JSON
with open('faturamento.json', 'r') as f:
    faturamento_mensal = json.load(f)

# Obtendo o menor valor de faturamento diário
menor_valor = min(faturamento_mensal)

# Obtendo o maior valor de faturamento diário
maior_valor = max(faturamento_mensal)

# Calculando a média mensal, ignorando os dias sem faturamento
dias_com_faturamento = [faturamento for faturamento in faturamento_mensal if faturamento > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contando o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for faturamento in faturamento_mensal if faturamento > media_mensal)

# Imprimindo os resultados
print(f"Menor valor de faturamento diário: {menor_valor}")
print(f"Maior valor de faturamento diário: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")