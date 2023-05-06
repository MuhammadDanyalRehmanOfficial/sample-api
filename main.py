
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.masala.tv/curry-patta-pulao-quick-recipe-masala-tv/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# extract video URL
video_url = soup.find('iframe')['src']

# create recipe dictionary
recipe = {
'video_url': video_url
}

# write recipe dictionary to JSON file
with open('curry_patta_pulao.json', 'w') as f:
    json.dump(recipe, f)