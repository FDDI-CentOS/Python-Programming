import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        response = input("Did you mean %s instead? (Y/N)" % get_close_matches(w,data.keys())[0]).lower()
        if response.lower() == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Sorry your %s response was not valid." %response
    elif len(get_close_matches(w.title(), data.keys())) > 0:
        response = input("Did you mean %s instead? (Y/N)" % get_close_matches(w.title(),data.keys())[0]).lower()
        if response.lower() == 'y':
            return data[get_close_matches(w.title(),data.keys())[0]]
        else:
            return "Sorry your %s response was not valid." %response
    else:
        return("Word not exist. Please double check it and try again.")

word = input("Enter a dictionary search term: ")

output = search(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)