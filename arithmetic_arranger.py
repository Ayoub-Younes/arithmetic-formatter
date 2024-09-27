import re

def all_numbers(problems):
    arr_numbers = [re.split(r'\s.\s',prob) for prob in problems]
    numbers = []
    for digits in arr_numbers:
        numbers += digits
    return numbers
# I. Situations that will return an error
#****************************************
def errors_detection(problems):
    #1. Too many problems:
    #---------------------
    if len(problems) > 5: return('Error: Too many problems.')
    #2. Digits:
    #----------
    numbers = all_numbers(problems)
    test_digits = [re.findall(r'^\d+$',d) for d in numbers]
    if not all(test_digits): return 'Error: Numbers must only contain digits.'
    else:
        test_n_digits = [len(d) < 5 for d in numbers]
        if not all(test_n_digits): return 'Error: Numbers cannot be more than four digits.'
    #3. Operators:
    #-------------
    test_ops = [re.findall(r"^\d+\s[+-]\s\d+$", prob) for prob in problems]
    if not all(test_ops): return "Error: Operator must be '+' or '-'."
#*******************************************
# II. Conversion
#****************
def calculation(problems,show_answers=False):

    arr = [re.split(' ', prob) for prob in problems]
    def max_length(list):
        return max([len(el) for el in list])
    length = [max_length(list) for list in arr]
    result = [str(eval(prop)) for prop in problems]
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    for i in range(len(arr)):
        if i == 0:
            first_line += f'{arr[i][0].rjust(length[i]+2)}'
        else:
            first_line += arr[i][0].rjust(length[i]+6)
#/////////////////////////////////////////////////////
    for i in range(len(arr)):
        if i == 0:
            second_line += f'\n{arr[i][1]}{arr[i][2].rjust(length[i]+1)}'
        else:
            second_line += "".rjust(4) + arr[i][1] + arr[i][2].rjust(length[i]+1)
#/////////////////////////////////////////////////////
    for i in range(len(arr)):
        if i == 0:
            third_line += f'\n{"".rjust(length[i]+2,"-")}'
        else:
            third_line += "".rjust(4) + "".rjust(length[i]+2,"-")
    
    for i in range(len(arr)):
        if i == 0:
            fourth_line += f'\n{result[i].rjust(length[i]+2)}'
        else:
            fourth_line += result[i].rjust(length[i]+6)
    if not show_answers: fourth_line = ''
    calc = first_line + second_line + third_line + fourth_line
    
    return calc

def arithmetic_arranger(problems, show_answers=False):
    if errors_detection(problems):
        return errors_detection(problems)
    else:
        return calculation(problems,show_answers)
    
print(f'{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)}')





