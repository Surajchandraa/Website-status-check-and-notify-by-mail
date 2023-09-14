import requests
import smtplib
import datetime as dt

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False
    return False


server= smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(user='',password='') #use here your gmail id and password[Node- password should be "Generated app password"]


links=[]

links.append("****      Website report    ****")
x=dt.datetime.now()
links.append(str(x))



website_url="http://103.154.2.116/~maxdevcallastro/call_astro/home" #enter your website url here 








try:
    with open('webcrash.txt', 'r') as status_file:
        status = status_file.read().strip()
except FileNotFoundError:
    status = 'up'

if status == 'up' and not check_website():
    print('Website is down. Sending email notification...')
    links.append("Website is down. ")
    formatted='\n\n'.join(links)
    server.sendmail(from_addr='',to_addrs='',msg=formatted)# Enter here your gamil and receiver's gmail
    # server.sendmail(from_addr='surajjosh7@gmail.com',to_addrs='Alok.trivedi@gmail.com',msg=formatted)
    print("mail sent")

    # Update status in the file
    with open('webcrash.txt', 'w') as status_file:
        status_file.write('down')
elif status == 'down' and check_website(website_url):
    print('Website is accessible again. Sending email notification...')
    links.append("Website is accessible again. ")
    formatted='\n\n'.join(links)
    server.sendmail(from_addr='',to_addrs='',msg=formatted)#Enter here your gmail and receiver's gmail


    print("mail sent")

    # Update status in the file
    with open('webcrash.txt', 'w') as status_file:
        status_file.write('up')
else:
    print('Website status remains unchanged.')
