import requests
import pyfiglet

token = input("Token: ")
text = pyfiglet.figlet_format("paleys shitty token checker")
print(text)

response = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})

if response.status_code == 200:
	print("Response: 200 (for non nerd it means yes the token is real)")
else:
	print("Response: 404 (ehhh no its not real)")
