# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:30:22 2019

@author: Anupreet Singh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from requests import get
from bs4 import BeautifulSoup as bs
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import keyboard
import click
import csv
import threading
import sys
import os
import time
import math
import re
import random
import cleverbotfree.cbfree

my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

from chatterbot.trainers import ChatterBotCorpusTrainer
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')
cb=cleverbotfree.cbfree.Cleverbot()
def chat(userin):
    return cb.single_exchange(userin)
    



chrome_options = Options()
chrome_options.add_argument("user-data-dir=./User_data")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://web.whatsapp.com/")
time.sleep(10)


# set this  to the group name you want the bot to work in
target = '"Hsj"'

driver.find_element_by_css_selector('span[title='+target+']').click()
time.sleep(2)
scr1 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
time.sleep(1)
url=driver.page_source
soup=bs(url,"lxml")

fortune_cookie=["It is certain"  ,"It is decidedly so"  ,"Without a doubt"  ,
                "Yes, definitely"  , "You may rely on it"  , "As I see it, yes"  ,
                "Most likely"  , "Outlook good"  , "Yes"  , "Signs point to yes"  ,
                "Reply hazy, try again"  , "Ask again later"  ,
                "Better not tell you now"  , "Cannot predict now"  ,
                "Concentrate and ask again"  , "Don't count on it"  , "My reply is no"  ,
                "My sources say no"  , "Outlook not so good"  , "Very doubtful"]

pickup=["Did you ever realize screw rhymes with me and you?"  , "I lost my virginity... can I have yours?"  ,
        "My body is telling me yes. I hope yours is doing the same thing."  ,
        "Oh no, I'm choking! I need a mouth to mouth, quick!"  ,
        "What's your favourite silverware? Because I like to spoon!"  ,
        "Be unique and different, just say yes."  ,
        "Your father must be a drug dealer, cuz you dope!"  ,
        "Hi, will you reject me if I try and pick you up?"  ,
        "Are you tired? Because you've been running around in my mind all day!"  ,
        "Hi, the voices in my head told me to come over and talk to you."  ,
        "Do you have a map? I just keep getting lost in your eyes."  ,
        "If I were a cat, would you like me to spend all 9 lives with you?"  ,
        "You're on my list of things to do tonight."  , "Ik ben helemaal niet dik!"  ,
        "I'm not sure what quidditch position you play, but I bet you're a keeper."  ,
        "I'm not a photographer, but I can picture us together."  ,
        "Ik kan bepalen of zeugen berig zijn."  ,
        "Is jouw naam WiFi, want ik voel een connectie."  ,
        "Ben jij IEEE 802.11, want ik voel een connectie."  ,
        "Ben je dopamine? Want je maakt me blij."  ,
        "Are you a fossil? Because I'm a paleontologist and I want to date you badly."  ,
        "You're pretty, I'm pretty, want to go back to my place and stare at each other for a while?"  ,
        "I have a netflix account."  ,
        "On a scale from 1 to 10, you're a 9 and I'm the 1 you need. "  ,
        "I want to paint you green and spank you like a disobedient avocado."  ,
        "I want to paint you purple and spank you like a disobedient eggplant. "  ,
        "I want to paint you red and spank you like a disobedient tomato."  ,
        "Do you live around here often?"  , "If you were a flower, I'd fuck you."  ,
        "Are you dead, because you give me the necropheels."  ,
        "Hey babe, wanna have really high expectations and then be really disappointed?"  ,
        "You'll do."  , "Hey... Get in the van."  , "I think I'm in love with you."  ,
        "Do you have a last name? Because I want it."]


