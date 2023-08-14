import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def arithmetic_arranger(problems, solver=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    top= ""
    bottom= ""
    lines = ""
    totals = ""
    for n in problems:
        fnum = n.split()[0]
        operator = n.split()[1]
        snum = n.split()[2]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if not fnum.isdigit() or not snum.isdigit():
            return "Error: Numbers must only contain digits."
        if len(fnum) > 4 or len(snum) > 4:
            return "Error: Numbers cannot be more than four digits"

        total = ops[operator](int(fnum), int(snum))
        operatorDistance = max(len(fnum), len(snum)) + 2

        snum = operator + snum.rjust(operatorDistance - 1)
        top = top + fnum.rjust(operatorDistance) + (4 * " ")
        bottom = bottom + snum + (4 * " ")
        lines = lines + len(snum) * "_" + (4 * " ")
        totals = totals + str(total).rjust(operatorDistance) + (4 * " ")
    if solver:
        print(top)
        print(bottom)
        print(lines)
        print(totals)


if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
