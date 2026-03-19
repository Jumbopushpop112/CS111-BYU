#print all values up to 5 from 0
x = 0
while x < 5:
    print(x)
    x += 1

#find multiples of 7 between 100 and 200
counter = 100
while counter < 200:
    if counter % 7 == 0:
        print(counter)
    counter += 1

#find multiple with continue statement
counter = 100
while counter < 200:
    counter += 1
    if counter % 7 != 0:
        continue
    print(counter)

nums = [1,2,3,4]
nums2 = nums
print(nums is nums2)

