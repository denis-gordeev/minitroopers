import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import http.cookiejar
import os
import itertools

nicks_f = open('troopers.txt','r')
nicks = nicks_f.read().split(' ')
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

class Opponent(object):
    def _init_(self, name, strength, link):
        self.name = name
        self.strength = strength
        self.link


def battles(nick):
    print (nick.upper(), 'is fighting!')
    f = opener.open("http://"+ nick +".minitroopers.com/b/opp")
    r = f.read()
    soup = BeautifulSoup(r)
    opponents = soup.find_all('td')[2:]
    opponents_list = []

    for i in range(len(opponents)):
        if i == 1:
            pass
        else:
            if len(opponents)<2:
                return
            opp = opponents[i]
            if not opp.h1:
                return
            name = opp.h1.get_text()
            strength = int(opp.li.get_text().strip())
            link = opp.a['href']
            opponents_list.append([name,strength,link])
    min_strength = 999
    your_opponent = 0
    for i in range(len(opponents_list)):
        if opponents_list[i][1] < min_strength:
            your_opponent = i
            min_strength = opponents_list[i][1]

    f = opener.open("http://"+ nick +".minitroopers.com"+opponents_list[your_opponent][2])

    print("http://"+ nick +".minitroopers.com"+opponents_list[your_opponent][2])
    r = f.read()
    print('Your opponent is', opponents_list[your_opponent][0])
    print ('His strength is', opponents_list[your_opponent][1])
    key = re.findall('chk.*',opponents_list[your_opponent][2])
    missions(key)
def missions(key):
    print ("Some missions here")
    f = opener.open("http://"+nick+".minitroopers.com/b/mission?"+key[0])

for nick in nicks:
    for _ in itertools.repeat(None, 3):
        battles(nick)

