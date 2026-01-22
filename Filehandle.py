# file handling
import pandas as pd
df = pd.read_csv('Test.csv')
# df.loc[df['Last Name'] == 'Magwood','Age'] = 63
# df['Age_Category'] = df['Age'].apply(lambda x: 'Senior' if x > 60 else 'Adult')
df = df.drop(['Phone 1','Phone 2','Last Name','Subscription Date'], axis=1)
df.to_csv('Test.csv', index=False) 
print(df.head())
# print(df.loc[df['Age'] == df['Age'].max()])