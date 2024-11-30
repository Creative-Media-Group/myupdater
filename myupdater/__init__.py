import requests


def updater(file_url, version=""):
    r = requests.get(url=file_url)
    return r


def writeversion(filepath, version):
    with open(file=f"{filepath}/VERSION", mode="w+") as f:
        f.write(version)


if __name__ == "__main__":
    print(updater(file_url=""))
