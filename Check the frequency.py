test_dict = {'Codingal':2,'is':2,'best':2,'for': 2,'coding': 1}
print("The orignal dictionary: "+ str(test_dict))
k = 2
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
print("Frequency of k is : "+ str(res))