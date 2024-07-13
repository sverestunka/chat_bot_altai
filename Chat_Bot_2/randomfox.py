import requests

def fox():
    url = "https://randomfox.ca/floof/"
    imagefox = requests.get(url)
    if imagefox.status_code:
        data = imagefox.json()
        return data.get('image')

        # print(data.get('image'))
    # print(data)
    # print(imagefox.status_code)

if __name__ == '__main__':
    fox()

# 200-300- все ок
# 400 - ошибки баз
# 500 - ошибки на сервере