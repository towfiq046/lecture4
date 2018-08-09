import requests

def main():
    # prompt the user.
    #base = input("First Currency: ")   BASE CAN NOT BE CHANGED. ACCESS IS RESTRICTED. may be free account.
    target = input("Enter Currency: ")

    result = requests.get("http://data.fixer.io/api/latest?access_key=df63a18c1b1fbb8e020b75bb6db79f1a",
                            params={"base": "EUR", "symbols": target})   # parameterizing the url.

    if result.status_code != 200:
        raise Exception("Error: unsuccessful API request.")

    # doesn't work.
    data = result.json()
    if data["success"] == False:
        raise Exception("Error: Invalid currency.")


    rate = data["rates"][target]
    print(f"1 EUR = {rate} {target}")

if __name__ == "__main__":
    main()
