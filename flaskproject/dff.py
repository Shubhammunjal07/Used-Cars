import numpy as np
import pandas as pd

data = pd.read_csv("../used_cars.csv", index_col = 0)

def get_year():
    y = []
    y = data['year'].unique()
    y = pd.Series(list(y))
    return y

def get_company():
    comp = []
    comp = data['company'].unique()
    comp = pd.Series(list(map(lambda x: x.strip(), comp)))
    return comp

def get_carsname():
    car = []
    car = data['cars_name'].unique()
    car = pd.Series(list(map(lambda x: x.strip(), car)))
    return car

def get_owner():
    o = []
    o = data['owner'].unique()
    o = pd.Series(list(map(lambda x: x.strip(), o)))
    return o

def get_sellertype():
    seller = []
    seller = data['seller_type'].unique()
    seller = pd.Series(list(map(lambda x: x.strip(), seller)))
    return seller

def get_fuel():
    f = []
    f = data['fuel'].unique()
    f = pd.Series(list(map(lambda x: x.strip(), f)))
    return f

def get_transmission():
    trans = []
    trans = data['transmission'].unique()
    f = pd.Series(list(map(lambda x: x.strip(), trans)))
    return trans




