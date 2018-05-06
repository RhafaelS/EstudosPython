responses = {}

polling_active = True

def show_data(name, mountain):
    print(name + " would like to climb " + response + ".")

while polling_active:
    name = input("\nWhats is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False


print("\n--- Poll Results ---")
for name, response in responses.items():
    show_data(name, response)