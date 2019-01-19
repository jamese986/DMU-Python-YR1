#Week 7 Task 4
#A program which displays the first 10 terms of the Fibonacci sequence.
#James English - P14138628

#defining variables
num = 1
last_num = 0
before_last = 0


#printing program use
print ("First 10 terms of the Fibonacci sequence")

for i in range(0,10):
    before_last = last_num
    last_num = num
    num = before_last + last_num
    print(num)

