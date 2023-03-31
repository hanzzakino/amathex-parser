'''
AmthexParser
@author: Hanz Aquino
'''
__author__ = 'Hanz Aquino'
__version__ = '$Revision: 2.0.1 $'
__date__ = '$Date: 2023-4-1 $'

###
# New Algorithm Steps (Updated from AmthexParser):
# solveExpression() will convert variables into real numbers ex. 'x','-','3' -> (x=1)  -> '1','-','3'
# after all the variables are replaced with real numbers solveExpression() will call solve() and return the output
# solve() function will handle the brackets by solving inner brackets ex. 5*(5-(6*2)/7) -> 5*(5-12/7) -> 5*3.285714285714286 -> 16.42857142857143
# solve() will call self.solveSums(self.solveQuotients(self.solveProducts(self.solveExponents((self.combineNegatives(inner))))))
# the 'inner' above contains all the numeric expression inside the innermost bracket
# each arithmetic operator function is a recursive function thats solve the arithmetic by
# finding the index i of the operator and solving if using the value in i-1 and i+1, the function will continue to call itself until all
# the operator have been solve
# solveFunctions() solve any math function present in the expression ex. sin,cos, etc.
# i.e. for solveProducts(), 5*5-45/89-67+1*2*3 will return 25-45/89-67+6 (as a string array)
# i.e. for solveQuotients(), 25-45/89-67+6 will return 25-0.5056179775280899-67+6 (as a string array)
###


import re
import math


