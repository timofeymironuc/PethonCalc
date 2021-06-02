print("This is calculator program")

FirstNumber = float (input("Please enter first number"))
SecondNumber = float (input("Please enter second number"))

Key = input ("Please enter operator")



if (Key == "+"):
    Result = FirstNumber + SecondNumber

elif (Key == "-"):
    Result = FirstNumber - SecondNumber

elif (Key == "*"):
    Result = FirstNumber * SecondNumber

elif(Key == "/"):
    Result = FirstNumber/SecondNumber

else:
    print('You entered an incorrect symbol.')

print('Result is ' + str( Result)  )
