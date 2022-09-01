# Function that finds the max num of 3 numbers

def max_num(a,b,c):
  return max(a,b,c)

print(max_num(1,2,3))
print(max_num(45,34,12))
print(max_num(436,217,217))


#Function that multiplies all numbers in a list

def mult_list(lst):
  val = lst[0]
  if len(lst) > 1:
    for i in lst[1:]:
      val = val * i
  return val
    
print(mult_list([2,2,3]))
print(mult_list([3,5,3]))
print(mult_list([15,7,9]))

# Reverse a string

def rev_string(my_str):
  return my_str[::-1]

print(rev_string("Hans loves to code"))
print(rev_string("Test String"))
print(rev_string("Supercalifragilisticexpiolidocious"))

# Function that checks if a num is within a range of one

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))