import requests

token = 'sus'

headers = {"Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

def update_status(text, emoji, emoji_id): 
    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, data={
        "status":"online","custom_status":{"text":text,"emoji_id":int(emoji_id),"emoji_name":emoji}
                                                                                            })
    
    if r.status_code == 200:
        print("Status updated")
    else:
        print("Error updating status")
        print(r.text)
    
while True:
#   update_status("Message", ":emoji_name:", "123456789 emoji id")
    update_status("rekt", "02heh", "643505002387865620")
    update_status("certified discord tos follower", "CatKiss", "857364278176907275")
    update_status("https://namemc.com/unpacks", "Minecraft", "811260964813013012")
    update_status("https://hypixel.one", "CatKiss", "857364278176907275")

