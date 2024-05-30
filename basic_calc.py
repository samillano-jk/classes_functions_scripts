def basic_calc(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    
    
def math_equation_converter(equation):
    try:
         list1 = equation.split()
         n1 = int(list1[0])
         op = str(list1[1])
         n2 = int(list1[2])
         return [n1, op, n2]
    except IndexError:
         print("There's no spaces")
    
    
def intermediate_calc(n1, op, n2):
     if op == "^" or op == "**":
          return n1 ** n2
     elif op == "//":
          return n1 // n2
     elif op == "%":
          return n1 % n2


def calc(n1, op, n2):
    basic_operands = ["+", "-", "*", "/"]
    inter_operands = ["**", "^", "//", "%"]
    
    
    if op in basic_operands:
          return basic_calc(n1=n1, op=op, n2=n2)
    elif op in inter_operands:
          return intermediate_calc(n1=n1, op=op, n2=n2)
    
   
         


while True: 
     if __name__ == "__main__":
          equation = input(" Write the equation: ")
          n1, op, n2 = math_equation_converter(equation=equation)
          result = calc(n1=n1, op=op, n2=n2)
          print(result)
          
     
