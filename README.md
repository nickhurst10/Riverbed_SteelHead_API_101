# Riverbed_SteelHead_API_101

This is a Steelhead API 101 script, with the goal of showing the basics required to do an API GET requests to a Riverbed SteelHead.

The script is writen for Python3.

To work in your environment, update the device_ip and access_code variables in the script with the relevant information.

To run on your machine you’ll require both the script file and “steelhead_API_list.txt” file.

The “steelhead_API_list.txt” file, lists all the current GET requests as of May 2020.

Before the script can work, you’ll need to enable Rest API Access and create an access code.

https://{steelhead_ip_addr}/mgmt/gui?p=setupRESTInterface

The access code is used to request a Bearer token

This script should only be used in a test environment.

If you have any questions please reach out to me
