arr = [int(i) for i in input('Enter array : ').split()]
num = int(input("Enter Searching Number : "))
start = 0
end = len(arr)-1
found = False

while start <= end:
    mid = (start+end)//2
    if (arr[mid]==num):
        found = True
        break;
    elif num < arr[mid]  :
        end = mid - 1
    
    else:
        start = mid + 1
print(found)
if found:
    print(f"Value Present {num}")
else:
    print(f"Value Not Present {num}")
