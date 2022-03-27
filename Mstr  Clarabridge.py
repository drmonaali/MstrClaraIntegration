from mstrio.connection import Connection
from getpass import getpass
import pandas as pd

import requests
import os
import json

# Create a cleaned json response
def jprint(obj):
 text = json.dumps(obj, sort_keys=True, indent=4)
 print(text)
# Define variables
access_token = "YourKey"
url = "https://api.engagor.com/xxxx/dashboards/component/xxxx/xxxxx/"
headers = {'Authorization': 'Bearer '+'YourKey'}


# Make get request
response = requests.request("GET", url, headers=headers)
response_data = response.json()
#print(response_data)

nrepsonse = pd.DataFrame(response_data['response'][0]['data']['timeline mentions_compared_by_sentiment']['data'])


tresponse= pd.DataFrame.transpose(nrepsonse)
#sentiments_df=  pd.DataFrame(tresponse,columns=["", "Date", "Neutral", "Positive","Negative"])
base_url = "MStrServerURL"
mstr_username = "mona.ali"
mstr_password = getpass("Password: ")
project_id = "YourProjectID"
conn = Connection(base_url, mstr_username, mstr_password, project_id=project_id)

conn.connect()

tresponse['Positive'] = tresponse['Positive'].astype('int')
tresponse['Negative'] = tresponse['Negative'].astype('int')
tresponse['Neutral'] = tresponse['Neutral'].astype('int')


from mstrio.project_objects.datasets import SuperCube
ds = SuperCube(connection=conn, name="Test XXX")
ds.add_table(name="Sentiments", data_frame=tresponse, update_policy="replace")
ds.create()


conn.close()


