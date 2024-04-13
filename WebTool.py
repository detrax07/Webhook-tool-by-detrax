import os
import requests
import time
import colorama
import gratient
import fade
from discord import SyncWebhook
from dhooks import Webhook, File 

os.system("title 𝘿𝙀𝙏𝙍𝘼𝙓 𝙒𝙀𝘽𝙃𝙊𝙊𝙆 𝙏𝙊𝙊𝙇")

def menu():
    print(fade.greenblue("""


 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░                   ░ ░      ░ ░      ░  ░
                      ░                                                                        

by  d e t r a x

Choose an option: 
                          ---------------------------
                         |                           |
                         | [1]-Webhook spammer       |                               
                         | [2]-Webhook info          |
                         | [3]-Webhook Deleter(soon) |
                         |                           |
                          ---------------------------                
                            """))
menu()                            
option = int(input(gratient.purple("Enter your Webhook Option: ")))

while option != 0:
    if option == 1:
        print(gratient.green("Webhook spammer has been selected."))
        time.sleep(2)
        os.system("cls")
        print()
        menu()

        loop = "Y"
        webhook = input(gratient.purple("Enter the discord webhook here: "))
        text = input(gratient.purple("Enter the spamming text: "))

        payload = {
            "content": f"{text}"
            }

        loop = input(gratient.purple("start spamming? (Y/N): ")).capitalize()

        while loop =="Y":
            print("Spamming", text, "to webhook")
            response = requests.post(webhook, json=payload)
            print(gratient.purple("message sent successfully!"))

        else:
            print(gratient.purple("Message failed to send! can not connect to the webhook."))
            time.sleep(3)
            exit()

    elif option == 2:
        print(gratient.green("Webhook Info Selected."))
        time.sleep(2)
        os.system("cls")
        print()
        menu()

        hook = Webhook(input(gratient.purple(" WEBHOOK : ")))
        hook.get_info()
        print(gratient.blue(f"\n GUILD ID    : {hook.guild_id}"))
        print(gratient.blue(f" CHANNEL ID  : {hook.channel_id}"))
        print(gratient.blue(f" USERNAME    : {hook.default_name}"))
        print(gratient.blue(f" IMAGE       : {hook.default_avatar_url}"))
    else:
        print(gratient.red("Invalid Option."))

    print()
    menu()
    option = int(gratient.purple("Enter your webhook option: "))    





                        


