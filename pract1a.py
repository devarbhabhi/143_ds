myarray = [22, 4, 16, 38, 13]
choice = 0
while True:
    print("\nThe array 'myarray' has the following elements:", myarray)
    print("\nARRAY OPERATIONS:")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Merge an array with the given array")
    print("4. Modify an existing element")
    print("5. Delete an existing element by its position")
    print("6. Delete an existing element by its value")
    print("7. Sort the array in ascending order")
    print("8. Sort the array in descending order")
    print("9. Reverse an array")
    print("10. Search the element in the given array")
    print("11. Display the array")
    print("12. Exit")

    choice = int(input("\nEnter your choice (1-12): "))

    if choice == 1:
        element = int(input("Enter the element to be appended: "))
        myarray.append(element)
        print("The element has been appended.\n")

    elif choice == 2:
        element = int(input("Enter the element to be inserted: "))
        pos = int(input("Enter the position: "))
        myarray.insert(pos, element)
        print("The element has been inserted.\n")

    elif choice == 3:
        newarray = list(map(int, input("Enter the elements (separated by commas): ").split(',')))
        myarray.extend(newarray)
        print("The arrays have been merged.\n")

    elif choice == 4:
        pos = int(input("Enter the position of the element to be modified: "))
        if pos < len(myarray):
            newelement = int(input("Enter the new element: "))
            oldelement = myarray[pos]
            myarray[pos] = newelement
            print("The element", oldelement, "has been modified to", newelement, ".\n")
        else:
            print("Position is out of bounds.\n")

    elif choice == 5:
        pos = int(input("Enter the position of the element to be deleted: "))
        if pos < len(myarray):
            element = myarray.pop(pos)
            print("The element", element, "has been deleted.\n")
        else:
            print("Position is out of bounds.\n")

    elif choice == 6:
        element = int(input("Enter the element to be deleted: "))
        if element in myarray:
            myarray.remove(element)
            print("The element", element, "has been deleted.\n")
        else:
            print("The element is not present in the array.\n")

    elif choice == 7:
        myarray.sort()
        print("The array has been sorted in ascending order.\n")

    elif choice == 8:
        myarray.sort(reverse=True)
        print("The array has been sorted in descending order.\n")

    elif choice == 9:
        myarray.reverse()
        print("The array has been reversed.\n")

    elif choice == 10:
        element = int(input("Enter the element to search: "))
        if element in myarray:
            index = myarray.index(element)
            print("The element", element, "is found at index", index, ".\n")
        else:
            print("The element is not present in the array.\n")

    elif choice == 11:
        print("The current array is:", myarray, "\n")

    elif choice == 12:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.\n")
