'''
@author: Hanz Aquino
'''
__author__ = 'Hanz Aquino'
__version__ = '$Revision: 1.0 $'
__datecreated__ = '$Date: 2021-02-23 $'

###
# Algorithm Steps:
# solveExpression() will convert variables into real numbers ex. 'x','-','3' -> (x=1)  -> '1','-','3'
# after all the variables are replaced with real numbers solveExpression() will call solve() and return the output
# solve() function will handle the brackets by solving inner brackets ex. 5*(5-(6*2)/7) -> 5*(5-12/7) -> 5*3.285714285714286 -> 16.42857142857143
# solve() will call self.solveSums(self.solveQuotients(self.solveProducts(self.solveExponents((self.combineNegatives(inner))))))
# the 'inner' above contains all the numeric expression inside the innermost bracket
# each arithmetic operator function is a recursive function thats solve the arithmetic by
# finding the index i of the operator and solving if using the value in i-1 and i+1, the function will continue to call itself until all
# the operator have been solve
# i.e. for solveProducts(), 5*5-45/89-67+1*2*3 will return 25-45/89-67+6 (as a string array)
# i.e. for solveQuotients(), 25-45/89-67+6 will return 25-0.5056179775280899-67+6 (as a string array)
###
# arr_expression is an array of the expression characters
# ex. (5^3)-78 to ['(','5','^','3',')','-','78']

# Test: ((5-(-3*4*5))/(67-9))^3 will output 1.407524908770347

import re
import math


class AmthexParser():

    # This will solved the arr_expression error where 5*-6 will be ['5','*','-','6']
    # The item '*','-' will produce an error thus it needs to be converted from  ['5','*','-','6'] to ['5','*','-6']
    def combineNegatives(self, arr_expression):
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
            if (arr_expression[i] == '*' or arr_expression[i] == '/' or arr_expression[i] == '+' or arr_expression[i] == '-' or arr_expression[i] == '^'):
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

    #### The function is the same on every operations ####
    # This is a recursive function that solves all the multiplication operation
    # in an expression
    def solveProducts(self, arr_expression):
        # Treat --6 as 6
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
            self.solveProducts(arr_expression)
        except ValueError:
            pass
        return arr_expression

    def solveQuotients(self, arr_expression):
        arr_expression[0] = arr_expression[0].replace('--', '')
        try:
            i = arr_expression.index('/')
            temp = float(arr_expression[i-1])/float(arr_expression[i+1])
            arr_expression[i-1] = str(temp)
            arr_expression.pop(i)
            arr_expression.pop(i)
            self.solveQuotients(arr_expression)
        except ValueError:
            pass
        return arr_expression

    def solveSums(self, arr_expression):
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

    def solveExponents(self, arr_expression):
        arr_expression[0] = arr_expression[0].replace('--', '')
        try:
            i = arr_expression.index('^')

            # i = -1
            # for n in range(len(arr_expression)-1,-1,-1):
            #     if arr_expression[n] == '^':
            #         i = n
            #         break

            temp = pow(float(arr_expression[i-1]), float(arr_expression[i+1]))
            arr_expression[i-1] = str(temp)
            arr_expression.pop(i)
            arr_expression.pop(i)
            self.solveExponents(arr_expression)
        except ValueError:
            pass
        return arr_expression

    #### The function is the same on every operations ####
    # Handling brackets and Solving algorithm for arithmetics
    # Solving patern using PEMDAS self.solveSums(self.solveQuotients(self.solveProducts(self.solveExponents((self.combineNegatives(inner))))))
    def solve(self, arr_expression):
        # Check if brackets still exist
        if not arr_expression.count('(') == arr_expression.count(')'):
            raise ArithmeticError
        if (arr_expression.count('(') > 0):

            # The process below will output (5*(67+1)*8) into (5*68*8)

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
            temp = self.solveSums(self.solveQuotients(self.solveProducts(
                self.solveExponents((self.combineNegatives(inner))))))
            # replace the first bracket index with the variable temp
            # Since all the charcters inside the first_bracket_index and last_bracket_index will be
            # deleted and replaced with the solved value stored in temp
            arr_expression[first_bracket_index] = str(temp)
            # This deletes all the characters inside the first_bracket_index and last_bracket_index will be
            # (excluding first_bracket_index item since it is the solved value)
            # Since its already been solved
            for i in range(last_bracket_index-first_bracket_index):
                arr_expression.pop(first_bracket_index+1)
            ###

            # Recursion continue until there are no remaining brackets ()
            self.solve(arr_expression)
        # If there are no brackets, the program will out put the value
        return self.solveSums(self.solveQuotients(self.solveProducts(self.solveExponents((self.combineNegatives(arr_expression))))))

    # ###! Experimental Todo !###
    # def solveTrig(self, arr_expression):
    #     return arr_expression
    # ###! Experimental !###

    ################ Exported functions ################

    def solveExpression(self, str_expression):
        # This removes the whitespaces and change constants
        # step:: '((5*e-3)*3)' -> '((5*2.71828-3)*3)'
        str_expression = str_expression.replace(' ', '')
        str_expression = str_expression.replace('e', str(math.exp(1)))

        # this regex converts the expression string into array:
        # '(5^3)-78' to ['(','5','^','3',')','-','78']
        expression_arr = re.findall(
            '[)]|[(]|[\^]|[*/+-]|[0123456789.]+', str_expression)

        if expression_arr == '':
            return 0
        # after all the variables are replaced with real numbers
        # continue solving it
        # Returns string value
        try:
            return self.solve(expression_arr)
        except Exception as e:
            return 'Input Error'

    # For single variable expression
    def solveExpressionVar(self, str_expression, v, var_input):
        str_expression = str_expression.replace(' ', '')
        str_expression = str_expression.replace('e', str(math.exp(1)))

        str_expression = str_expression.replace(v, var_input)

        expression_arr = re.findall(
            '[)]|[(]|[\^]|[*/+-]|[0123456789.]+', str_expression)

        if expression_arr == '':
            return 0
        return (float(self.solve(expression_arr)))

    # Summations and Functions
    def x_sum(self, str_expression, start, end):
        return sum(float(self.solveExpression(str_expression.replace('x', str(i)))) for i in range(start, end+1))

    def function_table(self, variable, expression, start, end, step=1):
        output = [self.solveExpressionVar(
            expression, variable, str(i)) for i in range(start, end+1, step)]
        return output

    # The program will ask for the value of all the unknown variable before continuing
    def solveExpression_cmdvar(self, str_expression):
        # This removes the whitespaces and change constants
        # step:: '((5*e-3)*3)' -> '((5*2.71828-3)*3)'
        str_expression = str_expression.replace(' ', '')
        str_expression = str_expression.replace('e', str(math.exp(1)))

        # list of variables
        variable_arr = re.findall('[a-zA-Z]', str_expression)
        variable_arr = list(dict.fromkeys(variable_arr))

        # Replace variables to numbers
        for v in variable_arr:
            print(v+' = ')
            # variables will also accept arithmetic only expressions
            var_input = self.solve(input())
            # Replace all the varibles with the input
            str_expression = str_expression.replace(v, var_input)

        # this regex converts the expression string into array:
        # '(5^3)-78' to ['(','5','^','3',')','-','78']
        expression_arr = re.findall(
            '[)]|[(]|[\^]|[*/+-]|[0123456789.]+', str_expression)

        if expression_arr == '':
            return 0
        # after all the variables are replaced with real numbers
        # continue solving it
        # Returns string value
        return self.solve(expression_arr)
