#!/usr/bin/python

import sys


call_printer = {
    "1": " is in your list!",
    "2": "Tom is on your list!",
    "3": "Tom Brank is on your list!",
    "4": "No Gilbert looks like Samuel so ew!",
    "5": " is not on your list!",
    "6": "Now exiting",
    "7": " isn't a command!",
    "8": "Nobody is here"
}


who_are_you = {
    "all friends": "1",
    "search friend": "1",
    "none!": "2",
    "no one": "2",
    "no-one": "3",
    "nobody": "3",
    "none": "4",
    "tom": "4",
    "Tom": "5",
    "tom brank": "6",
    "brank Tom": "7",
    "none!": "8"
}

sys.stdout.write("Who are you? :")
input_date = str(raw_input().strip())
number = who_are_you[input_date]
print_stdr = call_printer[number]
print(input_date + print_stdr)
