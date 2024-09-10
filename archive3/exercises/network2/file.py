import requests

result = requests.get("https://deishacks-2023.devpost.com/project-gallery")
other_page = requests.get("https://devpost.com/software/narratives-of-innovations-youth-art-exhibition")
print(result.text)