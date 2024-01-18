import requests

url = "https://www.google.com/search?q=software+developer&rlz=1C1VDKB_enCA1062CA1062&oq=google+jobs&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhAMgYIAhBFGEDSAQgxNzA0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwivtqXSis6DAxWZGDQIHbOpDjYQudcGKAF6BAgYECo&sxsrf=ACQVn09VkgyrBns9RFWfHC3Pf3b5UzKf0w:1704726916330#fpstate=tldetail&htivrt=jobs&htidocid=f7uKJQh7xVlw0FCfAAAAAA%3D%3D"

page = requests.get(url)
content = page.text

with open('test2.html', 'w', encoding="utf-8") as file:
    file.write(page.text)