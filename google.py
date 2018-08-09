import requests

def main():
    result = requests.get("https://www.google.com/")
    print(result.text)

if __name__ == "__main__":
    main()
