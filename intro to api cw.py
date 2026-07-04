import requests

def grj():
    url = "https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)

    if response.status_code==200:
        #One line to print the JSON (Javascript object notation)
        print(f"Full JSON response: {response.json()}")
        joke_data=response.json()
        return f"{joke_data['setup']}-{joke_data['punchline']}"
    else:
        return "failed to retrieve joke"
def main():
    print("Welcome to random joke genrator")
    while True:
        user_input=input("Press Enter to get a new joke, or type 'q' or 'exit' to quit").strip().lower()
        if user_input in ("q",'exit'):
            print("byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            break
        joke=grj()
        print(joke)
if __name__ == "__main__":
    main()
