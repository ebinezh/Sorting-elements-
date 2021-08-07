# to sort the elements in a list
n = int(input("Enter the size of the list: "))
print("Enter the elements:")
list = []
for i in range(0, n):
    list.append(int(input()))
print("Entered elements are", list)
for i in range(1, len(list)):
    j = i
    while j > 0 and list[j - 1] > list[j]:
        temp = list[j]
        list[j] = list[j - 1]
        list[j - 1] = temp
        j-= 1
print("Sorted List: ", list)

# thanks for watching
# like, share & subscribe to
# Dream2code
