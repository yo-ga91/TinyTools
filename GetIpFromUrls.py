import csv, socket
#import whois, time

#Format shortlist csv Ursl  Name;
#

def getip (s_name="google.ru"):
   try:
        ip = socket.gethostbyname(str(s_name))
        print(ip)
        return ip
   except Exception:
       #myDomenStatus=whois.whois(str(s_name))
       print('error')
       return 'error'
       #return myDomenStatus

AddrList=[]
file_shortlist=str(input('Enter file name URLs for test and extract IP:'))
file_LiveURLs=str(input('Enter file name for write IP good urls:'))
file_badurls=str(input('Enter file name for write bad urls:'))

with open(file_shortlist) as f:
    reader=csv.reader(f, dialect='excel',delimiter=';')
    for row in reader:
        AddrList.append(row[0])

print(AddrList)

handle = open(file_LiveURLs, "w")
BadUrls = open(file_badurls, "w")
handle.write("Name" + ";" + "Ip" + "\n")
BadUrls.write(("Name" + ";" + "Ip" + "\n"))
flag=0
for i in AddrList:

    #if flag => 28:
    #    time.sleep(40)
    #    flag = 1

    print(i)
    Ip=getip(i)
    if Ip=='error':
        print(i)
        BadUrls.write((i + ";" + str(Ip) + "\n"))
        flag+=1
    else:
        handle.write(i + ";" + str(Ip) + "\n")
        AddrList.remove(i)
BadUrls.close()
handle.close()
