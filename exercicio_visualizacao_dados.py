import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')

#Tratamento
print('Tipagem dos dados: \n', df.dtypes)
print('Quantidade de valores nulos:', df.isnull().sum())
df['Material'] = df['Material'].fillna('não informado')
df['Gênero'] = df['Gênero'].fillna('não informado')
df = df.fillna(0)
print('Quantidade de valores nulos:', df.isnull().sum().sum())

df['Marca'] = df['Marca'].str.title()
df['Material'] = df['Material'].str.title()
df['Temporada'] = df['Temporada'].str.title()

print(df.head(10).to_string())
print(df.tail(10).to_string())

#Gráfico de barras
x = df['Temporada'].value_counts().index
y = df['Temporada'].value_counts().values

plt.figure(figsize=(15, 8))
plt.bar(x, y, color='#60aa65')
plt.title('Temporada')
plt.xlabel('Vendas por Temporada')
plt.ylabel('Quantidade')
plt.xticks(rotation=50)
plt.show()

#Gráfico de pizza
plt.figure(figsize=(15,8))
plt.pie(y, labels=x, autopct='%.2f%%', startangle=90)
plt.title('Distribuição de Nível de Venda por Temporada')
plt.show()

#Gráfico Pairplot - Dispersão e Histograma
sns.pairplot(df[['Qtd_Vendidos_Cod', 'Preço', 'Marca_Cod']])
plt.show()

#Gráfico de Densidade - Quantidade de Vendas
plt.figure(figsize=(15,8))
sns.kdeplot(df['Qtd_Vendidos_Cod'], fill=True, color='#863e9c')
plt.title('Densidade de Vendas')
plt.xlabel('Quantidade de Vendas')
plt.show()

#Gráfico de Regressão
sns.regplot(x='Qtd_Vendidos_Cod', y='N_Avaliações', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Quantidade de Vendas por Avaliações')
plt.xlabel('Quantidade Vendas')
plt.ylabel('Avaliações')
plt.show()

#Mapa de Calor
corr = df[['Qtd_Vendidos_Cod', 'N_Avaliações']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Quantidade de Vendido e Avaliações')

plt.show()
