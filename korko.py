# Input, assignment
name = input('What is your name?\n')
print('Hello! Use a period as a decimal, %s.' % name)


import decimal
def calculation():
    resetcalc = False
    try:
        choicemath=int(input(" 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n"))
    except ValueError:
        print("not an integer!")
        calculation()
    choicenumber1=decimal.Decimal(input(" Please select your first number: "))
    choicenumber2=decimal.Decimal(input(" Please select your second number: "))
    if choicemath is (1):
        result = choicenumber1 + choicenumber2
    elif choicemath is (2):
        result = choicenumber1 - choicenumber2
    elif choicemath is (3):
        result = choicenumber1 * choicenumber2
    elif choicemath is (4):
        result = choicenumber1 / choicenumber2
    else:
        print ("Not one of the choices! Try again!")
        calculation()
    print ("Result:", result)
    resetcalculation()
def resetcalculation():
    user_answer = input("Do another calculation? \n").lower().strip()
    if user_answer == "yes":
        calculation()
    elif user_answer == "no":
          quit
    else:
         print("Error: Answer must be yes or no")
calculation()
resetcalculation()


