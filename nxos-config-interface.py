import requests
import json
from requests.auth import HTTPBasicAuth

def main():

  auth = HTTPBasicAuth('AAAAA', 'BBBBBB')
  #myheaders={'content-type':'application/json'}
  #url='http://XXX.XXX.XXX.XXX/ins'
  #payload={
   # "ins_api": {
   #   "version": "1.0",
   #   "type": "cli_conf",
   #   "chunk": "0",
   #   "sid": "1",
   #   "input": "config t ;interface eth1/1 ;description Configured by Python Script ;switchport ;exit",
   #   "output_format": "json"
   # }
 # }
  
  #response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=auth)

  #print 'Status Code: ' + str(response.status_code)

  myheaders={'content-type':'application/json'}
  url='http://XXX.XXX.XXX.XXX/ins'
  payload2={
    "ins_api": {
      "version": "1.0",
      "type": "cli_show",
      "chunk": "0",
      "sid": "1",
      "input": "show run interface eth1/1",
      "output_format": "json"
    }
  }
  
  response = requests.post(url,data=json.dumps(payload2), headers=myheaders,auth=auth)
  rx_object = json.loads(response.text)


  #print json.dumps(rx_object, indent=4)
  simple = rx_object['ins_api']['outputs']['output']['body']
  print simple

if __name__ == "__main__":
  main()
