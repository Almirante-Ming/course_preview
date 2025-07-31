import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Consumo (kWh)': [445, 430, 398, 385, 392, 370, 380, 362, 355, 360, 370, 442]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Mês'], df['Consumo (kWh)'], color='skyblue')
plt.xlabel('Mês')
plt.ylabel('Consumo (kWh)')
plt.title('Consumo Mensal de Energia Elétrica da Família Martins')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_barras_consumo_mensal.png')
plt.close()


df['Percentual'] = (df['Consumo (kWh)'] / df['Consumo (kWh)'].sum()) * 100

plt.figure(figsize=(10, 10))
plt.pie(df['Percentual'], labels=df['Mês'], autopct='%1.1f%%', startangle=90,
        pctdistance=0.85, wedgeprops={'edgecolor': 'black'})
plt.title('Distribuição Relativa do Consumo Mensal de Energia Elétrica')
plt.axis('equal')
plt.tight_layout()
plt.savefig('grafico_pizza_consumo_mensal.png')
plt.close()

print("Gráficos 'grafico_barras_consumo_mensal.png' e 'grafico_pizza_consumo_mensal.png' gerados com sucesso!")