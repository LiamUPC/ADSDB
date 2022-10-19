import pandas as pd
from dateutil import rrule
from datetime import datetime as dt

# %% [markdown]
# <h2>Crimes Dataset</h2>
# 
# Import to a dataframe the files for crimes between the start and end month

# %%
startMonthCrimes = dt(year=2020, month=6, day=1) 
endMonthCrimes   = dt(year=2021, month=6, day=1)
startMonthPrices = dt(year=2021, month=6, day=1)
startMonthPrices = startMonthPrices.strftime('%Y-%m')
endMonthPrices   = dt(year=2022, month=4, day=1)
endMonthPrices = endMonthPrices.strftime('%Y-%m')

crimes = pd.DataFrame()
for dt in rrule.rrule(rrule.MONTHLY, dtstart=startMonthCrimes, until=endMonthCrimes):
  month = str(dt)[0:7]
  crimes = pd.concat([crimes, pd.read_csv("../../data/landing/temporal/crimes/" + month + "-lincolnshire-street.csv")], axis=0)

print(crimes.shape)
# %% [markdown]
# <h2>Saving Crimes To Persistent</h2>
# 
# We will use a dataSourceName-startMonth-endMonth-timestamp naming convention for both the price and crimes datasets.

# %%
ext = startMonthCrimes.strftime('%Y-%m')+"-"+endMonthCrimes.strftime('%Y-%m')+"-"+dt.now().strftime("%Y-%m-%d-%H_%M_%S")
crimes.to_csv("../../data/landing/persistent/crimes/crimes-"+ext+".csv", index=False)

# %% [markdown]
# <h2>Prices Dataset</h2>
# 
# Import to a dataframe the instances for prices between the start and end month

# %%
prices = pd.read_csv("../../data/landing/temporal/houseprices.csv")


prices['Month'] = pd.to_datetime(prices['Month']).dt.strftime('%Y-%m')

prices = prices.loc[(prices['Month'] >= startMonthPrices) & (prices['Month'] <= endMonthPrices)]

# %% [markdown]
# <h2>Saving Prices To Persistent</h2>
# 
# We will use a dataSourceName-startMonth-endMonth-timestamp naming convention for both the price and crimes datasets.

# %%
ext = startMonthPrices+"-"+endMonthPrices+"-"+dt.now().strftime("%Y-%m-%d-%H_%M_%S")
prices.to_csv("../../data/landing/persistent/prices/prices-"+ext+".csv", index=False)