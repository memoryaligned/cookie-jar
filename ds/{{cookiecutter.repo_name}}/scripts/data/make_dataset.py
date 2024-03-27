from urllib import request

url = ""
filename = ""

if __name__ == "__main__":
    request.urlretrieve(url, f"data/raw/{filename}")
