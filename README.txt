#################################
Scripted By Hejaze
trapperx.1@gmail.com
v1 working with nmap without args
#################################

** worked and tested with python 3 only
-------------------------------------
1 - make sure you have a mysql database with a table contains subdomains records
2 - make sure that mysql database service is running
3 - make sure nmap tool is installed and tested
4 - install required python packages
    pip install -r requirements.txt
    pip3 install -r requirements.txt
5 - provide all access credentials in config.py
6 - run nmap_runner.py
    python nmap.runner.py
