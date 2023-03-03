import requests, json

image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTccAUbsX5rEZUPfzQmOHTb_7fptbxzx2Szvi2akXSGKQ&s'

response = requests.get(image_url)

with open("images/test.jpg", "wb") as file:
    file.write(response.content)