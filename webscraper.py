from bs4 import BeautifulSoup
import requests

html_file = "test2.html"

#with open('test2.html', 'r', encoding="utf-8") as file:
#    contents = file.read()
#    soup = BeautifulSoup(contents, "lxml")
#    transcript = soup.find_all("span", class_="HBvzbc")

url = "https://www.google.com/search?q=software+developer&rlz=1C1VDKB_enCA1062CA1062&oq=google+jobs&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhAMgYIAhBFGEDSAQgxNzA0ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwivtqXSis6DAxWZGDQIHbOpDjYQudcGKAF6BAgYECo&sxsrf=ACQVn09VkgyrBns9RFWfHC3Pf3b5UzKf0w:1704726916330#fpstate=tldetail&htivrt=jobs&htidocid=f7uKJQh7xVlw0FCfAAAAAA%3D%3D"

page = requests.get(url)
content = page.text
soup = BeautifulSoup(content, "lxml")
transcript = soup.find_all("span", class_="HBvzbc")
#transcript = transcript.get_text(strip=True, separator=' ')
text = []

for x in transcript:
    text.append(str(x))
    print(x)


with open('test.txt', 'w', encoding="utf-8") as file:
    for x in text:
        file.write(str(x))
