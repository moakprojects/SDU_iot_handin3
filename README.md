# SDU_iot_handin3
These are the source codes of the third assignment of the iot course at Sysddansk Universitet

src/main.py - to run on a Lopy4 device (wlan connection, http request)
src/al.php - PHP webserver which receive the hhtp request from Lopy4 and send it to a remote database
src/handler.py - read the exported csv file from the database and create a chart to show frequency
src/charts.py - read the exported csv file and plot the measured values
