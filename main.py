import pandas as pd
df=pd.read_csv("movies.csv")
print("First 10 rows:")
print(df.head(10))
print("\nMovies per year:")
print(df['Year'].value_counts().sort_index())
print("\nTop 5 Movies:")
print(df.sort_values(by='Rating', ascending=False).head(5))
df['Decade'] = (df['Year']//10)*10
print("\nAverage rating per decade:")
print(df.groupby('Decade')['Rating'].mean())
print("\nMost common genre:")
print(df['Genre'].value_counts().head(1))