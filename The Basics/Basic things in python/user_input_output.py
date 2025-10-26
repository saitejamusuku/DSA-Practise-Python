x = input("Enter Something:") # Takes input from the user and stores it in variable x

num = int(input("Enter a number:")) # Takes input from the user, converts it to an integer, and stores it in variable num

lis = list(map(int, input("Enter space-separated numbers:").split()))# Takes space-separated input from the user, splits it, converts each part to an integer, and stores it in lis

print(x, sep=' ', end=" ")

print(num) #prints the number


print(lis) #prints the list as it is
print(*lis, sep=' ') # Unpacks the list and prints each element separated by space