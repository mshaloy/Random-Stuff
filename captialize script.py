"""This script takes in a string and capitalizes the first letter of every word, excepting some
(but not all) articles, prepositions, or conjunctions. Exit with 0"""

#Written to deal with article titles in all caps for mla citation formatting
#because I didn't want to do it by hand anymore. Not perfect
#but it saves me a lot of time. Not actively maintained at this time
#Usage:
#String: Houston, we have a problem…or do we? The trajectory of astrobioethics and Indigenous thought
#Houston, We Have a Problem…or Do We? the Trajectory of Astrobioethics and Indigenous Thought
#String: 0

list = ["a", "the", "an", "for", "and", "nor", "but", "or", "yet", "so", "of", "not", "as", "at", "by",
        "in", "on", "to", "up"]
def string_cap(str_1):
    str_part = str_1.split(' ')
    for i in range(len(str_part)):
        if(str_part[i] not in list or i==0):
            str_part[i] = str_part[i].capitalize()
    cap_str = ' '.join(str_part)
    print(cap_str)
str_to_capitalize = input("String: ")
while(str_to_capitalize != "0"):
    string_cap(str_to_capitalize.lower())
    str_to_capitalize = input("String: ")
