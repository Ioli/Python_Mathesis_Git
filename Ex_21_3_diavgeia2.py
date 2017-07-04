# Project in Python 3.6.1 on Mathesis e-learning platform http://mathesis.cup.gr/
# June 2017 "Εκμάθηση Python 3.6.1 " με καθηγητή τον Νικόλαο Αβούρη του Πανεπιστημίου Πατρών 
# 21.3 Tελική εργασία: Ανάκτηση δεδομένων από τη diavgeia.gov.gr
# Πρότυπο λύσης της Νικολαΐδου Δήμητρα Χριστίνα (Ιόλη)

import re
import urllib.request
import urllib.error

arxes = {}

def rss_feed(url):
    '''
    Άνοιγμα του rss feed,
    :param url: η διεύθυνση του rss feed
    καλεί την συνάρτηση process_feed 
    η οποία επιλέγει και τυπώνει περιεχόμενο
    '''
    #σύμφωνα με την ανακοίνωση της διαύγειας τα rss feeds είναι στο ίδιο url/rss
    url += r"/rss" 
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode()        
        filename = rss_filename(url)
        with open(filename, "w", encoding="utf-8") as p:
            p.write(html)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.readline())
    except urllib.error.URLError as e:
        print(e)
        if hasattr(e, 'reason'):  # χωρίς σύνδεση ιντερνετ
            print('Αποτυχία σύνδεσης στον server')
            print('Αιτία: ', e.reason)
        print (0)
    else:
          process_feed(filename) 
       


def process_date(date):
    '''
    η συνάρτηση διαμορφώνει την ελληνική ημερομηνία του rss feed
    :param date:
    :return: η ελληνική ημερομηνία
    '''    
    months = {"01": "Ιαν", "02": "Φεβ", "03": "Μαρ", "04": "Απρ",
          "05": "Μαι", "06": "Ιουν", "07": "Ιουλ", "08": "Αυγ",
          "09": "Σεπ", "10": "Οκτ", "11": "Νοε", "12": "Δεκ"}
    d = date.split("Ημ/νια:&lt;/strong&gt; ")[-1][:10]  
    if re.search(r"[0-9]{2}/[0-9{2}/[0-9]{4}",d) :
        d = d.split("/")
        mhnas=' '+months[d[1]]+' '
        d[1]=months[d[1]]     
        return d
    else:
        print("xaxa",0000)
        #return date

def process_feed(filename):
    '''
    συνάρτηση που ανοίγει το αρχείο με το rss feed και 
    τυπώνει την ημερομηνία και τους τίτλους των αναρτήσεων που περιέχει
    '''
    print("process feed", filename)
    with open(filename, 'r', encoding = 'utf-8') as f:
        rss = f.read().replace("\n", " ")
        feeds = []
        items = re.findall(r"<item>(.*?)</item>",rss, re.MULTILINE | re.IGNORECASE)
        for item in items:
              if "" in item:
                title = re.findall(r"<title>(.*?)</title>",item, re.MULTILINE | re.IGNORECASE)
                if len(title)>0:
                    title = title[0]                    
                    print("ΤΙΤΛΟΣ:",title)
                descriptions = re.findall(r"<description>(.*?)</description>",item, re.MULTILINE | re.IGNORECASE)              
                if "Ημ/νια:" in item:
                      f_date=process_date(descriptions[0])                     
                      print("Ημ/νια:",f_date)                     
                else:
                        print("diavgeia:",description[0])
                        print("kenh description")

def search_arxes(arxh):
    '''
    αναζήτηση ονόματος Αρχής που ταιριάζουν τα κριτήρια του χρήστη
    '''
    l=[a for a in arxes if arxh.upper() in a]
    return l

def load_arxes():
    '''
    φορτώνει τις αρχές στο λεξικό arxes{}
    '''
    with open('500_arxes.csv', 'r', encoding = 'utf-8') as f :
        for arxi in f:
          arxi = arxi.split(';')
          key = arxi[0]
          value = arxi[1].strip('\n')
          arxes.update({key:value})

def rss_filename(url):
    '''
    Η συνάρτηση με όνομα το αντίστοιχο της διεύθυνσης url που ενδιαφέρει τον χρήστη,

    '''
    furl=url
    furl=furl.strip()
    furl=furl.replace("https://","")
    furl=furl.replace("/rss","")
    furl=furl.replace("/","_")
    furl=furl.replace(".","_")
    furl=furl+".rss"
    return furl          
######### main ###############
'''
το κυρίως πρόγραμμα διαχειρίζεται την αλληλεπίδραση με τον χρήστη
'''
load_arxes()
while True :
    arxh = input(50*"^"+"\nΟΝΟΜΑ ΑΡΧΗΣ:(τουλάχιστον 3 χαρακτήρες), ? για λίστα:")
    if arxh == '':
        break
    elif arxh == "?": # παρουσιάζει τα ονόματα των αρχών
        for k,v in arxes.items():
            print (k,v)
    elif len(arxh) >= 3 :
        # αναζητάει όνομα αρχής που ταιριάζει στα κριτήρια του χρήστη
        result = search_arxes(arxh) 
        for r in result:
            print (result.index(r)+1, r, arxes[r])
        while True:
            epilogh = input("ΕΠΙΛΟΓΗ....")
            if epilogh == "" or len(result) == 0: break
            elif epilogh.isdigit() and 0<int(epilogh)<len(result)+1:
                epilogh = int(epilogh)
                url = arxes[result[epilogh-1]]
                print(url)
                # καλεί τη συνάρτηση που φορτώνει το αρχείο rss:
                rss_feed(url)
            else: continue
    else :
        continue
