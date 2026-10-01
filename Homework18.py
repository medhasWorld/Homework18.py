Test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
print("The original Dictionary : " + str(Test_dict))
k = int(input("Enter the value of which u want to find how many times it shows up: "))
res = 0
for key in Test_dict:
    if Test_dict[key] == k:
        res = res + 1
print("Frequncy of k is : " + str(res))