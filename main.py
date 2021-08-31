import requests
from dotenv import load_dotenv
import os

load_dotenv("/home/kali/Documents/vars.env")

sheety_token = os.getenv("SHEETY_TOKEN")

print("Welcome to the Flight Club. We'll require some details in order to send you cheap flight prices.\n")

respondeu = False

while not respondeu:
    nome = input("Please insert your name:\n")

    mail = input("Please insert your mail adress:\n")

    mail2 = input("Confirm your mail address:\n")

    if mail == mail2 and nome and mail and mail2:
        respondeu = True
        endpoint = "https://api.sheety.co/b8c398efa9867737110d0d6532a3b2a0/voos/people"
        headers = {
            "Authorization": f"Bearer {sheety_token}"
        }

        print(sheety_token)
        json = {
            "person": {
                "nome": nome,
                "email": mail
            }
        }

        print(json)

        resp = requests.post(url=endpoint, json=json, headers=headers)

        resp.raise_for_status()
        print("We have successfully added you to the mailing list, thank you!")
    else:
        print("Something went wrong. Please insert your details correctly.\n\n")

