#Name: Lovissa Price
#Prog Purpose: this program demonstrates how to use lists, including:
#   finding number of items in the list, sorting the list, adding/deleting items,
#   copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle", "Gonzo", "Sweetie-Pie", "Diego"]

dogs2 = []

def main():
    how_many = len(dogs)
    print("\nNumber of dogs in the list, using len(): " + str(how_many))
    print("\nOriginal list of dog names: ")
    print(dogs)
    pause()

    dogs.reverse()
    print("\nList from last to first, using list(): ")
    print(dogs)
    pause()

    dogs.sort()
    print("\nAlphabetized list of dogs, using sort(): ")
    print(dogs)
    pause()

    dogs.sort(reverse = True)
    print("\nList in reverse alphabetized order, using (reverse = True): ")
    print(dogs)
    pause()

    dogs.append("Ranger")
    print("\nAdd a dog name to the end of this list, using append(): ")
    print(dogs)
    pause()

    doggy = dogs.pop(0)
    print("\nRemove a dog from the front of the list, using pop()")
    print(dogs)
    print(doggy + " was removed from the front of the list")
    pause()

    another_dog = dogs.pop(3)
    print("\nRemove another dog from the list at position 3 (dog 4 on the list), using pop(index-here)")
    print(dogs)
    print(another_dog + " was removed from position 3 of the list")
    pause()

    dogs.remove("AnnaBelle")
    print("\nRemove a dog from the list by name rather than position number, using remove(name-here)")
    print(dogs)
    pause()

    dogs2 = dogs
    print("\nA list can be added to another list by setting them equal to eachother.")
    print("Dogs: ")
    print(dogs)
    print("Dogs2: ")
    print(dogs2)
    pause()

    print("\nUse a FOR loop to give each dog in the list the same last name:")
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Price"
    print(dogs)

def pause():
    press_enter = input("\nPress ENTER to continue...")

main()
    

    
