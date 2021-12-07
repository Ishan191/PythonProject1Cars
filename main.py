import pandas as pd
car = pd.read_csv(r"C:\Users\Ishan\Project1Cars\CarsData.csv")
car.head()
car.shape
car.isnull().sum()
car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)
car['Make'].value_counts() # Make of the Cars
car[car['Origin'].isin(['Asia','Europe'])]  # Cars With Origin in Europe And Asia
car[~(car['Weight'] > 4000)]  # Cars removed with weight greater than 4000
car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)
