from datetime import date, timedelta
import urllib.request as urlrequest
import os
import time

def main():
    #friendlyjava
    #openknot
    #rest
    #sourcefu
    #virtualJUG
    #---
    #javaee
    #northeastlinuxfest
    #pdurbin
    #spanworm
    #wonderstudy

    #archive("friendlyjava", date(2014, 3, 29), date(2021, 8, 10))
    #archive("openknot", date(2015, 7, 29), date(2021, 8, 10))
    #archive("rest", date(2014, 5, 24), date(2018, 9, 18))
    #archive("sourcefu", date(2012, 11, 28), date(2021, 8, 10))
    #archive("virtualJUG", date(2014, 11, 12), date(2017, 10, 31))

    #archive("javaee", date(2013, 7, 17), date(2014, 3, 30))
    archive("northeastlinuxfest", date(2013, 3, 29), date(2014, 4, 6))
    #archive("pdurbin", date(2012, 11, 28), date(2012, 12, 14)) # removed days with no content
    #archive("spanworm", date(2013, 2, 8), date(2014, 4, 4))
    #archive("wonderstudy", date(2013, 5, 11), date(2014, 5, 18))

def archive(name, start_date, end_date):
    print(name, start_date, end_date)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = str(start_date + timedelta(days=i))
        #print(day)
        time.sleep(1)
        url = 'http://irclog.greptilian.com/' + name + '/' + day
        print(url)
        response = urlrequest.urlopen(url)
        content = response.read().decode(response.info().get_param('charset') or 'utf-8')
        daydir = name + '/' + day
        #print(daydir)
        os.makedirs(daydir, exist_ok=True)
        with open(daydir + '/index.html', 'w') as indexfile:
            indexfile.write(content)

    # get index page for #friendlyjava
    index_url = 'http://irclog.greptilian.com/' + name
    index_response = urlrequest.urlopen(index_url)
    index_content = index_response.read().decode(response.info().get_param('charset') or 'utf-8')
    chandir = name + '/'
    os.makedirs(chandir, exist_ok=True)
    with open(chandir + '/index.html', 'w') as indexfile:
        indexfile.write(index_content)

if __name__ == '__main__':
    main()
