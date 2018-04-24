# -*- coding: UTF-8 -*-
"""
I'm in UR exam.

This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.

You've got an hour.
"""
import string
import time
import json


def greet(name="Towering Timmy"):
    """Return a greeting.

    return a string of "Hello" and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    return "Hello " + name


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.

    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    count = 0 
    for i in input_list:
        if i == 3:
            count += 1
    
    return count



def fizz_buzz():
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
            from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special, and a string
    if it is. E.g. [1, 2, "Fizz", 4, "Buzz", 6, 7, ...]
    """
    fizzBuzzList = []
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("Fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("Buzz")
        else:
            fizzBuzzList.append(i)
    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.

    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: make sure that you have a pipe on both ends of the string.
    """
    input_string = "|".join(input_string)
    input_string = "|" + input_string + '|'

    return input_string


def pet_filter(letter="a"):
    """Return a list of animals with `letter` in their name."""
    pets = ["dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken",
            "guinea pig", "donkey", "duck", "water buffalo",
            "western honey bee", "dromedary camel", "horse", "silkmoth",
            "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca",
            "guineafowl", "ferret", "muscovy duck", "barbary dove",
            "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi",
            "canary", "society finch", "fancy mouse", "siamese fighting fish",
            "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"]
    letter_pet = []
    for pet in pets:
        if letter in pet:
            letter_pet.append(pet)
    return letter_pet

def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string
    the_alphabet = string.ascii_lowercase
    max_pet = 0
    for letter in the_alphabet:
         
        if len(pet_filter(letter)) > max_pet:
            max_pet = len(pet_filter(letter))
            max_letter = letter
    return max_letter


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.

    There is a random word generator here:
    "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=3&maxLength=10&limit=1"
    Currently, minLength=3 and maxLength=10 in this url. 
    This means we will get a word between 3 and 10 characters.
    If we set minLength=7 and maxLength=7 like here:
    "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=7&maxLength=7&limit=1"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g. {3: ['cat','pop','cow'], ...}
    Use the API to get the 3 words.
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library
    TIP:
        >>> r = requests.get(url)
        >>> r.json() # will get you a python list containing something like this:
        >>> # [{"id":5651391,"word":"salmony"}]
    """
    import requests
    url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength="
    url2 = "&maxLength="
    url3 = "&limit=3"

    return_dict = {}
    for length in range(3,8):
        r = requests.get(url+str(length)+url2+str(length)+url3)
        r = r.json()
        return_dict[str(length)] = []
        for word in r: 
                return_dict[str(length)].append(word["word"])
    return return_dict
    
def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.

    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library
    Bonus: extra mark if you get the paragraph to start with a
           capital letter and end with a full stop.
    """
    import random
    
    paragraph_words = make_filler_text_dictionary()
    paragraph = ""
    for i in range(number_of_words):
        length = str(random.randint(3, 7))
        word = random.randint(0, 2)
        paragraph = paragraph + " " + paragraph_words[length][word]
    paragraph = paragraph[0].upper() + paragraph[1:]
    paragraph += '.'
    return paragraph


def fast_filler(number_of_words=200):
    """Reimplement random filler text.

    This time, the first time the code runs, save the dictionary to a file.
    On the second run,if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.words"
    TIP: you'll need the os library
    TIP: you'll probably want to use json dumps and loads to get the dictionary
    into and out of the file. Be careful when you read it back in, it'll
    convert integer keys to strings.
    """
    import os
    import json
    import random
    if os.path.isfile("dict_racey.words"):
        paragraph_words = json.load(open("dict_racey.words"))
        paragraph = ""
        for i in range(number_of_words):
            length = str(random.randint(3, 7))
            word = random.randint(0, 2)
            paragraph = paragraph + " " + paragraph_words[length][word]
        paragraph = paragraph[0].upper() + paragraph[1:]
        paragraph += '.'
        
    else:
        paragraph_words = make_filler_text_dictionary()
        with open("dict_racey.words",'w') as f:
            f.write(json.dumps(paragraph_words))
        paragraph = ""
        for i in range(number_of_words):
            length = str(random.randint(3, 7))
            word = random.randint(0, 2)
            paragraph = paragraph + " " + paragraph_words[length][word]
        paragraph = paragraph[0].upper() + paragraph[1:]
        paragraph += '.'
    return paragraph
        
         


if __name__ == '__main__':
    print(greet())
    print(three_counter())
    print(fizz_buzz())
    print(put_behind_bars())
    print(pet_filter()) 
    print(best_letter_for_pets())
    print(make_filler_text_dictionary())
    print(random_filler_text())
    print(fast_filler())
    for i in range(10):
        print(i, fast_filler())
