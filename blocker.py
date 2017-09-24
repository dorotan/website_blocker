import time
from datetime import datetime as mytime

hosts_temp="hosts"
hosts_path =r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list = ["www.facebook.com","facebook.com", "gmail.com", "wp.pl", "www.wp.pl"]

while True:
    if mytime(mytime.now().year, mytime.now().month, mytime.now().day,16) < mytime.now() < mytime(mytime.now().year, mytime.now().month, mytime.now().day,22):
        print("Working hours")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+ "\n\t")
    else:
        with open(hosts_temp, "r+") as fiel:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun python hours...")
    time.sleep(5)