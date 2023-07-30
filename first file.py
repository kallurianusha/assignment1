#checking given number is +ve or -ve:
#num = int(input("enter a number:"))
#if num > 0:
#   print("positive number")
#elif num == 0:
#    print("zero")
#else:
#    print("negative number")

#num =13
#if num > 0:
#    print("positive number")
#elif num < 0:
#    print("negative number")
#else:
#    print("zero")


#num = -16
#if num > 0:
#    print("positive number")
#else:
 #   print("negative number")


#num =25
#if num > 0:
#    print("positive number")
#else:
 #  print("negative number")


#num = -30
#if num > 0:
#   print("positive number")
#else:
#   print("negative number")


#checking 2 numbers which is greater:
#num1=5
#num2=9
#if num1 >= num2:
#    if num1 == num2:
#         print("both num are equal:")
#else:
#    print("second num is greater than first num")


#a = 80
#b = 50
#if a > b:
#    print("greatest number")
#else:
#    print("smaller number")

#a = -20
#b = -40
#if a > b:
#    print("greater number")
#else :
#    print("smaller number")


#a = 50
#b =-20
#if a > b:
#    print("greater number")
#else:
#    print("smaller number")


#num1 =-50
#num2 =20
#if num1 < num2:
#    print("greater number")
#else :
#    print("smaller number")


# repeating strings:
#string = "hello"
#print (string *5)

#string = "hello"
#print("hello\n" *5)


#for i in range(5):
#    print("nice to meet u")



#num = int(input("num of times to repeat a string!"))
#print("python developer\n " * num)


#for i in range (5):
#    print("helloworld",end = " ")
#    print ("helloworld")



#printing half of the string:
#s = "keep smiling"
#n = len(s)//2
#str1 = s[:5]
#str2 = s[-2:]
#print(str1)
#print(str2)



#s = "coding champion"
#str1 = s[8:13:1]
#str2 = s[2:]
#str3 = s[:2:]
#str4 = s[-13:-5]
#str5 = s[2:-10:-2]
#str6 = s[4:-8]
#print(str1)
#print(str2)
#print(str3)
#print(str4)
#print(str5)
#print(str6)



#num = [10,30,60,90]
#new_num1= num[0:3]
#new_num2 = num[2:4]
#new_num3 = num[-4:-1]
#print (new_num1)
#print (new_num2)
#print (new_num3)


 
#checking student pass or fail from input:
#n =int(input("enter any size of class:"))
#intlist =[]
#for i in range(1,n+1):
#    value = int(input("enter marks 0-100:"))
#    intlist.append(value)
#    i = value
#    pass_student= 15
#    invalid = 0
#    fail_student =5
#    if i >= 50:
#        pass_student =pass_student+1
#    elif i >= 100:
#        invalid = invalid+1
#    elif i < 50:
#        fail_student = fail_student+1
#print("the total passed students:",pass_student)
#print("invalid marks!!!")
#print("the total failed students:", fail_student)




#print("enter marks obtained in 5 subjects")
#s1 =int(input())
#s2 =int(input())
#s3 =int(input())
#s4=int(input())
#s5 =int(input())
#avg =(s1+s2+s3+s4+s5)/5

#if s1>30 and s2>30:
#    print("pass")
#elif s2>30 and s3 >30:
#    print("pass")
#elif avg>30:
#    print("pass")
#else:
#    print("fail")



#age eligibility:
#age = int(input("enter age of a use:"))
#if age >= 18:
#    print("he is eligible for voting:", age)
#else:
#    print("he is not eligible for voting:", age)



#age = int(input("enter age of a use:"))
#if age <= 18:
#    print("he is eligible for voting:", age)
#else:
#    print("he is not eligible for voting:", age)



#printing in square :
#length = int(input("enter length:"))
#breadth = int(input("enter breadth:"))
#for i in range(length):
#    for j in range(breadth):
#        print("*",end=" ")
#    print()



#length = int(input("enter the length of square:"))
#breadth = int(input("enter the breadth of a square:"))
#for i in range(breadth):
#    for j in range(length):
#        print("#",end =" ")
#    print()



#printing all even and odd numbers:
#even_numbers = []
#odd_numbers = []
#for number in range(1,100):
#    if number % 2 == 0:
#        even_numbers.append(number)
#    else:
#        odd_numbers.append(number)
#print("even_numbers:",even_numbers)
#print("odd_numbers:",odd_numbers)


#for x in range(1,100):
#    if x%2==0:
#        print(x)

#for x in range(1,100):
#    if x%2!=0:
 #       print(x)