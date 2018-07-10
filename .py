# Created by: Roman Beya and Gillian Gonzales
# Created for: Digitera Interactive, Web Scraping Assignment: Link 2
# Created on: Tuesday, July10th, 2018
# This script scrapes all of the data off of this DJ website using Beautiful Soup to parse the data

from bs4 import BeautifulSoup
import requests
import csv

# Create a csv file object that will open up a new csv file and write to it
csv_file = open("Web_Scraping_Link_2.csv", "w")

# Create a csv writer object that will write to the new csv file created above
csv_writer = csv.writer(csv_file)

# Define names of headers to properly identify the sorted data
csv_writer.writerow(['Name_of_DJ', 'Followers', 'Music Type', 'Global Rank', 'Voters Choice'])

# Open up a connection to request the specific url of the website that is to be scraped
the_dj_list_URL = requests.get("http://thedjlist.com/djs/rank/1").text

# Create a BeautifulSoup object called soup, add arguments("which website do you want to parse", "which format")
soup = BeautifulSoup(the_dj_list_URL, "lxml")

# Grabbing the title of the web page
title_of_the_dj_list = soup.title.string

# Storing within the variable container, all of the containers that hold all attributes of the individual DJs
containers = soup.findAll("div", class_="col-sm-15 col-xs-12")
print(len(containers))

# Creating a loop that will iterate through all the DJs and return back the names of each DJ
for container in containers:
    # Loop through all names of DJs
    name_of_dj = container.find("div", class_="name-dj")

    # Loop through all followers per DJ
    number_of_followers = container.find("div", class_="follower-dj")

    # Loop through all the types of music
    # There are many types music but only one is chosen NEED A FIX
    types_of_music = container.find("div", class_="tag-profile-global margin-left")

    # Loop through the global rankings of DJs
    global_rank = container.find("span", class_="number-global")

    #

    # Split the HTML string by every occurrence of the character sequence ">
    split_name_of_dj_front = name_of_dj.string.split("\">")[0]  # Return the first value in the list
    split_number_of_followers_front = number_of_followers.string.split("\">")[0]
    split_global_rank_front = global_rank.string.split("\">")[0]
    try:
        split_type_of_music_front = types_of_music.string.split("\">")[0]
    except AttributeError:
        # Could be replaced with N/A because of DJ doesn't have a type of music
        continue

    # Split the HTML by every occurrence of the character sequence </div>
    split_name_of_dj_back = split_name_of_dj_front.split("</div>")[0]
    split_number_of_followers_back = split_number_of_followers_front.split("</div>")[0]
    split_type_of_music_back = split_type_of_music_front.split("</div>")[0]
    split_global_rank_back = split_global_rank_front.split("</span>")[0]
    print(split_global_rank_back)
    # print(split_type_of_music_back)
    # print(split_name_of_dj_back)
    # print(split_number_of_followers_back)

    # Using try-except block to work around minor ascii bug - WILL REVIEW LATER IF TIME
    try:
        # Add the data to the correct header
        csv_writer.writerow([split_name_of_dj_back, split_number_of_followers_back, split_type_of_music_back,
        split_global_rank_back])
    except UnicodeEncodeError:
        continue

# Closing the csv file after use to open it again in the future
csv_file.close()
