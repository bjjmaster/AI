import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import time
from sklearn.metrics import mean_squared_error

df = pd.read_csv('C:\\Users\\max\\Desktop\\УЧЕБА\\датаметы\\autos.csv')
df = df.drop(['DateCreated', 'PostalCode', 'LastSeen', 'DateCrawled','NumberOfPictures'], axis=1)

pet = df['VehicleType'].unique()
pet = pet[1:]
med1 = df['Model'].dropna().unique()


def petrol1(row):

    FuelType = row['FuelType']
    VehicleType = row['VehicleType']

    if FuelType != FuelType:
        if VehicleType != VehicleType:
            return 'petrol'
        return petrol[VehicleType]
    return FuelType

def moodel1(row):
    VehicleType = row['VehicleType']
    Model = row['Model']

    try:
        if VehicleType != VehicleType:
            return mod[Model]
        return VehicleType
    except:
        return 'sedan'


petrol = {}
mod = {}
for i in pet:
    d = df.query('VehicleType == @i')
    m = d.pivot_table(index=['VehicleType', 'FuelType'], values='Model', aggfunc='count').sort_values(by='Model',
                                                                                                      ascending=False)
    petrol[i] = m.index[0][1]

for j in med1:
    try:
        dr = df.query('Model == @j').dropna().reset_index(drop=True)
        ma = dr.pivot_table(index='VehicleType', values='Model', aggfunc='count').sort_values(by='Model',
                                                                                              ascending=False)
        mod[j] = ma.index[0]
    except:
        continue

df['FuelType'] = df.apply(petrol1, axis=1)
df['VehicleType'] = df.apply(moodel1, axis=1)
df['Gearbox'] =  df['Gearbox'].fillna(method='backfill')
df['Repaired'] =  df['Repaired'].fillna('no')
df["Model"] = df["Model"].fillna('Unknown')

data_ohe = pd.get_dummies(df, drop_first=True)
features = data_ohe.drop(['Price'], axis=1)
target = data_ohe['Price']
feat_all, features_test, target_all, target_test = train_test_split(
    features,  target, test_size=0.2, random_state=42)

features_train, features_valid, target_train, target_valid = train_test_split(
    feat_all,  target_all, test_size=0.25, random_state=42)