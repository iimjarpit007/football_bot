import bs4
import requests
import numpy as np
from datetime import date
import time
#import pandas as pd
import re
from bs4 import BeautifulSoup


def football_update():
    res = requests.get('https://www.goal.com/en-in/live-scores')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    soup_data = soup.select('.widget-fixtures-and-results')

    # splitting and geeting text as List-newval
    val = ''
    newval = []
    for i in soup.select('.widget-fixtures-and-results'):
        # print(i.text)
        val = i.text
    print(val)
    neval = val.split()
    print('newval', neval)

    # occ=neval.index('Premier')
    # print(occ)

    # triming list element by removing other championship-hmatch
    hmatch = []
    for m in range(len(neval)):
        if neval[m] != "Copa":
            hmatch.append(neval[m])
        elif neval[m] == "Copa":
            break

    # converting todays date in string format to compare with date in list

    todayfor = time.strftime("%d/%m/%Y")
    print(todayfor)
    todayrst = todayfor[0:6]
    todayyr = todayfor[8:]
    print("todayrst", todayrst)
    print("todayyr", todayyr)
    todcomp = todayrst + todayyr
    print("todcomp", todcomp)
    # print(nwarray[0][1]==todcomp)

    # taking index of date in list
    for i in range(len(neval)):
        if neval[i] == todcomp:
            y = i
            break
    print("index value of date", y)
    # removing list(hmatch) elements until 1st occurence of todays date

    del hmatch[0:y]
    print("list after removing through today dates", hmatch)

    # storing indices of todays date

    indices = []
    for i in range(len(hmatch)):
        if hmatch[i] == todcomp:
            indices.append(i)
    print("index values of todays date", indices)
    print(len(hmatch))
    print(hmatch[26])
    locdate = indices[-1]
    print("last occurence of todays date", locdate)

    # trim hmatch content till last match content and convert to list mcontent
    mcontent = hmatch[:locdate + 9]
    print("trimmed only match content", mcontent)

    nsplits = len(indices)
    nwarray = np.array_split(mcontent, nsplits)

    for i in range(nsplits):
        print(nwarray[i])

    print(nwarray[0][1])
    # today = date.today()
    # print("Today date is: ", today)
    # today = time.strftime("%Y-%m-%d")
    # today = date.today()
    # print("Today date is: ", today)
    # today = time.strftime("%Y-%m-%d")

    # storing displayable content of matches in List to be returned)
    for i in range(len(nwarray[0])):
        if nwarray[0][i] == todcomp:
            y = i
            break
    print(nwarray[0][y])
    print("index of date ", y)
    print("the match between {fteam} and {steam} was played on {d} {t}{moev} {zone} and the score was {fts}{hy}{sts}"
          .format(fteam=nwarray[0][7], steam=nwarray[0][8], d=nwarray[0][0], t=nwarray[0][1], moev=nwarray[0][2]
                  , zone=nwarray[0][3], fts=nwarray[0][4], hy=nwarray[0][5], sts=nwarray[0][6]))

    st1 = "the match between " + nwarray[0][7] + " and " + nwarray[0][8] + " was played on " + nwarray[0][
        0] + " and the score was " + nwarray[0][4] + "-" + nwarray[0][6] + "."
    print("st1", st1)

    finallist = []
    count = 0
    for i in range(nsplits):
        st2 = "the match between " + nwarray[i][7] + " and " + nwarray[i][8] + " was played on " + nwarray[i][
            0] + " and the score was " + nwarray[i][4] + "-" + nwarray[i][6]
        print("i", i)
        finallist.insert(i, st2)
    print("finallist", finallist)
    return finallist



