

def full_name(**names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']}"
    else:
        return f"{names['first']} {names['last']}"
    

print(full_name(first="Bob", last = "Builder"))
print(full_name(first = "Jimmy", middle = "Bob", last = "Jeremy"))