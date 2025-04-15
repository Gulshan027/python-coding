travel_log=[
    {
        "country":"france",
        "visits":4,
        "cities":["Paris",'lille']

    },
    {
        "country":"germany",
        "visits":5,
        "cities":["berlin",'hemburg']
    }
]
country=input("country: ")
visits =int(input("visits: "))
list_of_cities=eval(input("cities"))

def entry(country,visits,list_of_cities):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["list_of_cities"]=list_of_cities

    travel_log.append(new_country)
    print(travel_log)

entry(country,visits,list_of_cities)



