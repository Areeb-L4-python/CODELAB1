# Invite somee people to dinner.
guests = ['dean','jess','logan']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry," + name + "cant make it to dinner.")

#jess cant make it! Lets invite Max instead.
del(guests[1])
guests.insert(1,'Max')

#Print the invitations again.
name = guests[0].title()
print("\n" + name +",Please come to dinner.")

name = guests[1].title()
print(name + ",please come to dinner.")

name = guests[2].title()
print(name + ",please come to dinner.")