spotify=["396L7sSrvWRrdDFS6uu9tB"
       ,
        "3u4rIcRR7gSoJdkJIx9zpu"
       ,
        "6trOWWOKQeql1UibRk9SBS"
       ,
        "3eR23VReFzcdmS7TYCrhCe"
       ,
        "0E3HnGJSMplqBSYGsh2exH"
       ,
        "0IVHlst3XMgzXUJbIyZ8oO"
       ,
        "6GyFP1nfCDB8lbD2bG0Hq9"
       ,
        "0xzn2U71zNWLeJbE4Zat4C"
       ,
        "7hzlzoOwCZ4D3Ow5YZK4kj"
       ,
        "1WSGTYKLEpKfNQYYW5Oymt"
       ,
        "7FtQLQTo7fFPkM855kmAwm"
       ,
        "6J9kvynZrZnWRZOkyjkV3n"
       ,
        "1OJxI8lIWRqBvouJxW1nzN"
       ,
        "0CZ8lquoTX2Dkg7Ak2inwA"
       ,
        "0vxVmFrsrREswFaAT0QEkA"
       ,
        "3Kuu5vASpXK8oRsxOvau6P"
       ,
        "7K7E7LKK51PezScgsvVg9Y"
       ,
        "2Fxmhks0bxGSBdJ92vM42m"
       ,
        "5aszZdstjgA4vz2N6NBkGo"
       ,
        "4aSfgWmRa9KsISD4Jmx7QB"
       ,
        "6PR3ZUCnxtQTEu30qgZLwT"
       ,
        "7I8MCiM3A4xvnM6zIiuMZn"
       ,
        "2cGxRwrMyEAp8dEbuZaVv6"
       ,
        "0mp6WVhgI5FF6DGtYcyBNm"
       ,
        "4Kaw0HUTA9Q3z7Elnqvb8T"
       ,
        "5fqjfiMOFapIb8uFcxBStH"
       ,
        "1OS490EO5cVK5ht55dLlB3"
       ,
        "18IEKx5i6mgxVh2pp3hFpW"
       ,
        "6Dno7FrbG6vnTm9KfjFwf6"
       ,
        "5Vi5PBLiJAq0GVU1n9yZRB"
       ,
        "4G3IXyVRxSx5lLhUvv3fu3"
       ,
        "5Nt6b6XcJgOCtvs1yaYroM"
       ,
        "4x79cjezqX3yd15rSrAVFF"
       ,
        "5qaEfEh1AtSdrdrByCP7qR"
       ,
        "6Pz0u5ItrGIwkKr0Z7S93H"
       ,
        "4qhpmaAwOP4R59YrNpVRin"
       ,
        "4B6A1T91lF1IRKkBVwUzWe"
       ,
        "73OZcwiBI41R0o5TDGeZ7i"
       ,
        "6vvyavHx8WHdsw6vsuMwyR"
       ,
        "1CxoHCwwmaXHimhV2cyTBx"
       ,
        "6xwhCiWXREsAIQVZqHswVw"
       ,
        "5Il6Oe7lr5XM7A0cWbVQtr"
       ,
        "3nNNYRBtkNsKjertmtTRMO"
       ,
        "5ezjiqla1EIIXUOWrs2aGu"
       ,
        "6aXluH3KdN1DcFJgyEhzF6"
       ,
        "4Ar3oSp4bAw5gz22F70GM7"
       ,
        "4kV4N9D1iKVxx1KLvtTpjS"
       ,
        "4um6CPDIxnNWSEbj3LJQhQ"
       ,
        "57nReJa69S1lEJGYHLCKlx"
       ,
        "5p7ujcrUXASCNwRaWNHR1C"
       ,
        "4mu5UnYMvr9NgtqK4N5BGN"
       ,
        "1JIWyERVO0MWPBC5W7OF2Q"
       ,
        "4NzMOnvSJVNKF7nw5NkXIP"
       ,
        "5xhQChGGhKLWqBqX4XhtYE"
       ,
        "7zsXy7vlHdItvUSH8EwQss"
       ,
        "7r21zihtk3dpmhgnmqOjUO"
       ,
        "5dARQrWSzFLtdRP1s0hjea"
       ,
        "6CfniWm3ly8u5q4r4DAh2T"
       ,
        "7E2ZNBAy0DFOWC5RUEyh5V"
       ,
        "4RROfcxQXFIwW0ugcZfdC4"
       ,
        "3t54qOwXEw2pUCqqkYLkFK"
       ,
        "4Fvtl6P5d8h2lzzwhUCHHD"
       ,
        "0rnsCkei7qBWm9NNJNXVHo"
       ,
        "1lpLPTbD2SzE2ULY8s1rSu"
       ,
        "1gk3FhAV07q9Jg77UxnVjX"
       ,
        "5pLpkaIRobcvPnUmclNv6o"
       ,
        "3S9C6nln4g7FySngPwhWs0"
       ,
        "7w0FV6ViNDZFy9Mu90sQzl"
       ,
        "0rRjGruFonCGOt0S5zAJNQ"
       ,
        "14msK75pk3pA33pzPVNtBF"
       ,
        "1NLk2ytaTQSfgKvBjCRIFY"
       ,
        "2U9xilwDVbl5upU99insIn"
       ,
        "6mUwMth1MQT8NVSMI7lKjx"
       ,
        "54u57ENyxehtdNKSUVFa6I"
       ,
        "6WmIyn2fx1PKQ0XDpYj4VR"
       ,
        "7t45rVEAGizSu3THc05qVv"
       ,
        "3dYD57lRAUcMHufyqn9GcI"
       ,
        "2k80B1DEqJFUG4L5LUa6Mv"
       ,
        "54OyMf9WrMvrkAlZ3t0AMs"
       ,
        "4uTvPEr01pjTbZgl7jcKBD"
       ,
        "16gvjuZGmibA3348jWdjKV"
       ,
        "3DamFFqW32WihKkTVlwTYQ"
       ,
        "6vi4I2vZkN5mDePmVSSVTq"
       ,
        "6mORGLOz79w6VsCRLWYYuK"
       ,
        "3dK02Pz2XLiqLKx1GQQwb9"
       ,
        "1gNcPHAiVIQZmqJFJdt3ti"
       ,
        "71e1rw9RguCvkunZyI33CY"
       ,
        "50Nbcw1vdETKBXvw5ogoV1"
       ,
        "19hM5qpD5U5jLmNh4dg77m"
       ,
        "7hDVYcQq6MxkdJGweuCtl9"
       ,
        "3sbcAG3y97g63yDSVMf38o"
       ,
        "1VqmEOKrIBxNbnvMaTfssE"
       ,
        "100eDEmpWV5YGVCqHI0leU"
       ,
        "4WMCllwqU4hot6yqJcxWoH"
       ,
        "1tinoQpYXzpZDrb0BjK1e7"
       ,
        "30yJXxtuCUjmQ6xn5suA4N"
       ,
        "3ee8Jmje8o58CHK66QrVC2"
       ,
        "0ww9IfRZtVFvfQ42RKP7B3"
       ,
        "04D2wKcN9ju5IY06nwV24m"
       ,
        "5IMtdHjJ1OtkxbGe4zfUxQ"
]

