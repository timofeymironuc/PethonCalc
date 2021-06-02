print("This is calculator program")

MathProblem =  (input("Please enter any math problem"))
Numbers = []
Operators = []

PieseNumber=None

for i in MathProblem:
    if (i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0'):
        if (PieseNumber == None):
            PieseNumber = i
        else:
            PieseNumber = PieseNumber + i
            
    else:
        Operators.append(i)
        Numbers.append(int(PieseNumber))     
        PieseNumber = None

Numbers.append(int(PieseNumber))

a = 1

Result = Numbers[0]


while(a <= len(Operators)):   
    
    if (Operators[a-1] == "+"):
        Result = Result + Numbers[a]


    elif (Operators[a-1] == "-"):
        Result = Result - Numbers[a]

    elif (Operators[a-1] == "*"):
        Result = Result * Numbers[a]

    elif(Operators[a-1] == "/"):
        Result = Result / Numbers[a]
        
    a = a + 1


print('Result is ' + str( Result))
