print("This is calculator program")

MathProblem =  (input("Please enter any math problem"))
Numbers = []
Operators = []


for i in MathProblem:
    if (i == '-' or '+' or '*' or '/'):
        Operators.add(i)
        Numbers.add(Number)
        Number=None
        
    else:
        Number= int(str(Number)+i)

a=1
Result=Numbers[0]
while(a!=Operators.len):   
    
    if (Operators[a-1] == "+"):
        Result = Result+Numbers[a]

    elif (Operators[a-1] == "-"):
        Result = Result-Numbers[a]

    elif (Operators[a-1] == "*"):
        Result = Result*Numbers[a]

    elif(Operators[a-1] == "/"):
        Result = Result/Numbers[a]
        
    a=a+1


print('Result is ' + str( Result)  )
