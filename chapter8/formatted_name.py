def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
#f是在告訴後面的字串要印出的是變數("{變數}")
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    print(first_name.title(),middle_name.title(),last_name.title())
get_formatted_name('jimi', 'hendrix')
get_formatted_name('john', 'hooker', 'lee')