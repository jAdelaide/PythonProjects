print()
names = [
 "bob",
 "mary",
 "larry"
]
        # lists can be done over multiple lines between [ ]

print (names)
print()

names = ["tom", "dick", "harry"]
        # or done on one line, as long as you have the [ ] and , between values

for name in names:
 print("Hello " + name)
        # doesn't work without the space before print here as the indent shows it's with the for loop: that's what it's looking for
        # without the space you will get an error message telling you it expected that
print()

for name in names:
 print("Hello " + name.capitalize())
        # capitalizes the first letter of each item in the list
print()
