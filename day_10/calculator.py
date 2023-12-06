from art import logo


#ADD
def add(a,b):
    return a+b

#sub
def sub(a,b):
    return a-b

#multiply
def mult(a,b):
    return a*b
#devide 
def devide(a,b):
    return a/b
operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : devide,

}
def calculator():
    print(logo)
    flag = True


    num1 =  float(input("What`s the first number?: "))
    for symbol in operations : 
        print(symbol)
    operations_symbol = input("Pick an operation from the line above: ")
    num2 =  float(input("What`s the second number?: "))
    answer = operations[operations_symbol]
    answer_f = answer(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {answer_f}")
    while flag == True: 
        keep_calculating = input(f"Type 'y' to continue calcultaing with {answer_f}, or type 'n' to exit and start a new calculation  : ")
        if keep_calculating == 'y':
            operations_symbol = input("Pick an operation : ")
            num_next =  float(input("What`s the next number?: "))
            answer = operations[operations_symbol]
            x = answer_f
            answer_f = answer(answer_f,num_next)
            print(f"{x} {operations_symbol} {num_next} = {answer_f}")
        else:
            flag = False
            calculator()


calculator()