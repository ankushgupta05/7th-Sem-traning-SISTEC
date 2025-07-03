arr = [int(i) for i in input("Enter Array Element :").split()]
num = len(arr)
for i in range(num):
    swape = False
    for i in range(0,num-i-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
            swape=True
    if  not swape:
        break

print('The Sorted Array : ',arr) 

