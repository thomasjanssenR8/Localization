data = '{"resultCount":1,"last":1,"success":true,"results":[{"trilat":51.22378540,"trilong":4.40892172,"ssid":"UAntwerpen","qos":7,"transid":"20120419-00187","firsttime":"2012-04-19T23:05:18.000Z","lasttime":"2015-02-22T11:26:18.000Z","lastupdt":"2015-02-22T09:28:02.000Z","netid":"00:0B:86:26:79:C5","name":null,"type":"infra","comment":null,"wep":"2","channel":6,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false}],"first":1}'

latitude_index = data.find("trilat") + 8
latitude = data[latitude_index: (latitude_index+11)]
print(latitude)

longitude_index = data.find("trilong") + 9
longitude = data[longitude_index: (longitude_index+10)]
print(longitude)
