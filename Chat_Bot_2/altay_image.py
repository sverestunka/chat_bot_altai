import requests

def searchPhotos():
    url = 'https://ru.freepik.com/search?ai=excluded&format=search&last_filter=query&last_value=altai&query=altai&type=photo'
    altay_photo = requests.get(url)
    if altay_photo.status_code:
        data = altay_photo.json()
        return data.get('image')
        print(data.get('image'))

if __name__ == '__main__':
    searchPhotos()