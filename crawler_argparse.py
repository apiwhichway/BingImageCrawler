import time
import os
import json
import argparse
from PIL import Image

import pandas as pd
import urllib.error
import urllib.request

from selenium import webdriver
from tqdm import tqdm
from io import BytesIO

from urllib.parse import urlparse
from user_agent import generate_user_agent

# local python
# from image_crawler import ImageCrawler


parser = argparse.ArgumentParser(description='Process sesrch keys and page scrolling.')
parser.add_argument('search_keys', help = 'search keys')

args = parser.parse_args()
print(args.search_keys)

###############################################
# search_keys declaration
###############################################
search_keys = "Birds"
search_keys = args.search_keys
page_scrolling = 10

images_save_dir = os.path.join('../data/imgs', search_keys)
link_save_dir = os.path.join('../data/links', search_keys)


print("search_keys: ", search_keys)
print("page_scrolling: ", page_scrolling)

print("images_save_dir: ", images_save_dir)
print("link_save_dir: ", link_save_dir)


see_more_pages = '//div[@class="mm_seemore"]/a[@class="btn_seemore"]'
image_sqaure_xpath = '//div[@class="imgpt"]/a[@class="iusc"]'

link_save_item = 'm'
link_save_item_attr = 'murl'

image_links = set()



###############################################
# driver declaration
###############################################



driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.bing.com/images')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element('name','q')

search_box.send_keys(search_keys)

search_box.submit()

driver.get('http://www.bing.com/images/search?q=' + search_keys + '&qft=+filterui:imagesize-custom_256_256+filterui:photo-transparent')

###############################################
# scrolling section
###############################################
for _ in tqdm(range(page_scrolling), ncols=70):
    driver.execute_script('window.scrollBy(0, 1000)')
    time.sleep(1)

    if see_more_pages is not None:
        try:
            driver.find_element('xpath', see_more_pages).click()
            # time.sleep(1)
        except Exception as e:
            print(e)
            print("the bing page may automatically expanding when scrolling in newer version \n")
            # time.sleep(1)

###############################################
# download function
###############################################

count = 0
headers = {}

def download_image( image_url, image_save_dir, image_name,search_keys ):

    global count
    global headers

    print( "downloading image: ", image_url, "\n")

    try:
        parse = urlparse(image_url)
        ref = parse.scheme + '://' + parse.hostname
        ua = generate_user_agent()
        headers['User-Agent'] = ua
        headers['referer'] = ref

        req = urllib.request.Request( image_url.strip(), headers = headers )
        response = urllib.request.urlopen( req, timeout = 5 )

        data = response.read()
        # image = Image.open(BytesIO(data)).convert('RGB')
        image = Image.open(BytesIO(data))


        ext = image_url.split('.')[-1]
        image_name ='{}_{}.{}'.format(search_keys,image_name, ext)
        image_path = os.path.join( image_save_dir, image_name )
        image.save( image_path )
        print( image_path )

        count += 1 
        print( "count" + str( count ) + "\n" )

    except urllib.error.URLError as e:
        pass
    except urllib.error.HTTPError as e:
        pass
    except Exception as e:
        print(e)


###############################################
# link crawler and image donwload section
###############################################
# create directory
if not os.path.exists(images_save_dir):
    os.makedirs(images_save_dir)

print(images_save_dir)

images_sqaures = driver.find_elements('xpath', image_sqaure_xpath)

for image_sqaure in images_sqaures:

    image_download_link = image_sqaure.get_attribute(link_save_item)

    # print(image_download_link)
    # print("########## image download link ############### \n")

    if link_save_item_attr is not None:
        try:
            image_download_link = json.loads(image_download_link)[link_save_item_attr]
        except Exception as e:
            print(e)
    
    download_image(image_download_link, images_save_dir, count,search_keys)

    image_links.add(image_download_link)
    # print(image_links)


###############################################
# link save section
###############################################

# create directory
if not os.path.exists(link_save_dir):
    os.makedirs(link_save_dir)

# save links
links_file = os.path.join(link_save_dir, search_keys + '.csv')
links_df = pd.DataFrame(data=list(image_links), columns=['links'])

links_df.to_csv(links_file, index=False)
print(links_file)



###############################################
# driver quit
###############################################

time.sleep(6000) # Let the user actually see something!

driver.quit()