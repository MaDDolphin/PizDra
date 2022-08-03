#https://pozdravok.com/pozdravleniya/lyubov/dobroe-utro/korotkie/proza-17.htm
#https://pozdravok.com/pozdravleniya/lyubov/dobroe-utro/74.htm

import shutil
import requests
from bs4 import BeautifulSoup
import os


def read_file(filename):
    with open(filename, encoding='utf-8') as input_file:
        text = input_file.read()
    return text


def html_req():
    i = 1
    for page_nmb in range(1, 75):
        print(page_nmb)
        url = 'https://pozdravok.com/pozdravleniya/lyubov/dobroe-utro/%d.htm' % page_nmb
        r = requests.get(url)
        with open('./pages/' + str(i) + '.html', 'w', encoding="utf-8") as output_file:
            output_file.write(r.text)
        i += 1



def photo_parse(filename, links):
    try:
        text = read_file(filename)
        soup = BeautifulSoup(text)
        photo_list = soup.find('div', {'class': 'content'})
        photos = photo_list.find_all('p', {'class': 'sfst'})
        i = 0
        for photo in photos:
            photo=str(photo)
            a = photo.find('">')
            print(a)
            b = photo.rfind('<')
            photo = photo[a+2:b]
            print(photo)
            photo.replace('<br/>', ' ')
            print(photo)
            '''
            while os.path.exists('./bg/' + str(i) + '.jpg'):
                i = i+1
            link = photo.find('img', {'class': 'wallpapers__image'}).get('src').replace('168x300', '480x854')
            print(link)
            img_data = requests.get(link).content
            with open('./bg/'+str(i)+'.jpg', 'wb') as handler:
                handler.write(img_data)

            links.append(link)    '''
    except:
        print(filename)





def main():
    tags = ["макро"]
    folder = './pages'
    '''
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    html_req()'''
    links = []

    for root, dirs, files in os.walk('./pages'):
        for file in files:
            photo_parse('./pages/' + file, links)

if __name__ == "__main__":
    main()