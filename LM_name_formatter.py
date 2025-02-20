def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
print("Here are some examples of musicians' full names:")
musician = get_formatted_name('jimi', '', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')  
print(musician)
# ask for user to input first name
user_first_name = input("Please enter your favorite musician's first name: ")
# ask user to input middle name
user_middle_name = input("Please enter your favorite musician's middle name: ")
if user_middle_name == '':
    user_middle_name = None
# ask user to input last name
user_last_name = input("Please enter your favorite musician's last name: ")
if user_last_name == '':
    user_last_name = None
print(f"Your favorite musician is {get_formatted_name(user_first_name, user_middle_name, user_last_name)}")
