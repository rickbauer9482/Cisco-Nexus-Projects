import requests
import json
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('XXXXXXX', 'YYYYYYY')
myheaders = {'Content-Type': 'application/json'}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show version",
        "output_format": "json"
  }
}

def main():

    with open('nexus-ip-list.txt') as iplist:
        for cnt, ip in enumerate(iplist):
            iptext=ip.strip('\n')
            #print("IP{}: {} ".format(cnt, iptext))
            url="http://" + iptext + "/ins"
            # print url
            response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=auth)

            #for key in response.keys():
            #     print "response includes", key
            # print 'Status Code: ' + str(response.status_code)

            rx_object = json.loads(response.text)

            # print json.dumps(rx_object, indent=4)

            simple = rx_object['ins_api']['outputs']['output']['body']

            print ''
            print 'Hostname: {host_name}'.format(**simple)
            print 'Chassis ID: {chassis_id}'.format(**simple)
            print 'NXOS Version: {kickstart_ver_str}'.format(**simple)
            #print 'Uptime dd:hrs:min:sec: ', simple['kern_uptm_days'], ':', simple['kern_uptm_hrs'], ':', simple['kern_uptm_mins'], ':', simple['kern_uptm_secs']
            print 'Up Time: {kern_uptm_days} days {kern_uptm_hrs} hrs {kern_uptm_mins} mins {kern_uptm_secs} secs'.format(**simple)
            print 'Last Reboot Reason: {rr_reason}'.format(**simple)
        
if __name__ == "__main__":
   main()
