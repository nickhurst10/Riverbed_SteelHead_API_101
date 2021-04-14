"""
This is a Steelhead API 101 script, with the goal of showing the basics required to do an API calls to a Riverbed SteelHead.
If you have any questions please reach out to me
"""
__author__ = "Nick Hurst nhurst@riverbed.com"

import requests
import json
import time


#Your SteelHead mgmt IP address
device_ip = '192.168.111.119'

#initial post url to get Bearer token
url = "https://"+device_ip+"/api/common/1.0/oauth/token?Content-type=application/x-www-form-urlencoded&Accept=application/json"

#You'll need to create an access code from the steelhead, Administration -> Security -> REST API Access
#https://{steelhead_ip_addr}/mgmt/gui?p=setupRESTInterface
#this access code is reqired to get a Bearer Token
access_code = "eyJhdWQiOiAiaHR0cHM6Ly8xNDItTEFCL2FwaS9jb21tb24vMS4wL3Rva2VuIiwgImlzcyI6ICJodHRwczovLzE0Mi1MQUIiLCAicHJuIjogImFkbWluIiwgImp0aSI6ICIxMTE4ZDdlNi03Mjg5LTRmNmQtODNkYS0yZjI3ZTUwYzkzZTciLCAiZXhwIjogIjAiLCAiaWF0IjogIjE1OTMxMDY3MDMifQ=="

#with access code create API request payload
payload = 'grant_type=access_code&assertion=eyJhbGciOiJub25lIn0K.'+access_code+'.&state=state_string'

#Post request... Verify false, is due to not trusting the self signed cert of the SteelHead
response = requests.request("POST", url, data = payload,verify=False)

#get response in json format
json_response = response.json()

#print out response in a more readable format
print(json.dumps(json_response, indent = 6, sort_keys=True))

#create the API header using the Bearer Token for authentication and authorization
#Plus insuring the responce is a json formate.
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+json_response["access_token"],
}

#open a file which hold the current API call as of May/2020 and put into a list
#see https://support.riverbed.com/apis/_products/SteelHead/index.html
with open ("steelhead_API_list.txt", "r") as myfile:
    url_list=myfile.read().splitlines()

# loop_count is for naming the files for each output of an API call
loop_count = 1

#loop through list of URL's
for url_feed in url_list:
	#using the time library to pause one second before each call, to insure the Steelhead isn't overlaoded with requests
	time.sleep(1)
	#create the url for query
	url = 'https://'+device_ip+url_feed
	#GET request...
	response = requests.get(url, headers=headers, verify=False)
	#get responcs in json format
	data_info = (response.json())
	#create file name for file
	js_file_name = "json_file_"+str(loop_count)+".txt"
	
	print (data_info)
	#create file with name created above, remember if file already exist in the dir, then it will be over writen
	file2 = open(js_file_name,"w")
	json.dump(data_info,file2)
	file2.close()
	
	#increment loop count
	loop_count += 1
