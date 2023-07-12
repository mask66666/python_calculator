print("insert what you want to do (+-*/)\n")
do = input()
if do == "+":
 plus = 1
 minus = 0
 multiply = 0
 devide = 0
elif do == "-":
 plus = 0
 minus = 1
 multiply = 0
elif do == "*":
 plus = 0
 minus = 0
 multiply = 1
 devide = 0
elif do == "/":
 plus = 0
 minus = 0
 multiply = 0
 devide = 1
else:
 print("please next time insert what you want to do")
 exit()


print("insert first number\n")
number_1 = int(input())
print("insert second number\n")
number_2 = int(input())


if plus == 1:
 answer = int(number_1) + int(number_2)
elif minus == 1:
 answer = int(number_1) - int(number_2)
elif multiply == 1:
 answer = int(number_1) * int(number_2)
elif devide == 1:
 answer = int(number_1) / int(number_2)
else:
 print("somethink wrong happened")
 exit()

print("answer is:\n" + str(answer))

exit()
