import requests

def get_cat():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    categories = r.json()
    for i in categories:
        print(i["name"])