# # Greet the world
# print('Hello world!')
#
# # Take user's name and print it
# name = input("What's your name? ")
# print(type(name))
# print('Hello', name, sep=":)")
# print("Hello \"friend\"")
#
# # f-strings
# print(f"Hello {name}")
#
# # String methods
# name = name.strip()
# name = name.capitalize()
# name = name.title()
# print(name)

# Style
name = input("Enter you name: ").strip().title().split('-')
print(name)

