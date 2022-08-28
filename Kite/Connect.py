# KiteTicker for Current data and KiteConnect for Historical data 

from kiteconnect import KiteTicker,KiteConnect
import pandas as pd
import numpy as np



from datetime import datetime,timedelta

if __name__=='__main__':
    api_key=open('api_key.txt','r').read()
    api_secret=open('api_secret.txt','r').read()

    
    kite=KiteConnect(api_key=api_key)

### 1 if u have already written access token, access token is having 24 hr life span
    access_token=open('access_token.txt','r').read()

    kite.set_access_token(access_token)



### 2if u are opening the access data for the first time in the day 

    # print(kite.login_url())
    # ### data =kite.generate_session("REQUEST TOKEN <<5 min life span>>",api_secret=api_secret)
    # data =kite.generate_session("kxYyW3v37VMKajpM8VasoNjwKjaxh4fP",api_secret=api_secret)
    # print(data['access_token'])
    # kite.set_access_token(data['access_token'])


    # with open('access_token.txt','w') as ak:
    #     ak.write(data['access_token'])

    

    ##Dates 

    from_date=datetime.strftime(datetime.now()-timedelta(10),'%Y-%m-%d')
    to_date=datetime.today().strftime('%Y-%m-%d')

    