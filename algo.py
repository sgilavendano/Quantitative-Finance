import requests
import quandl as q
import pandas as pd
import matplotlib.pyplot as plt

q.ApiConfig.api_key = 'r6sJbbi5zmcb38jP4jJr'

mydata = q.get("EIA/PET_RWTC_D")
print(mydata)