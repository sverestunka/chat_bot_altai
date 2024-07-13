import requests

def altai_foto():
    api_key = "7okDTNFNIXmIA5CKgNfbNQJ5sdoy2IbzWD42CFS0Snk"
    url = "https://api.unsplash.com/photos/random?query=altai-mountains"

    headers = {"Authorization": "Client-ID " + api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        return json_response["urls"]["small"]
    else:
        return None


if __name__ == '__main__':
    altai_foto()
