
def get_formatted_name(first_name, middle_name = '', last_name =''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print('Example Musicians:')
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

print()

print('Name a musician:')
first = input('First name: ')
print('Middle name is optional. press enter to skip.')
# if the user doesn't enter a middle name, it will be an empty string
middle = input('Middle name: ')
last = input('Last name: ')
musician = get_formatted_name(first, middle, last)
print(musician)
