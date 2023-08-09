def arithmetic_arranger(problems, val=False):
  first_op, second_op, op = [], [], []
  first , second, dashes= "", "", ""

  # Checking for errors and storing operator and operands to the lists
  if (len(problems)>5): return "Error: Too many problems."
  for problem in problems:
    if ("*" in problem or "/" in problem): return "Error: Operator must be '+' or '-'."
    temp = problem.split(" ")
    if not (temp[0].isdigit() and temp[2].isdigit()):return "Error: Numbers must only contain digits."
    if (len(temp[0])>4 or len(temp[2])>4): return "Error: Numbers cannot be more than four digits."
  
    first_op.append(temp[0]) 
    op.append(temp[1])
    second_op.append(temp[2])

  # Formatting operands and dashes
  for i in range(len(first_op)):
    if(len(first_op[i])>len(second_op[i])): 
      first += " "*2 + first_op[i]
      second += op[i] + " "*(len(first_op[i]) - len(second_op[i]) + 1) + second_op[i] 
    else: 
      first += " "*(len(second_op[i])-len(first_op[i])+2) + first_op[i] 
      second += op[i] + " " + second_op[i] 

    dashes += "-"*(max(len(first_op[i]), len(second_op[i])) + 2) 
    if i!=len(first_op)-1: 
      first += " "*4
      second += " "*4
      dashes += " "*4

  if val == False: return '\n'.join((first, second, dashes))

  # Storing results into list - if val = true
  soln = ""
  for i in range(len(first_op)):
    x = max([len(first_op[i]),len(second_op[i])]) + 2
    result = 0
    if(op[i]=='+'):
      result = str(int(first_op[i])+int(second_op[i]))
    else:
      result = str(int(first_op[i])-int(second_op[i]))
    
    if len(result) > x:
        soln += " " + result
    else:
        soln+=" "*(x- len(result)) + result
    if i != len(op)-1:
      soln += " "* 4
  return '\n'.join((first, second, dashes, soln))