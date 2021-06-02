FirstNumber=int(input("First number"))
SecondNumber=int(input("Second number"))

Key=input("Key")



if (Key=="+"):
    Result=FirstNumber+SecondNumber

elif (Key=="-"):
    Result=FirstNumber-SecondNumber

elif (Key=="*"):
    Result=FirstNumber*SecondNumber

else:
    Result=FirstNumber/SecondNumber

print(Result)
