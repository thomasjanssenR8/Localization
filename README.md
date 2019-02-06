# Wi-Fi localization

##Introduction
With LPWAN technologies such as Sigfox, LoRaWAN or NB-IoT, we can locate Internet of Things (IoT) devices on a very 
large scale. In order to improve the accuracy of this localization, Wi-Fi networks can be used. By scanning the environment
for available Wi-Fi access points (APs), we can estimate the location by sending HTTP requests to databases that contain
the location of many access points worldwide. In this project, we use the [WiGLE](https://wigle.net/) and [LocationAPI](http://locationapi.org/) databases.
The first one contains the most APs worldwide, while the latter contains the most APs in Belgium. Important to note is 
that there is no need to connect to any Wi-Fi network used to locate a mobile device. Typically, the available SSIDs 
(the names of the network) or BSSIDs (the unique MAC address of an access point) are sent via an LPWAN network to a 
backend server. Then, that server performs the HTTP requests to the location databases. For this project, only 2 access
points were requests, because we wanted to reduce power consumption. However, if power consumption is not an issue, all
available BSSIDs can be requested. Note that there is a daily limit on the amount of requests one can perform to the
databases. If you want to request more BSSIDs, you can upgrade your account at a cost.


##Hardware
For this experiment, we used a Windows laptop to perform measurements in outdoor environments. Note that this mobile device
can easily be replaced by, for example, a small Raspberry Pi with a Wi-Fi chip. The BSSIDs of access points in the vicinity
are stored on the device. Afterwards, this data is copied to a server and included in the request in order to estimate the locations.
As mentioned earlier, this data can be sent through LPWAN networks, but the focus in this research was on the location accuracy
and not on the communication aspect. 

In order to have ground through data, a GPS was used. On every measurement location, the GPS coordinates were stored,
together with the available BSSIDs.

##Software
Below is a quick overview of the Python 3 scripts that were used to perform the measurements. All [data](data) is stored in Excel sheets.
* **_main_bssid.py_** - Manually collect the available BSSIDs and perform the requests to the WiGLE database. _Please change the account name and API token to your own name and token!_
* **_bssid_collect.py_** - Automatically scan the available Wi-Fi networks and save the BSSIDs. Note that this part is specifically made for Windows, but it should be easy to find the correct command to perform this on another OS.
* **_bssid_request.py_** - Request the stored BSSIDs to the WiGLE database and collect the estimated coordinates from the response. _Please change the account name and API token to your own name and token!_
* **_bssid_calcualte.py_** - Process the collected and requested data from the WiGLE database. First, create all possible combinations of 2 BSSIDs. Second, calculate the mean coordinate. Third, calculate the location estimation error and finally, plot a heatmap.
* **_locationAPI_with_rssi.py_** - Request the collected BSSIDs and RSSI values to the LocationAPI database and process the data in a similar way as we did with the WiGLE database. _Note that with the LocationAPI database, you need to send at least 2 BSSIDs to get a location estimate._
* **_locationAPI_without_rssi.py_** - Request the collected BSSIDs to the locationAPI database and process the data in a similar way as we did with the WiGLE database.
* **_chance_of_corrupt_bssid.py_** - Calculate the chance of a corrupt BSSID in the response. With 'corrupt', we mean that the access point is moved to a different location and this has not been updated in the database yet. Another problem can be MAC address spoofers. Of course, these responses could be filtered out.

##Localization accuracy
An article is published on the accuracy of Wi-Fi fingerprinting in LPWAN using only 2 BSSIDs. In this research, we found that when sending the 2 BSSIDs with the highest RSSI, an mean error of 46 en 93 meters can be achieved for the LocationAPI and WIGLE databases, respectively. The chance of having an access point match in the databases is around 87%. See https://www.mdpi.com/2076-3417/7/9/936.

##Author
If you have any questions or remarks, please feel free to contact the author:

**Thomas Janssen** - _thomas.janssen@uantwerpen.be_