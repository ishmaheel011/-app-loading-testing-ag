#Kgosi Ntlakana
#19 May 2023

import requests

def getURL(url):
    '''takes a URL and makes an http request for it, if request is successful, content information is displayed, else error message is displayed'''
    try:
        response = requests.get(url)
        print(f"URL {url} successfully requested, content information...")
        for i in response.headers:
            print(f"{i} : {response.headers[i]}")

    except:
        print(f"could not fetch {url}")

def main():
    url = input("enter a URL to fetch or press enter to fetch default example.com\n")
    x = len(url)>0
    if not x:
        url = "http://example.com/"
    getURL(url)

if __name__ == "__main__":
    main()
