from difflib import get_close_matches
import json
data=json.load(open("data.json"))
def get_the_def(dict_word):
    if dict_word in data:
      print("Here's what I've found for %s." % dict_word)
      return data[dict_word]
    elif len(get_close_matches(dict_word,data.keys()))>0:
       response=input("did you mean %s or %s?please enter 'yes' if you did.\n"  %(get_close_matches(dict_word,data.keys())[0], get_close_matches(dict_word,data.keys())[1]))
       if response=="yes":
           resp1=input("please enter 1 for %s and 2 for %s: "  %(get_close_matches(dict_word,data.keys())[0], get_close_matches(dict_word,data.keys())[1]))
           if resp1=="1":
               return data[get_close_matches(dict_word,data.keys())[0]]
           elif resp1=="2":
               return data[get_close_matches(dict_word,data.keys())[1]]
           else:
               return "no match found for %s" %dict_word
       else:
             return "please check the spelling of the word! No match found for %s" %dict_word
    else:
      return "no match found for %s" %dict_word

dict_word=input("\nplease enter the word:")
dict_w= dict_word.lower()
O=get_the_def(dict_w)
if(type(O)==list):
    for definition in O:
        print(definition)
else:
    print(O)