spotify_comment=["Love this song",
                 "This is <3",
                 "OMG please listen to this",
                 "<3<3",
                 "you gotta listen to this",
                 "such a sweet voice",
                 "wow just wow"]

depressed_quotes=["Depression is a battle between a body that fights with all its might to survive and a mind that wants to die.",
                  "People ask me what depression is like. I tell them it’s a lot like walking down a dark hallway, never really knowing when the light turn go on.",
                  "Remember this: You weren’t put here to be depressed. To feel guilty, ashamed, unworthy or condemned. You were put here to be victorious.",
                  "I honestly don’t know what I want in life. I don’t even know what I want right now. All I know is that it hurts so much inside, and it’s eating me alive. One day, there won’t be anything left of me.",
                  "I honestly don’t like getting close to people. In my mind, they’re just going to walk out of my life anyway no matter how close we were.",
                  "Depression is an overwhelming feeling of numbness, and the endless desire for something – anything – to take you from one day to the next.",
                  "I smile to make everyone’s day, but the truth is that I’m crying on the inside.",
                  "I hate feeling like I’m here, but I’m really not; like someone cares, but they really don’t; like I belong anywhere but here.",
                  "Sometimes, you just need that one person to tell you that you aren’t as bad as you think you are.",
                  "Depression makes you feel like you want to just disappear from the world, but in reality, all you truly want is to be found.",
                  "lol i wanna kill myself"
                  ]

srijan_dict=["ttylirl",
             "Srijan has left the group",
             "Mujhe bt mat de",
             "IRL mein baat karunga",
             "bro gorakhpur better than mumbai bro",
             "Keventers h gorakhpur mein",
             "bsdk teen teen gaaye h mere paas",
             "Ghar ghar mein bhoot mullon ki maa ki chut",
             "Chal nashe karte h",
             "Call me for cab bookings"
             ]




#wait = WebDriverWait(driver, 600)

#string ="Hi i am a bot!"
#input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#input_box.send_keys(string + Keys.ENTER)
url=driver.page_source
soup=bs(url,"lxml")
srijan_mode=False
cbbot=True
while(1):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
    time.sleep(2)
    messages=soup.find_all('span',class_='_F7Vk selectable-text invisible-space copyable-text')
    print(str(messages[-1]))
    clean=str(str(messages[-1]).replace("\n"," "))
    print(clean)
    if re.search(r'<span>(.*?)</span>',str(clean)) is not None:
        input_msg=re.search(r'<span>(.*?)</span>',clean).group(1)
    else:
        input_msg=re.search(r'<span>(.*?)</span>',str(clean))
    print(input_msg)
    if "@bot " in input_msg:
        if "on srijan mode" in input_msg:
            srijan_mode=True
            string="Srijan mode ON!!!!"
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "off srijan mode" in input_msg:
            srijan_mode=False
            string="Srijan mode Off"
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif srijan_mode:
            string=random.choice(srijan_dict)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "start bot2" in input_msg:
            cbbot=True
            string="Replaced bot1 with a newer version"
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "start bot1" in input_msg:
            cbbot=False
            string="You just downgraded back to bot1 u degenerate!"
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif cbbot:
            string=chat(input_msg)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "hello there" in input_msg:
            string ="general kenobi!"
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "fortune cookie" in input_msg:
            string=random.choice(fortune_cookie)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "pickup line" in input_msg:
            string=random.choice(pickup)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "music" in input_msg:
            string="https://open.spotify.com/track/"+random.choice(spotify)+"\n"+random.choice(spotify_comment)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        elif "depress" in input_msg:
            string=random.choice(depressed_quotes)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
        else:
            send_string=input_msg.replace('@bot','')
            string=str(my_bot.get_response(send_string))
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys(string + Keys.ENTER)
    url=driver.page_source
    soup=bs(url,'lxml')








