# Scapy_RandomPaketSender

This Script requires [Scapy](https://github.com/secdev/scapy) for sending randomly 1.000 ARP, TCP, Beacon Frame or ICMP Pakets in the air.


## Execution

Open up your shell and type	`python scapy_randompaketsender.py`

Notice that you have to set your wireless antenna into monitor mode. One way to do this is

```
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor
```

or through airmon-ng

`airmon-ng start wlan0`

## Change settings
You can change some addresses and of course the name of your interface, which you use for sending the pakets. In this case, the wireless antenna is listed as wlan0 respectively wlan0mon in monitor mode.
```python
#Settings
Beacon_SSID = 'Fake_Beacon'   		#network name
interface = 'wlan0mon'         		#interface
broadcast = "ff:ff:ff:ff:ff:ff" 	#broadcast
bssid = "aa:aa:aa:aa:aa:aa"		#bssid
source = "111.111.111.111"		#source address
destination = "222.222.222.222"		#destination address
```

The number of pakets can be customized in line 16.

``python
for i in range(0,1000):
``

The payload of the ICMP Paket, both the length and the content, is also randomly generated with
```python
def random_data(size=randint(1, 1000), chars=string.ascii_uppercase + string.digits):
			return ''.join(random.choice(chars) for _ in range(size))
```

(borrowed from the User [Ignacio Vazquez-Abrams at stackoverflow](https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python)