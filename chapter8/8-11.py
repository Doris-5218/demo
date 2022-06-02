def show_magicians(names):
    for name in names:
        print(name.title())
def make_magicians(names):
    for name in names:
        meg = f" the Greeat {name.title()}"
        print(meg)
magicians = ["doris","john","joe"]
make_magicians(magicians[:])
show_magicians(magicians)

print(magicians)