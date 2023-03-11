from termcolor import colored
from pyfiglet import figlet_format
import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

print(colored(figlet_format("Dad Joke 3000"), color="cyan"))

topic = input("Let me tell you joke. Give me a topic: ")

response = requests.get(
    url, 
    headers = {"Accept": "application/json"},
    params = {"term": topic}
    ).json()
result = response["results"]
# print(result[0]["joke"])

if len(result) == 0:
    print(f"Sorry, I don't have any jokes about {topic}")
elif len(result) == 1:
    print(f"I've got one joke about {topic}. Here it is: ")
    print(result[0]["joke"])
else:
    print(f"I've got {len(result)} jokes about {topic}. Here is one: ")
    print(choice(result)["joke"])





