'''
Problem 1: Festival Lineup
    Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.
    An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

 Using AI Dictionaries - dictionary is a built-in data structure that stores data as a collection of key-value pairs. 
 Think of it like a real-world dictionary where you look up a word (the key) to find its definition (the value)

 Dictionary functions -- 
    .get(key) - checks if the vlaue of a key exsists or gets it
    .update({}) - used to update keys or dictionary items
    .pop(key) - Removes a key-value pair from the dictionary and returns the corresponding **value
    .popitem() - Removes and returns the last inserted key-value pair as a tuple **(key, value)
    .clear() - Removes all key-value pairs from the dictionary, making it empty
    .keys() - Prints all of the keys in the dictionary
    .values() - Prints all the values in the dictionary
    .items() - Returns a view object that displays a list of a dictionary's key-value pairs as tuples (key, value)

 The zip() function creates pairs: ('name', 'Alice'), ('age', 30), etc.
 The dict() constructor then turns these pairs into a dictionary.
 hash_map = dict(zip(keys, values))
'''


def lineup(artists, set_times):
    # Created HashMap
    hash_map_artist = dict(zip(artists, set_times))
    # Printed HashMap
    print(hash_map_artist)
    print(hash_map_artist.get("Kendrick Lamar"))

# Created Lists with artists and times
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# Called Hashmap with 
lineup(artists1, set_times1)

