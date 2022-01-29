import time
from datetime import datetime as dt
#current  time format month, day, hour, minutes, seconds and macroseconds.


Linux_host = '/etc/hosts'
MacOs_host = '/private/etc/hosts'
host = r"C:\Windows\System32\drivers\etc\hosts"
temp_host ="hosts"
redirect = '127.0.0.1'

website_list = ["www.instagram.com", "instagram.com"]

# while loop does is it execute an action very fast.
#def block_websites(start_hour , end_hour):
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,9)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        #each iteration you apply a conditional that says if a list item in content where content Is a text you have from the host file.
        #So if that item is in the content then don't do anything otherwise add that item in the host file.
        #We have methods to write content, methods to append content in that file but not to delete. so we need to
        print("don't sneak out, Do the work ....") 
        with open (host, 'r+') as file:
           content = file.read()
           for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')
        
    else:
        with open(host, 'r+') as file:
                content = file.readlines()
                #Replace the pointer just before the first character of the file content.
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                #deletes the content of the file from the current point and downwards
                file.truncate()
        print("relax ....")        
    time.sleep(3) #printed every 3 seconds.