import requests
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def grf():
    response=requests.get(url)
    if response.status_code == 200:
        fact_data=response.json()
        print(f"Did you know? {fact_data["text"]}")
    else:
        print("failed to fetch fact")
while True:
    user_input=input("Press eneter to get a random  fact or press q to quit")
    if user_input.lower() =='q':
        break
    grf()
