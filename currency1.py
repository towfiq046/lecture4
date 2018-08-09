import requests

def main():
    result = requests.get("http://data.fixer.io/api/latest?access_key=df63a18c1b1fbb8e020b75bb6db79f1a&base=EUR&symbols=BDT")

    if result.status_code != 200:
        raise Exception("Error: unsuccessful API request.")

    data = result.json()
    rate = data["rates"]["BDT"]
    print(f"1 EUR = {rate} BDT")

if __name__ == "__main__":
    main()
