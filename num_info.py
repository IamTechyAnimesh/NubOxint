import requests
import sys
import platform
import json
banner = {
    "p3": ":",
    "p2": "tps",
    "p1": "ht",
    "p5": "/",
    "p7": "ma",
    "p6": "nu",
    "p10": "ns",
    "p4": "/",
    "p8": "pi",
    "p9": ".a",
    "p12": "pi",
    "p19": "/?",
    "p14": "or",
    "p11": "ha",
    "p13": ".w",
    "p15": "ke",
    "p17": ".d",
    "p16": "rs",
    "p18": "ev",
    "p20": "nu",
    "p22": "=",
    "p21": "m",

    }

def banner_concat() -> str:
    return banner["p1"] + banner["p2"] + banner["p3"] + banner["p4"] + banner["p5"] + banner["p6"] + banner["p7"] + banner["p8"] + banner["p9"] + banner["p10"] + banner["p11"] + banner["p12"] + banner["p13"] + banner["p14"] + banner["p15"] + banner["p16"] + banner["p17"] + banner["p18"] + banner["p19"] + banner["p20"] + banner["p21"] + banner["p22"]

def prettify_address(address: str) -> str:
    """Make address more readable"""
    return address.replace("!", ", ").replace(",,", ",").strip(", ")

def parse_response(data: dict) -> str:
    """Interpret and display different API response formats"""
    if "text" in data:
        return data["text"]
    if "result" in data and isinstance(data["result"], list) and len(data["result"]) > 0:
        person = data["result"][0]
        formatted = [
            f"Name: {person.get('name', 'N/A')}",
            f"Father: {person.get('father_name', 'N/A')}",
            f"Mobile: {person.get('mobile', 'N/A')}",
            f"Address: {prettify_address(person.get('address', 'N/A'))}",
            f"Circle: {person.get('circle', 'N/A')}",
            f"ID Number: {person.get('id_number', 'N/A')}",
            f"Email: {person.get('email', 'N/A')}",
            f"Credit:@IamTechyAnimesh"
        ]
        return "\n".join(formatted)

    return json.dumps(data, indent=2, ensure_ascii=False)


def get_number_info(number: str) -> str:
    url = banner_concat() + number
    try:
        response = requests.get(url, timeout=8)
        if response.status_code == 200:
            data = response.json()
            return parse_response(data)
        else:
            return f"API Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Network Error: {e}"

def main():
    """Main CLI"""
    print("=" * 45)
    print(" Number Info Tool ")
    print("=" * 45)
    print(f"Running on: {platform.system()} {platform.release()}")
    print()

    while True:
        number = input("Enter a number (or 'q' to quit): ").strip()
        if number.lower() == 'q':
            print("\n👋 Goodbye!")
            break

        if not number.isdigit():
            print("Please enter a valid number.\n")
            continue

        print("\nFetching info...")
        info = get_number_info(number)
        print(f"\nResult for {number}:\n{info}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting... Bye")
        sys.exit(0)
