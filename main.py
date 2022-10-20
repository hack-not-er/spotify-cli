from selenium import webdriver
import os, sys, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    


artist={
    'bartika': '0iK3Z8bWIvj3PKVcUoOwGM',
    'ritviz' : '72beYOeW2sb2yfcS4JsRvb',
    'elements' : '3bLWp801OAckSYWrb0sgsH',
    'albatross' : '3Ols8mMOUzTAbtPmkm7HTa',
    'sacar' : '2KDTINgANslhPVBfLpNlz0',
    'rohit' : '7mz57vhpn0t6ETubyNa2Lp',
    'pariwartan' : '4ccMep7khP7H2V5yBaXn9h',
    'sabin' : '0pgcJf1JOhP3n3WbMlA4wu',
    'city' : '4DkYxtaASIKQnk4Gj0TB7k',
    'metallica' : '2ye2Wgw4gimLv2eAKyk1NB',
    'bipul' : '3sauLUNFUPvJVWIADSYTvZ',
    'arthur' : '0A1Qr8l43fIqhB5aItVaMy',
    'tribal rain' : '6So94AgQzV91d8k5xWb6wU',
    'sajjan' : '1deQzOQwArAsUgm2WdjtyI',
    'adele' : '4dpARuHxo51G3z768sgnrY',
    'ulto pulto' : '4GKKwO6NVDSrvEua9D6EzT',
    'coldplay': '4gzpq5DPGxSnKTe4SA8HAU',
    'pink floyd' : '0k17h0D3J5VfsdmQ1iZtE9',
    'linkin park': '6XyY86QOPPrYVGvF9ch6wz'
    }

playlist={
    'bipul radio': '37i9dQZF1E4ACR94Uehq9H',
    'city radio' : '37i9dQZF1E4rJoGRQVHrxB'
}

def get_artist():
    artist_name = input('Enter the artist name: ')
    try:
        artist_id = artist[artist_name]
    except KeyError:
        print(f'Artist not found\n Your options are: \n {[_ for _ in artist.keys()]}')
        get_artist()
    return artist_id

def get_playlist():
    playlist_name = input('Enter the playlist name: ')
    try:
        playlist_id = playlist[playlist_name]
    except KeyError:
        print(f'playlist not found\n Your options are: \n {[_ for _ in playlist.keys()]}')
        get_playlist()
    return playlist_id

def login():
    
    #username field

    #wait for the username field to be visible
    username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-username')))
    username.send_keys('xx')

    #password field
    password = driver.find_element_by_id('login-password')
    password.send_keys('xxx')
    time.sleep(1)

    #click login button
    driver.find_element_by_id('login-button').click()

def play():
    global playButton
    playButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[data-testid='play-button'][class='Button-qlcn5g-0 kgFBvD']")))

    exists = ''
    try:
        banner_close = driver.find_element_by_id('onetrust-close-btn-container')
        exists = True
    except NoSuchElementException:
        exists = False
    if exists:
        banner_close.click()
    shuffle = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[data-testid='control-button-shuffle']")))

    print(shuffle.get_attribute('aria-label'))
    if shuffle.get_attribute('aria-label') == 'Enable shuffle':
        shuffle.click()

    time.sleep(1)
    
    #click play button
    playButton.click()

if len(sys.argv) > 1:
    if sys.argv[1] == 'artist':
        artist_id = get_artist()
        link = f'https://open.spotify.com/artist/{artist_id}' 
    elif sys.argv[1] == 'liked':
        link = 'https://open.spotify.com/collection/tracks' 
    else:
        playlist_id = get_playlist()
        link = f'https://open.spotify.com/playlist/{playlist_id}'
else:
    print('No argument given \n Usage: \n python3 main.py artist \n python3 main.py liked \n python3 main.py playlist')
    exit()

def next():
    driver.find_element(By.CSS_SELECTOR,"button[data-testid='control-button-skip-forward']").click()


driver = webdriver.Chrome(executable_path='E:\SeleniumDrivers\chromedriver.exe')
driver.get(link)
driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button'][class='Button-qlcn5g-0 gPMZVP']").click()

login()
play()

while True:

    command = input('Any command: ')

    if command == 'exit':
        driver.close()
        exit()
    elif command == 'next':
        next()
    elif command == 'pause' or command=='play':
        playButton.click()

    elif command == 'other artist':
        artist_id = get_artist()
        link = f'https://open.spotify.com/artist/{artist_id}' 
        driver.get(link)
        play()
    elif command == 'other playlist':
        link = f'https://open.spotify.com/playlist/{playlist[sys.argv[2]]}' 
        driver.get(link)
        play()
    else:
        print('Invalid command')
        continue
