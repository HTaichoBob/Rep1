# while loop
total = 0
index = 0

my_list = list(range(1,51))

while index<len(my_list):
    if my_list[index] % 2 == 0:
        total += my_list[index]
    index += 1




# for loop
#my_list = list(range(1, 51))
#for number in my_list:
 #   if number % 2 == 0:
  #      total += number
        
print(f"The sum of even numbers 1 to 50 is {total}")







