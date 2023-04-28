import pandas as pd
from pytrends.request import TrendReq
trends = TrendReq()
#If the code has an error, go to the terminal and install pandas and pytrends 

trends.build_payload(kw_list = ["Woman Life Freedom"])
dt = trends.interest_by_region()
dt = dt.sort_values(by = "Woman Life Freedom",ascending = False)
dt = dt.head(20)
print(dt)

