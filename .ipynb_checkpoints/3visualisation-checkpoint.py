import seaborn as sb
import matplotlib.pyplot as plt
import seaborn as sns

df = sb.load_dataset('tips')

# # Постройте гистограмму распределения признака 'total_bill'

sns.displot(df['total_bill'])
plt.show()

# # Постройте scatterplot, представляющий взаимосвязь между признаками 'total_bill' и 'tip'

sns.scatterplot(data=df, x='total_bill', y='tip')
plt.show()

# # Постройте pairplot

sns.pairplot(df)
plt.show()

# # Постройте график взаимосвязи между признаками 'total_bill' и 'day'

sns.scatterplot(data=df, x='total_bill', y='day')
plt.show()

# # Постройте две гистограммы распределения признака 'tip' в зависимости от категорий 'time'

print(df['time'].value_counts())
sns.countplot(x='time', data=df)
plt.show()

# # Постройте два графика scatterplot,
# # представляющих взаимосвязь между признаками 'total_bill' и 'tip'
# # один для Male, другой для Female
# # и раскрасьте точки в зависимоти от признака 'smoker'

plt.subplot(1, 2, 1)
sns.scatterplot(data=df[((df['sex'] == 'Male') & (df['smoker'] == 'Yes'))], x='total_bill', y='tip', color='green')
sns.scatterplot(data=df[((df['sex'] == 'Male') & (df['smoker'] == 'No'))], x='total_bill', y='tip', color='red')
plt.subplot(1, 2, 2)
sns.scatterplot(data=df[((df['sex'] == 'Female') & (df['smoker'] == 'Yes'))], x='total_bill', y='tip', color='green')
sns.scatterplot(data=df[((df['sex'] == 'Female') & (df['smoker'] == 'No'))], x='total_bill', y='tip', color='red')
plt.show()

# Сделайте выводы по анализу датасета и построенным графикам. По желанию можете продолжить анализ данных и также отразить это в выводах.