class AmthexParser():

    ### PRIVATE METHODS ###

    # This will solved the arr_expression error where 5*-6 will be ['5','*','-','6']
    # The item '*','-' will produce an error thus it needs to be converted from  ['5','*','-','6'] to ['5','*','-6']
    def __combineNegatives(self, arr_expression):
        output_expression = []
        skip = 0
        # Iterate on all the characters in the arr_expression
        for i in range(len(arr_expression)):
            # Continue if the skip variable has value
            if (skip > 0):
                # Decrement the skip value
                skip -= 1
                continue
            # If current character is an operator
            if (arr_expression[i] == "*" or arr_expression[i] == "/" or arr_expression[i] == "+" or arr_expression[i] == "-" or arr_expression[i] == "^"):
                # if the next character is '-' ex, '*','-','6'
                if (arr_expression[i+1] == '-' and arr_expression[i+2] != '('):
                    # Append the arr_expression[i] (the operator) to the output
                    output_expression.append(arr_expression[i])
                    # Append the next 2 items as one string, '*','-','6' -> '*','-6'
                    output_expression.append(
                        arr_expression[i+1] + arr_expression[i+2])
                    # Skip the appended values
                    skip = 2
                elif (i == 0 and arr_expression[i] == '-' and arr_expression[i+1] != '('):
                    output_expression.append(
                        arr_expression[i] + arr_expression[i+1])
                    skip = 1
                else:
                    output_expression.append(arr_expression[i])
                    output_expression.append(arr_expression[i+1])
                    skip = 1
            else:
                output_expression.append(arr_expression[i])
                skip = 0
        return output_expression

    ## The function is the same on every operations ####
    # These are recursive functions that solve all the arithmetic operation
    # in an expression
    def __solveProducts(self, arr_expression):
        # Treat --6 as 6 in first index which cant be +
        arr_expression[0] = arr_expression[0].replace('--', '')
        try:
            # Find the index of the first multiplication operator
            i = arr_expression.index('*')
            # will solve the 'N','*','N'
            temp = float(arr_expression[i-1])*float(arr_expression[i+1])
            # This will output 6-8/5 from 6-4*2/5
            arr_expression[i-1] = str(temp)
            arr_expression.pop(i)
            arr_expression.pop(i)
            # Continue the iteration until arr_expression has no remaining multiplication operation
            self.__solveProducts(arr_expression)
        except ValueError:
            pass
        return arr_expression

    def __solveQuotients(self, arr_expression):
        arr_expression[0] = arr_expression[0].replace('--', '')
        try:
            i = arr_expression.index('/')
            temp = float(arr_expression[i-1])/float(arr_expression[i+1])
            arr_expression[i-1] = str(temp)
            arr_expression.pop(i)
            arr_expression.pop(i)
            self.__solveQuotients(arr_expression)
        except ValueError:
            pass
        return arr_expression

    def __solveSums(self, arr_expression):
        arr_expression[0] = arr_expression[0].replace('--', '')
        if (len(arr_expression) == 2):
            return str(-1*float(arr_expression[1]))
        summ = 0
        for i in range(len(arr_expression)):
            if (i == 0):
                summ += float(arr_expression[i])
                continue
            if (arr_expression[i] == '+'):
                summ += float(arr_expression[i+1])
                continue
            if (arr_expression[i] == '-'):
                summ -= float(arr_expression[i+1])
                continue
        return str(summ)

    def __solveExponents(self, arr_expression):
        arr_expression[0] = arr_expression[0].replace('--', '')
        try:
            i = arr_expression.index('^')
            temp = pow(float(arr_expression[i-1]), float(arr_expression[i+1]))
            arr_expression[i-1] = str(temp)
            arr_expression.pop(i)
            arr_expression.pop(i)
            self.__solveExponents(arr_expression)
        except ValueError:
            pass
        return arr_expression

    # This will solve some math functions in the expression i.e. sin,cos,tan,log
    def __solveFunctions(self, str_expression):
        # Convert the string expression to list
        arr_expression = list(str_expression)
        # List all the functions
        math_func_keys = ['asin', 'acos', 'atan', 'sin', 'cos', 'tan', 'log']
        # Dictionary of Functions with function operartor as key and function method as value
        math_functions = {
            'sin': lambda x:  math.sin(x),
            'cos': lambda x:  math.cos(x),
            'tan': lambda x:  math.tan(x),
            'asin': lambda x:  math.asin(x),
            'acos': lambda x:  math.acos(x),
            'atan': lambda x:  math.atan(x),
            'log': lambda x:  math.log(x),
        }
        # Check if brackets are matched in count
        if not arr_expression.count('(') == arr_expression.count(')'):
            print("Brackets are not balanced")
            raise ArithmeticError
        # Check if the input still contains a math function (To stop recursion)
        hasMathFunction = False
        for f in math_func_keys:
            if f in str_expression:
                hasMathFunction = True
        # Main Algorithm
        if (hasMathFunction):
            # Similar to __solve this starts by finding the
            # innermost bracket and check if it has a math function operator preceding it
            # Find the index of the innermost opening bracket and its matching closing bracket
            first_bracket_index = -9
            last_bracket_index = -9
            inner = []
            for i in range(len(arr_expression)):
                if (arr_expression[i] == ')'):
                    last_bracket_index = i
                    break
            for i in range(last_bracket_index, -1, -1):
                if (arr_expression[i] == '('):
                    first_bracket_index = i
                    break
            for i in range(first_bracket_index+1, last_bracket_index, 1):
                inner.append(arr_expression[i])
            # Check if there is a math function beside it
            # i.e. sin(
            function_index = -1
            for idx, func in enumerate(math_func_keys):
                if (func[len(func)-1] == arr_expression[first_bracket_index-1]):
                    isFunction = True
                    for i in range(len(func)-1, -1, -1):
                        if not (func[i] == arr_expression[first_bracket_index-(len(func)-i)]):
                            isFunction = False
                    if (isFunction):
                        function_index = idx
                        break
            # If a function is found, it will solve all the contained expression in it first
            # and it will Solve the function
            if (function_index > -1):
                # Function string for key
                function_str = math_func_keys[function_index]
                # Store the solve function in temp
                temp = math_functions[function_str](
                    float(self.solveExpression(''.join(inner))))
                # Modify the array to replace the function expression with its
                # value
                included_function = first_bracket_index - len(function_str)
                arr_expression[included_function] = str(temp)
                for i in range(last_bracket_index-included_function):
                    arr_expression.pop(included_function+1)
            else:
                # Solution: This function also detects other innermost brackets and result in infinite recursion
                temp = float(self.solveExpression(''.join(inner)))
                arr_expression[first_bracket_index] = str(temp)
                for i in range(last_bracket_index-first_bracket_index):
                    arr_expression.pop(first_bracket_index+1)
            # Save the value in the str_expression parameter
            str_expression = ''.join(arr_expression)
            # Call itself again to see if other math functions exist
            return self.__solveFunctions(str_expression)
        # If there are no more math functions, the recusion will stop
        return str_expression

    # Handling brackets and Solving algorithm for arithmetics
    # Solving patern using PEMDAS self.solveSums(self.solveQuotients(self.solveProducts(self.solveExponents((self.combineNegatives(inner))))))
    def __solve(self, arr_expression):
        # The process below will output (5*(67+1)*8) into (5*68*8)
        # Check if brackets are balanced
        if not arr_expression.count('(') == arr_expression.count(')'):
            print("Brackets are not balanced")
            raise ArithmeticError
        # Solve expression in every innermost bracket
        # Check in there are sstill brackets (For recursion)
        if (arr_expression.count('(') > 0):
            first_bracket_index = -9
            last_bracket_index = -9
            # The expressioncharacter array will be inside the inner variable
            inner = []
            # Find the index of innermost closing bracket
            for i in range(len(arr_expression)):
                if (arr_expression[i] == ')'):
                    last_bracket_index = i
                    break
            # Find the index of innermost opening bracket
            for i in range(last_bracket_index, -1, -1):
                if (arr_expression[i] == '('):
                    first_bracket_index = i
                    break
            # append all the values inside the first_bracket_index and last_bracket_index
            for i in range(first_bracket_index+1, last_bracket_index, 1):
                inner.append(arr_expression[i])
            # solve the expression in inner variable
            temp = self.__solveSums(self.__solveQuotients(self.__solveProducts(
                self.__solveExponents((self.__combineNegatives(inner))))))
            # replace the first bracket index with the variable temp
            # Since all the charcters inside the first_bracket_index and last_bracket_index will be
            # deleted and replaced with the solved value stored in temp
            arr_expression[first_bracket_index] = str(temp)
            # This deletes all the characters inside the first_bracket_index and last_bracket_index will be
            # (excluding first_bracket_index item since it is the solved value)
            # Since its already been solved
            for i in range(last_bracket_index-first_bracket_index):
                arr_expression.pop(first_bracket_index+1)
            # Recursion continue until there are no remaining brackets ()
            return self.__solve(arr_expression)
        # If there are no brackets, the program will output the value
        return self.__solveSums(self.__solveQuotients(self.__solveProducts(self.__solveExponents((self.__combineNegatives(arr_expression))))))

    ### PUBLIC METHODS ###
    # Main solving function
    # also included solving expressions with undefined variable  ex. 3*x+4

    def solveExpression(self, str_expression, v='', val=0):
        try:
            # Remove all spaces
            str_expression = str_expression.replace(" ", "")
            # Replace euler's number (e) with its value
            str_expression = str_expression.replace("e", str(math.exp(1)))
            # Replace the variable specified with its value
            if not v == '':
                str_expression = str_expression.replace(v, str(val))
            # Solve math functions i.e. sin,cos,tan,log
            str_expression = self.__solveFunctions(str_expression)
            # Regex converts '['5','.','0'+'4','0','0'] to ['5.0','+','400']
            expression_arr = re.findall(
                "[)]|[(]|[\^]|[*/+-]|[0123456789.]+", str_expression)
            # Return 0 if the input is null
            if expression_arr == "":
                return 0
            # Return the final solution as float
            return (float(self.__solve(expression_arr)))
        except:
            return 'Input Error'


# ################### TESTING ###################

# parser = mathexparser()

# expr1 = '((tan(5*sin(cos(5+sin(4.78))+0.2))+(sin(0.34)^4))/(sin(0.3)*cos(5)))*e^0.44'
# # = 26.58242078009371
# expr2 = '(0.3*sin(x))+(0.7*sin(4*x))+(0.2*sin(20*x))+(0.1*sin(40*x))+(0.7*sin(3*x))'
# print(parser.solveExpression(expr1))
# print(parser.solveExpression(expr2, v='x', val=5))

# # Test: ((5-(-3* 4  *5 ) )/(67-9))^3 will output 1.407524908770347
# while(True):
#     print("Input Expression:")
#     expression = input()
#     print("= "+str(parser.solveExpression(expression)))


# ################### TESTING ###################
