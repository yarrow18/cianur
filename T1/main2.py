from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import random
import threading
import time
import os
import requests
from fake_useragent import UserAgent

ti = 0
print("Don't forget to choose your config in config.txt")
print("Si vous ne savez pas, ecrivez: 0")
artist = input("Pseudo de l'artiste:\n")
#artist = "arrow_2828"
playlist = input("Lien de la playlist:\n")
#playlist = "https://open.spotify.com/playlist/6jkAa6Y7zbTo3p4XTjnXTy"
songtime = input("Temps total de la playlist:\n")
v1 = int(songtime)
#songtime = 60
repete = input("Nombre de vue (Le chiffre sera multiplier par 50):\n")
v2 = int(repete)
number_of_threads = input("Nombre de threads (Seulement 1 pour le moment):\n")
v3 = int(number_of_threads)

options = Options()
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
ua = (random_line('useragents.txt'))

ti2 = 0
fipp = open("OUTPUT_FILE.txt", "w")
fipp.close()
os.system("python gen.py -n 51 -o OUTPUT_FILE.txt")
while ti2 < v2:
    if ti < 50:
        print(ua)
        try:
            options.add_argument(f'user-agent={ua}')
            options.add_argument('--no-sandbox')
            options.add_argument('--log-level=3')
            options.add_argument('--lang=en')
            # Removes navigator.webdriver flag
            options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
            # For older ChromeDriver under version 79.0.3945.16
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("window-size=1280,800")
            # For ChromeDriver version 79.0.3945.16 or over
            options.add_argument('--disable-blink-features=AutomationControlled')
            #options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            try:
                driver.get("https://accounts.spotify.com/en/login/")
            except:
                pass

            with open('OUTPUT_FILE.txt') as f:
                for i, liness in enumerate(f):
                    if i == ti:
                        liness = liness.split(":")
                        firstName, lastName = liness[2], liness[3]
                        print(firstName, lastName)

            time.sleep(5)
            try:
                username_elem = driver.find_element_by_id('login-username').send_keys(firstName)
                password_elem = driver.find_element_by_id('login-password').send_keys(lastName)
                time.sleep(1)
                try:
                    login_button_elem = driver.find_element_by_id('login-button').click()
                except:
                    pass
                print("Login Done! Now in porcess...")
                time.sleep(5)
                #Insert your config
                ###################################################################################################################################################################
                driver.get("https://open.spotify.com/user/" + artist)
                time.sleep(8)
                spotifyfollow = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div/button[1]').click()
                time.sleep(3)
                #End config
                #####################################################################################################################################################################################
            except:
                pass
            try:
                driver.close()
            except:
                pass
        except:
            pass
        print("Finished")
        ti = ti + 1
    else:
        print("Create account... Please wait")
        fipp = open("OUTPUT_FILE.txt", "w")
        fipp.close()
        time.sleep(600)
        os.system("python gen.py -n 51 -o OUTPUT_FILE.txt")
        time.sleep(5)
        ti = 0
        ti2 = ti2 + 1








