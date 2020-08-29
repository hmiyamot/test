#!/usr/bin/python

import sys


call_printer = {
    "1": " is in your list!",
    "2": "Kai is on your list!",
    "3": "Kai Asamori is on your list!",
    "4": "No Gilbert looks like Samuel so ew!",
    "5": " is not on your list!",
    "6": "Now exiting",
    "7": " isn't a command!"
}


who_are_you = {
    "all friends": "1",
    "search friend": "2",
    "none!": "3",
    "no one": "4",
    "no-one": "5",
    "nobody": "6",
    "none": "7",
    "kai": "8",
    "Kai": "9",
    "kai asamori": "10",
    "asamori Kai": "11",
    "asamori Kai":"12",
    "none!": "13"
}

sys.stdout.write("Who are you? :")
input_date = str(raw_input().strip())
number = who_are_you[input_date]
print_stdr = call_printer[number]
print(input_date + print_stdr)
