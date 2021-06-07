import operator

print("This is calculator program")

MathProblem =  (input("Please enter any math problem"))

Operatorsset=set(('-', '+', '=', '*', '/'))

Operatorsdict={'-' : operator.sub, '+' : operator.add, '/' : operator.truediv, '*' : operator.mul}

Numbers = []
OperatorsList = []

Start=0

for i, nomer in zip (MathProblem, range(len(MathProblem))):

    if(Operatorsset >= set(i)):
        OperatorsList.append(i)
        Numbers.append(int(MathProblem[Start:nomer]))
        Start=nomer+1
        
    


Result = Numbers[0]

for i, nomer in zip(OperatorsList, range(len(OperatorsList))):   
    
    try:
        Result=Operatorsdict[i](Result, Numbers[nomer+1])

    except KeyError:
        print(Result)
