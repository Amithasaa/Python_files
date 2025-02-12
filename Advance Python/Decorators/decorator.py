
def decor(func):
    def inner(name):
        if name == "Ayush":
            print(name, "is Learning Java")
        else:
            func(name)
    return inner

@decor
def choice(name):
    print(name, "is Learning python")
choice("Akash")
choice("Ayush")
choice("Neha")


