import requests


def updater(file_url, version=""):
    r = requests.get(url=file_url)
    return r


if __name__ == "__main__":
    updater()
