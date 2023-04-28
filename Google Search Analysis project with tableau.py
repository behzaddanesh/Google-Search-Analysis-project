import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

trends.build_payload(kw_list = ["Woman Life Freedom"])
dt = trends.interest_by_region()
dt = dt.sort_values(by = "Woman Life Freedom",ascending = False)
dt = dt.head(20)  
print(dt)

dt.reset_index().plot(x="geoName",y="Woman Life Freedom",figsize = (10,5),kind = "bar")
plt.style.use('fivethirtyeight')
plt.show()

