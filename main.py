import requests, time, os

token = os.environ['token'] # your discord token
delay = os.environ['delay'] # delay in seconds
ratelimitdelay = os.environ['ratelimitdelay'] # how long to wait before trying to update status again

headers = {"Authorization": token,
            "content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1HQiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTQ3NjE2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}


def update_status(text, emoji, emoji_id): 
    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json={
        "status":"online","custom_status":{"text":text,"emoji_id":int(emoji_id),"emoji_name":emoji}
                                                                                            })
    
    if r.status_code == 200:
        #print("Status updated")
        time.sleep(int(delay))
    elif r.status_code == 401:
        print("Invalid token")
        input('')
        exit()
    elif r.status_code == 429:
        print("Too many requests")
        time.sleep(ratelimitdelay)
    else:
        print("Error updating status")
        print(r.status_code)
        print(r.text) # ez debug

while True:
#   update_status("Message", ":emoji_name:", "123456789 emoji id")
    update_status("i'm only a fool for you", "ctks", "925798465529872385")
    update_status("best bedwars player (real)", "ctks", "925798465529872385")
    update_status("https://xeny.uk", "ctks", "925798465529872385")
    update_status("i'm a bot (jk)", "ctks", "925798465529872385")
    update_status("https://youtu.be/f6iV6eK5dC4", "ctks", "925798465529872385")
    update_status("catboys >> ", "ctks", "925798465529872385")
    update_status("zzzzz", "ctks", "925798465529872385")
    update_status("I wonder what the CIA's opinion is on yaoi.", "ctks", "925798465529872385")


