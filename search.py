#!/usr/bin/python

import sys


call_printer = {
    "1": " is in your list!",
    "2": "Tom is on your list!",
    "3": "Tom Brank is on your list!",
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
    "tom": "8",
    "Tom": "9",
    "tom brank": "10",
    "brank Tom": "11",
    "none!": "13"
}

sys.stdout.write("Who are you? :")
input_date = str(raw_input().strip())
number = who_are_you[input_date]
print_stdr = call_printer[number]
print(input_date + print_stdr)
