import bs4, requests, smtplib
import simplejson as json
url="None"
message=" "
tweetArr=[]
avaliable=False


for i in range(1):     # Number of pages plus one 
    getPage = requests.get("https://www.freshercooker.in/category/courses/btech-be/internship/page/"+str(i)+"/")
    getPage.raise_for_status()
    menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
    n=menu.find_all("h3",{"class":["entry-title"]})
    
    for i in n:
        lol=(i.findChildren("a"))
        
        for link in lol:
            object = {
                "name":link.get('title'),
                "link":link.get('href')
            }
            message=message+json.dumps(object)+'\n'
            avaliable=True

    getPage = requests.get('https://www.offcampusjobs4u.com/category/internship/')
    getPage.raise_for_status()
    menu = bs4.BeautifulSoup(getPage.text,'html.parser')
    n=menu.find_all("h3",{"class":["entry-title"]})

    for i in n:
        lol=(i.findChildren("a"))
        
        for link in lol:
            object = {
                "name":link.get('title'),
                "link":link.get('href')
            }
            message=message+json.dumps(object)+'\n'
            avaliable=True

if avaliable == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.ehlo()
    conn.login('yourid', 'yourpassword')
    conn.sendmail('senderid','recieversid@gmail.com','Subject: Intern Notifier V1.0\n\nIntern Notifier V1.0'+'\n'+message)
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
else:
    print('Your favourite food is not available today.')

