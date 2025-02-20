first_name = input("Please enter your first name. ")
middle_name = input("Please enter your middle name (press Enter if none). ").strip()
last_name = input("Please enter your last name. ")

def get_formatted_name(first_name, middle_name, last_name):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name(first_name, middle_name, last_name)) 
