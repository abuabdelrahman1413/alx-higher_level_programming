#!/usr/bin/python3
person1_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}
person1_information_filtered = {k: v for k, v in person1_information.items() if v != "Sam"}

print(person1_information_filtered)
