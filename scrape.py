#-----------------------------------------Init-------------------------------------------------------------------
from termcolor import colored
import asyncio, time
import numpy as math
import time
from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Time:
    def __init__(self):
        self.start_time = 0

    async def dates(self):
        while True:
            t = time.time()
            if self.start_time == 0:
                self.start_time = t
            yield t
             #sleep period determines interval of next GET scraped data and POST to db
            await asyncio.sleep(86400)

    async def printer(self):
        while True:
#------------------------------------------------------GET--------------------------------------------------------
            this_Moment= (datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print (colored(this_Moment,'blue'))
            url="https://www.globalpetrolprices.com/South-Africa/"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            ZAR=soup.findAll()
            filter1=ZAR[0].text.replace('\n'," ")
            split_val=filter1.replace(','," ")
            split_val
            split_value=split_val.replace(','," ")
            reval=split_value.replace('\r'," ")
            redat=reval.split(" ")
            relist=list(redat)
            space=("")
            space_index=relist.index(space)
            fuel_Date_index=275
            Fuel_Date_val=relist[(fuel_Date_index)]
            print(colored("Last Date Price Changed :"+Fuel_Date_val,'green'))
            Fuel_value_index =280
            Fuel_value=relist[(Fuel_value_index)]
            FUll_Fuel_Value=("R"+Fuel_value+" "+"L")
            print("Petrol :" + FUll_Fuel_Value)
            Diesel_Date_value_index =300
            Diesel_Date_value=relist[(Diesel_Date_value_index)]
            print(colored("Last Date Price Changed :"+Diesel_Date_value,'green'))
            Diesel_value_index =305
            Diesel_value=relist[(Diesel_value_index)]
            Full_Diesel_Value=("R"+Diesel_value+" "+"L")
            print("Diesel :"+Full_Diesel_Value)
#---------------------------------------------------POST------------------------------------------------------------------
            data= {"Last Updated Diesel:": Diesel_Date_value,
            "Last Updated Petrol:": Fuel_Date_val,
            "Diesel Price": Diesel_value,
            "Petrol Price": Fuel_value,
            "Script TTL": this_Moment}
            r = requests.post('https://appnostic.dbflex.net/secure/api/v2/61847/CE1FD141E909483CBC78D51A80180680/Live%20Fuel%20Price/create.json',data)
            print(colored("API RESPONSE CODE : "+str(r.status_code),'yellow'))
            print(colored("API RESPONSE : "+str(r._content),'red'))
           # time.sleep(86400)--this sleep is another way to determine the frequency of Get and POST to happen

            await asyncio.sleep(self.interval)

    async def init(self):
        async for i in self.dates():
            if i == self.start_time: 
                 #interval period determines interval of next GET scraped data and POST to db
                self.interval = 10 
                await self.printer()
            print(i) # Never Called
#-------------------------------------loop for GET and POST methods-----------------------------------------------------
loop = asyncio.get_event_loop()
t = Time()
loop.run_until_complete(t.init())