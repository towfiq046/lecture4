import requests

def main():
    result = requests.get("http://data.fixer.io/api/latest?access_key=df63a18c1b1fbb8e020b75bb6db79f1a&base=EUR&symbols=BDT,INR")

    if result.status_code != 200:
        # if anything goes wrong.
        raise Exception("ERROR: API request unsuccessful.")

    data = result.json()    # extracting json data as it was fetched as query result.
    print(data)

if __name__ == "__main__":
    main()
