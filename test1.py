# SUM
def calculatesum(data_list):
    if data_list.__len__()==0:
        return 0
    else:
        total = 0
        for i in data_list:
            total = total + i
        return total

assert calculatesum([])==0
assert calculatesum([2,4,6,8,10])==30
assert calculatesum([1,3,5,7,9])==25

print(calculatesum([]))
print(calculatesum([2,4,6,8,10]))
print(calculatesum([1,3,5,7,9]))

#%%

#Product
def calculateproduct(data_list):
    if data_list.__len__()==0:
        return 0
    else:
        total = 1
        for i in data_list:
            total = total * i
        return total

assert calculateproduct([])==0
assert calculateproduct([2,4])==8
assert calculateproduct([1,3])==3

print(calculateproduct([]))
print(calculateproduct([2,4]))
print(calculateproduct([1,3]))


#%%
# Average
def average(data_list):
    if data_list.__len__()==0:
        return 0
    else :
        avg = sum(data_list)/len(data_list)
        return avg


assert average([])==0
assert average([12,20,37])==23
assert average([0,0,0,0,0])==0

print(average([]))
print(average([12,20,37]))
print(average([0,0,0,0,0]))


#%%
def median(numbers):
    if len(numbers) == 0:
        return 0
    numbers.sort()
    middleIndex=len(numbers) // 2

    if len(numbers) % 2 == 0:
        return (numbers[middleIndex]+numbers[middleIndex-1])/2
    else :
        return numbers[middleIndex]

#assert median([])==0
#assert median([1,2,3,1,2,3,1,2,3])==2
#assert median([12,20,37])==20
#assert median([0,0,0,0,0])==0

print(median([]))
print(median([1,2,3,1,2,3,1,2,3]))
print(median([12,20,37]))
print(median([0,0,0,0,0]))