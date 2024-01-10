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

# We got a bigger table, so lets add some more prople to the list.
print("\nWe got a bigger table!")
guests.insert(0,'nate')
guests.insert(2,'chuck')
guests.append('finn')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# Oh no, Table wont arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("sorry, "+ name.title()+ "there is no room at the table.")

name = guests.pop()
print("sorry, "+ name.title()+ "there is no room at the table.")

name = guests.pop()
print("sorry, "+ name.title()+ "there is no room at the table.")

name = guests.pop()
print("sorry, "+ name.title()+ "there is no room at the table.")

# There should be two people left. Lets invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)
