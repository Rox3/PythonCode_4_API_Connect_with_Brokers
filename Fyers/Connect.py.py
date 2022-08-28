from fyers_api.Websocket import ws
from fyers_api import fyersModel
from fyers_api import accessToken

      



app_id=open('StrategyADX/Fyers_app_id.txt','r').read()
app_secret=open('StrategyADX/Fyers_app_secret.txt','r').read()
 
redirect_url='http://fyers.trade'
 
### 1 if u have already written access token, access token is having 24 hr life span
access_token=open('StrategyADX/Fyers_generatToken.txt','r').read()
 
 
 
                                        # quote_details=kite.quote('NSE:RELIANCE')
                                        # print(quote_details)
 
 
### 2if u are opening the access data for the first time in the day
# session=accessToken.SessionModel(client_id=app_id,secret_key=app_secret,redirect_uri=redirect_url,response_type='code', grant_type='authorization_code')
# response=session.generate_authcode()
# print("your login url is :")
# print(response)
 
# print("\n")
# print("\n")
 
# auth_code='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NTY5OTQ5MjksImV4cCI6MTY1NzAyNDkyOSwibmJmIjoxNjU2OTk0MzI5LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYWTAyNDQ0Iiwibm9uY2UiOiIiLCJhcHBfaWQiOiIxVVVZWEdMVU9IIiwidXVpZCI6ImJlMGI5NzI1YWE1MDRkNjI4ZjBiNWRhODgxNDIwNGU5IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.lpAo76Ni_wHgqkgzIx5MhMu1m4XxEUAKaw6IXqyS-2I'
# session.set_token(auth_code)
# response=session.generate_token()
# print("\n")
# print("\n")
# print("your access token is :")
# access_token=response['access_token']
# print(access_token)
 
# with open('StrategyADX/Fyers_generatToken.txt','w') as ak:
#     ak.write(response['access_token'])
 
 
 
 
#Creating fyers model to access all the modules
fyers = fyersModel.FyersModel(client_id=app_id, token=access_token,log_path="/")



###################################################################################
  
            


    
