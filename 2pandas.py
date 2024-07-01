import seaborn as sb

# Загрузите датасет Tips из набора датасетов seaborn

df = sb.load_dataset('tips')

# Посмотрите на первые 5 строчек

print(df.head())

# Узнайте сколько всего строчек и колонок в данных

print(len(df))

# Проверьте есть ли пропуски в данных

print(df.isnull().sum())

# Посмотрите на распределение числовых признаков

print(df.describe())

# Найдите максимальное значение 'total_bill'

print(df['total_bill'].max())

# Найдите количество курящих людей

print(df['smoker'].value_counts())

# Узнайте какой средний 'total_bill' в зависимости от 'day'

print(df.groupby('day', observed=True)['total_bill'].mean())

# Отберите строчки с 'total_bill' больше медианы и узнайте какой средний 'tip' в зависимости от 'sex'

print(df[df['total_bill'] > df['total_bill'].median()].groupby('sex', observed=True)['tip'].mean())

# Преобразуйте признак 'smoker' в бинарный (0-No, 1-Yes)

df.replace({'smoker': 'Yes'}, 1, inplace=True)
df.replace({'smoker': 'No'}, 0, inplace=True)
print(df)
