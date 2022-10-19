import pkg_resources
import pandas as pd

def load_power():
 
    stream = pkg_resources.resource_stream(__name__, r'data\new_household_power_consumption.csv')
    return pd.read_csv(stream,encoding='latin-1')
target=load_power().columns[-1]
data=load_power().columns[:-1]
