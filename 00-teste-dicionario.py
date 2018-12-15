import psutil

dic_interfaces = psutil.net_if_addrs()
print(dic_interfaces["wlan0"][0].address)
