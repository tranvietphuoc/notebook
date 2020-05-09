import pandas as pd
import numpy as np
import geopandas

dates = pd.date_range('20191201', periods=6)
# create df
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('abcd'))

# create df by passing a dictionary
d = {
    'A': 1,
    'B': pd.Timestamp('20191201'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(['test','train', 'test', 'train']),
    'F': 'foo'
}
df1 = pd.DataFrame(d)
# df1.dtypes
df1.T.T



import pandas as pd
import googlemaps
import requests
from itertools import tee



print(dir(googlemaps))
# API_KEY = 'AIzaSyB0GObgzvHHYDNDGMjexV9NyiOsZC9gKS4'
# maps = googlemaps.Client(API_KEY)
# address = "so 4 Cuu Long, phuong 2, tan binh, Ho Chi Minh"
# print(maps.geocode(address))

# # use pairwise function to iterate through two consecutive rows in dataframe

# def pairwise(iterable):
#     a, b = tee(iterable)
#     next(b, None)
#     return zip(a, b)

# # read data from csv file

# df = pd.read_csv('filenam.file', sep=';')

# # make two dataframe columns to store lat and long

# df['Lat'] = googlemaps.



