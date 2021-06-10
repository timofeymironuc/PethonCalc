import operator #библеотека для замены операторов командами

a=True

while(a==True){
    
    print("This is calculator program")

    print("Please enter any math problem")
    MathProblem =  (input()) #перменная в которой храниться пример

    Operatorsset=set(('-', '+', '=', '*', '/'))#множество для праверки евляетьсяли символ оперетором

    Operatorsdict={'-' : operator.sub, '+' : operator.add, '/' : operator.truediv, '*' : operator.mul}#словарь нужен для сопоствления строковых символов с командами

    Numbers = [] #лист для чисел
    OperatorsList = []#лист для операторов

    Start=0#переменная для указания начала среза который превратится в число 

    for i, nomer in zip (MathProblem, range(len(MathProblem))):#перебор примера для разложения его на операторы и числ

        if(Operatorsset >= set(i)):#проверка евляется ли символ оператором
            OperatorsList.append(i)#добавление оператора
            try:
                Numbers.append(float(MathProblem[Start:nomer]))#добавление числа в Numbers
            except ValueError:
                print('You print unacceptable char')
                exit()
            #проверка на недопустимые символы
            Start=nomer+1
            
        

    try:
        Result = Numbers[0]

    except IndexError:
        print("You don't write operators")
        exit(0)
        #проверка на не написанные операторы
        
    for i, nomer in zip(OperatorsList, range(len(OperatorsList))):#перебор операторов   
        
        try:
            Result=Operatorsdict[i](Result, Numbers[nomer+1])#вычисление

        except IndexError:
            print("You don't write =" )
        #проверка на ненаписание ровно
        except KeyError:
            print(Result)#вывод результата
        #проверка на ошибку которая происходит если написать ровно она должна произойти для вывода результата
    print('Countinue? y, n')
    if (input()=='n'):
        a=False

}
