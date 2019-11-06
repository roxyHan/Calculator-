def main():
    correct_input = False
    while not correct_input:
        expr = input("Please enter the expression you wish to compute: ")
        correct_input = is_valid(expr)
        result = evaluate(expr)
        print("**!! Here is the result of your expression!!**\n" + expr + " = " + str(result))
        print("\n\nThank you for using our calculator!\n")


# -----------------------------
#       Helper functions
# -----------------------------

def is_valid(exp):
    open_parentheses = exp.count("(")
    close_parentheses = exp.count(")")
    plus_op = exp.count("+")
    minus_op = exp.count("-")
    times_op = exp.count("*")
    divides_op = exp.count("/")
    total_op = plus_op + minus_op + times_op + divides_op
    for character in exp :
        if (character in ("#$%^&@!<>,.?")):
            return False
    if open_parentheses != close_parentheses:
        return False
    return True


# Helps find the level of priority of the operation
# Addition and Subtraction have lower priority than Multiplication and Division
def priority_order(operator):
    # if the operation is an addition/subtraction than it has low priority
    # in evaluating the expression
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0


# Determine the operation to perform given two operands and a sign/operator
# Computes the given/reduced expression and returns the result
def determine_operation(first, second, sign):
    result = 0
    if sign == '+':
        # addition
        result = first + second
    if sign == '-':
        # subtraction
        result = first - second
    if sign == '*':
        # multiplication
        result = first * second
    if sign == '/':
        # division
        result = first // second
    return result


# Function that returns value of
# expression after evaluation.
def evaluate(tokens):
    # stack to store integer values.
    values = []

    # stack to store operators.
    ops = []
    i = 0

    while i < len(tokens):

        # if current character is bank go to the next
        if tokens[i] == ' ':
            i += 1
            continue

        # Current character is a parenthesis add it to operators stack
        elif tokens[i] == '(':
            ops.append(tokens[i])

        # current is a number,add it to stack for numbers.
        elif tokens[i].isdigit():
            val = 0

            # get the numbers
            while (i < len(tokens) and
                   tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1

            values.append(val)

        # end of calculation
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                a = values.pop()
                b = values.pop()
                operator = ops.pop()

                values.append(determine_operation(a, b, operator))
            # pop opening brace.
            ops.pop()

        else:
            # depending on the operation priority
            # get the values and operator from both stacks
            while (len(ops) != 0 and priority_order(ops[-1]) >= priority_order(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(determine_operation(val1, val2, op))

            # Push current character to 'ops'.
            ops.append(tokens[i])
        i += 1

    # remaining calculation if elements are still present
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(determine_operation(val1, val2, op))

    # return the result
    return values[-1]


# Driver Code
#
# if __name__ == "__main__":
#     print(evaluate("10 + 2 * 6"))
#     print(evaluate("100 * 2 + 12"))
#     print(evaluate("100 * ( 2 + 12 )"))
#     print(evaluate("100 * ( 2 + 12 ) / 14"))
# print(evaluate("100 * ( 2 + 12 ) / 14)"))
#

if __name__ == "__main__":
    main()
