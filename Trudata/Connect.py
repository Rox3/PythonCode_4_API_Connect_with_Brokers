from truedata_ws.websocket.TD import TD
from copy import deepcopy
import pandas as pd
from datetime import date
import time
username ='*******'
password ='*********'
realtime_port = 8082

# live_port to be set to None in case subscribed only for Historical data 

td_app = TD(username, password, live_port=realtime_port, historical_api=False)

symbols = ['NIFTY22063015850CE']
barsize = 'tick'
# barsize = 'EOD'

print('Starting Real Time Feed.... ')
print(f'Port > {realtime_port}')

req_ids = td_app.start_live_data(symbols)
live_data_objs = {}
for req_id in req_ids:
    live_data_objs[req_id] = deepcopy(td_app.live_data[req_id])
    print(f'touchlinedata -> {td_app.touchline_data[req_id]}')

while True:
    for req_id in req_ids:
        if not td_app.live_data[req_id] == live_data_objs[req_id]:
            print(td_app.live_data[req_id])  # your code in the previous version had a  print(td_app.live_data[req_id]).__dict__ here.
            live_data_objs[req_id] = deepcopy(td_app.live_data[req_id])
