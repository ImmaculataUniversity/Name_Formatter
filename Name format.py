def get_formatted_name(first_name, middle_name, last_name):
    '''return a full name, neatly formatted'''
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

fn = input('what is your first name: ')
mn = input('what is your middle name: ')
ln = input('what is your last name: ')
name = get_formatted_name(fn, mn, ln)
print(name)

musician = get_formatted_name('jimi', '', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)