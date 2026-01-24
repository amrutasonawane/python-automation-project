 #List  - Duplicate allowed
Value1 = [10,20,30,40,10]
print(Value1[0]) #10
Value1[2] = 35 # mutable
print(Value1)

 #Tuple - Duplicate
Value2 = (10,20,30,40,10)
print(Value2[0]) #10
#Value2[1] = 35
print(Value2)

# File "/Users/amgarud/Documents/Python/SequenceX.py", line 10, in <module>
#    Value2[1] = 35
#    ~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment

 #Set - Not Duplicate
Value3 = {10,20,30,40,10}
#print(Value3[0]) #Error 


