#dictionary
dict={
    "bug":"An error in a program",
    "function":"A piece of code that you can easily"

}
#retrieving items from dict dictionary
print(dict["bug"])

#adding
dict["loop"]="the action of doing something again and again."

print(dict)

#wipe an existing dictionar
# dict={}
# print(dict)


#edit an item
dict["bug"]="hello bug"
print(dict)


#loop through a dictionary
for thing in dict:
    print(thing)
    print(dict[thing])