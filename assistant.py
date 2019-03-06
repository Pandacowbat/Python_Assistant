import requests,datetime,json,wikipedia,os
from googlesearch import search
from gtts import gTTS

def talk_back(text):
    print(text)
    tts=gTTS(text)
    tts.save('audio.mp3')
    os.system('mpg123 -q audio.mp3')
## FOR WEATHER REQUESTS
def weather():
    api_key="bca2453ed5abd8350684b80d66bd95f9"
    city_name = "Bhubaneswar"
    url="https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city_name
    response= requests.get(url)
    x=response.json()
    if x["cod"] != "404":
        y=x["main"]
        current_temp=y["temp"]- 273.15
        current_pressure=y["pressure"]
        current_humidity=y["humidity"]
        z=x["weather"]
        weather_description=z[0]["description"]
        weather_description=str(weather_description)
    else:
        current_temp="0"
        current_pressure="0"
        current_humidity="0"
        weather_description="Enter valid city."
    text=("The current temperature is:" +str(current_temp)+" degrees celcius."
        +"\nThe current pressure is:" +str(current_pressure)+" in hPa units."
        +"\nThe current humidity is:" +str(current_humidity)+"%"
        +"\nDescription:" +weather_description)
    talk_back(text)

#WEATHER REQUEST ENDS

## FOR JOKE REQUESTS
def joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    x=response.json()
    joke_setup=x["setup"]
    joke_punchline=x["punchline"]
    text = ("You do realize you could just use Alexa instead. But fine, have your joke."
        +"\n"+joke_setup+"\n..."+joke_punchline)
    talk_back(text)
#JOKE REQUESTS ENDS

##FOR GOOGLE SEARCH
def google_it_for_me():
    text="\nWhat's your query? I'll return some nice links!\n"
    talk_back(text)
    google_query=input()
    for j in search(google_query, tld="com", lang='en', num=10, start=0, stop=1, pause=1.5):
        print(j)
#GOOGLE SEARCH ENDS

##FOR WIKIPEDIA SUMMARY
def search_wikipedia_for_me():
    wikipedia_query=input("\nWho or what do you want to search for?\n")
    talk_back(wikipedia.summary(wikipedia_query, sentences=4))
#WIKIPEDIA FUNCTION ENDS

# ASK QUERY AND CALL FUNCTIONS
user = "Panda"
talk_back("Hey " +user)
while(True):
    query=input("\nHow can I help?\n")
    if "weather" in query:
        talk_back("Sure, I'll fetch the weather real quick.")
        weather()
    elif "time" in query:
        print(datetime.datetime.now())
    elif "joke" in query:
        joke()
    elif "google" in query:
        google_it_for_me()
    elif ("wikipedia" or "describe") in query:
        search_wikipedia_for_me()
    elif ("exit" or "bye" or "quit") in query:
        print("Until next time.")
        break
    else:
        print("Not a valid query.")
print("Exiting...")