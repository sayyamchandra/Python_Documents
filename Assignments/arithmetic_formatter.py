#python3 programming of arithmetic_arranger
def main_program(list,start = False):
    list_first_numbers=[]
    list_operators=[]
    list_second_number=[]
    list_ans=[]
    list_questions = []
    if len(list)>5:
        print("Error: Too many problems.")
        quit()

    for s_part in list:
#code for addition
        if len(s_part.split('+')) == 2:
            list_operators.append('+')
            list_numbers = s_part.split('+')
            try:
                first_number = int(list_numbers[0])
                second_number = int(list_numbers[1])
            except:
                print("Error: Numbers must only contain digits.")
                quit()
            if len(list_numbers[0])>4 or len(list_numbers[1])>4:
                print("Error: Numbers cannot be more than four digits.")
                quit()
            ans = str(first_number + second_number)
            list_ans.append(ans)
#code for substraction
        elif len(s_part.split('-')) == 2:
            list_operators.append('-')
            list_numbers = s_part.split('-')
            try:
                first_number = int(list_numbers[0])
                second_number = int(list_numbers[1])
            except:
                print("Error: Numbers must only contain digits.")
                quit()
            if len(list_numbers[0])>4 or len(list_numbers[1])>4:
                print("Error: Numbers cannot be more than four digits.")
                quit()
            ans = str(first_number - second_number)
            list_ans.append(ans)


        else:
            print("Error: Operator must be '+' or '-'.")
            quit()


        list_first_numbers.append(list_numbers[0])
        list_second_number.append(list_numbers[1])





    list_questions = [(list_first_numbers[i], list_second_number[i],list_operators[i],list_ans[i]) for i in range(0, len(list_first_numbers))]


#code for printing first line in output
    for (first_parameter,second_parameter,operator_parameter,ans_parameter) in list_questions:
        spaces = 0
        length_of_first_parameter = len(first_parameter)
        length_of_second_parameter =len(second_parameter)

        if(length_of_first_parameter<length_of_second_parameter):
            spaces = length_of_second_parameter - length_of_first_parameter
        print(" "*(spaces+2),end = "")
        print(first_parameter,end = "    ")
    print("",end="\n")
    #code for printng second line in output
    for (first_parameter,second_parameter,operator_parameter,ans_parameter) in list_questions:
        spaces = 0
        length_of_first_parameter = len(first_parameter)
        length_of_second_parameter =len(second_parameter)

        if(length_of_first_parameter>length_of_second_parameter):
            spaces = length_of_first_parameter - length_of_second_parameter
        print(operator_parameter,end = " ")
        print(" "*spaces,end = "")
        print(second_parameter,end = "    ")
    print("",end = "\n")
    #code for printng third line in output
    for (first_parameter,second_parameter,operator_parameter,ans_parameter) in list_questions:
        if(len(first_parameter)>len(second_parameter)):
            dashes = len(first_parameter)+2
        else:dashes = len(second_parameter)+2
        print("-"*dashes,end="    ")
    print("",end = "\n")
    #code for printing fourth line in output
    if start is True:
        for (first_parameter,second_parameter,operator_parameter,ans_parameter) in list_questions:
            spaces = 0
            length_of_first_parameter = len(first_parameter)
            length_of_second_parameter = len(second_parameter)
            length_of_ans_parameter = len(ans_parameter)
            spaces = spaces + 2
            if length_of_first_parameter>length_of_second_parameter:
                if length_of_ans_parameter>length_of_first_parameter:
                    spaces = spaces - 1
                elif length_of_ans_parameter < length_of_first_parameter:
                    spaces = spaces + 1
            elif length_of_second_parameter>length_of_first_parameter:
                if length_of_ans_parameter>length_of_second_parameter:
                    spaces = spaces -1
                elif length_of_ans_parameter<length_of_second_parameter:
                    spaces = spaces +1
            elif length_of_first_parameter == length_of_second_parameter:
                if length_of_ans_parameter>length_of_first_parameter:
                    spaces = spaces - 1
                elif length_of_ans_parameter < length_of_first_parameter:
                    spaces = spaces + 1
            print(" "*spaces,end = "")
            print(ans_parameter,end ="    ")

#Code for checking the function

#question = input("Enter the question:")
def arithmetic_arranger(question,b = True):
    first_index = int(question.index('['))
    second_index = int(question.index(']'))
    required_string = question[first_index+2:second_index-1]
    list_question = required_string.split('","')

    if question.find("True")  == -1:
        b = False
    main_program(list_question,b)
#print(b)

#print(list_question)
#print(required_string)










a  = input("Enter the question:")
arithmetic_arranger(a)
