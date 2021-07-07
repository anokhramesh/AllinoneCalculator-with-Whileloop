# This is a simple Python Program to Do all mathematical calculation .
print('All in one Calculator with While loop')
print('**************************************')
while True:
    op = input("Choose an operator(+,-,*,/,%)or press q for Quit\n")#op is a string type variable name to store the user input operator.
     
    if op.lower() == 'q':#if user entry is lower case letter 'q' then break the loop and quit the program.
        break
 
    if op not in '+-*/%q':#if user entry is not any of these(+,-,*,/,%,q)charactor,print-Invalid entry and continue the loop. 
        print('Invalid entry')        
        continue
 
    a = float(input("Enter the Value of 'a'\n")) # prompting  user to enter the value of 'a'
    b = float(input("Enter the Value of 'b'\n")) # prompting user to enter the value of 'b'
  
    if op == '+': # if user entry is '+'
        sum = a + b # add the value of 'a'and 'b' then store to the variable-'sum'. 
        print('The sum of ',a, ' and ', b,' is = ', sum , sep = '')#display the values of 'a' and 'b' and 'sum'. 
  
    elif op == '-': # if user entry is '-'
        difference = a-b # subtract the value of'b' from 'a' and store to the variable-'difference'.
        print(a,' minus ',b,' equals ',difference, '.', sep = '')#display the values of 'a' and 'b' and 'difference'
  
    elif op == '*':  # if user entry is'*'
        product = a*b # multiply the value of 'a' and 'b' then store to the variable-'product' 
        print(a, ' times ', b, ' equals ', product, '.', sep='')#display the values of 'a' and 'b' and 'product'
  
    elif op == '/': # if user entry is'/'
  
        if b == 0:# if user entry is 0 
            print('You can not divide a number by zero.')#display -You can not divide a number by zero.
  
  
        else: 
            quotient = a/b # divide the value of 'a' by 'b' then store to the variable-'quotient' 
            rounded = format(quotient, '.2f')#formating the quotient variable,then store to rounded variable,display only 2 decimal values after the point.
            print(a,' divided by ',b,' equals ', rounded,'.', sep = '')#display the value of 'a','b' and  variable'rounded'
  
    elif op == '%': # if user entry is %
        remainder = a%b # devide the value of 'a' by 'b' store the remainder value to variable'remainder'
        print('The remainder of ',a, ' and ', b, ' is ', a%b, '.', sep ='') #display the value of 'a','b' and remainder.
  
  
    else:
        print('That is not a valid maths operator.')#if user entry is not matching the above operator,display-That is not a valid maths operator.
 
