import requests,datetime,json,wikipedia
from googlesearch import search

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
    print("The current temperature is:" +str(current_temp)+" degrees celcius."
        +"\nThe current pressure is:" +str(current_pressure)+" in hPa units."
        +"\nThe current humidity is:" +str(current_humidity)+"%"
        +"\nDescription:" +weather_description)
#WEATHER REQUEST ENDS

## FOR JOKE REQUESTS
def joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    x=response.json()
    joke_setup=x["setup"]
    joke_punchline=x["punchline"]
    print("You do realize you could just use Alexa instead. But fine, have your joke."
        +"\n"+joke_setup+"\n..."+joke_punchline)
#JOKE REQUESTS ENDS

##FOR GOOGLE SEARCH
def google_it_for_me():
    google_query=input("\nWhat's your query? I'll return some nice links!\n")
    for j in search(google_query, tld="com", lang='en', num=10, start=0, stop=1, pause=1.5):
        print(j)
#GOOGLE SEARCH ENDS

##FOR WIKIPEDIA SUMMARY
def search_wikipedia_for_me():
    wikipedia_query=input("\nWho or what do you want to search for?\n")
    print (wikipedia.summary(wikipedia_query, sentences=4))
#WIKIPEDIA FUNCTION ENDS

# ASK QUERY AND CALL FUNCTIONS
query=input("\nHey Panda. How can I help?\n")
if "weather" in query:
    print("Sure, I'll fetch the weather real quick.")
    weather()
elif "time" in query:
    print(datetime.datetime.now())
elif "joke" in query:
    joke()
elif "google" in query:
    google_it_for_me()
elif "wikipedia" or "description" in query:
    search_wikipedia_for_me()
else:
    print("Not a valid query.")
