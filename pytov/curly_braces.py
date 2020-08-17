def hide_curlys(text):
    text = [c for c in text]
    balance = 0
    balancePerns = 0
    hide_curly = False
    in_perns = False
    lambd = "lambda"
    lambdIter = 0
    isLambd = False
    lambdBalance = 0
    lambdFirst = False
    indentation = 0
    indentations = []
    last_was_indentation = True
    colon_balance = 0


    for index, item  in enumerate(text):

        if last_was_indentation and (item == " " or item == "\t"):
            indentation += 1
        elif last_was_indentation and (item != " " and item != "\t"):
            last_was_indentation = False
        elif item == "\n":
            indentation = 0
            last_was_indentation = True

        if item == "=":
            hide_curly = True
        elif item == "{" and hide_curly and not isLambd:
            text[index] = "~^$curly$-$braces$-$start$-$flag$^~"
            balance += 1
        elif item == "}" and hide_curly and not isLambd:
            text[index] = "~^$curly$-$braces$-$end$-$flag$^~"
            balance -= 1
            if balance == 0 and not in_perns:
                hide_curly = False

        elif item == ":" and ((not hide_curly) or isLambd):
            text[index] = "{"
            colon_balance += 1
            indentations.append(indentation)

        if colon_balance > 0 and len(indentations) > 0 and indentations[-1] >= indentation and ((index < len(text) - 1 and text[index + 1] == "\n") or index == len(text) - 1) and text[index - 1] != "{" and ((not hide_curly) or isLambd) and item != ":":
            text[index] = item + "}"
            colon_balance -= 1

        if item == "(":
            hide_curly = True
            balancePerns += 1
        elif item == ")":
            hide_curly = False
            balancePerns -= 1
        
        if balancePerns == 0:
            in_perns = False
        elif balancePerns > 0:
            in_perns = True
            hide_curly = True

        if item == lambd[lambdIter]:
            lambdIter += 1
            if (lambdIter == len(lambd) - 1):
                isLambd = True
                lambdIter = 0
        else:
            lambdIter = 0

        if item == "{" and isLambd:
            lambdBalance += 1
            if (lambdFirst == False):
                lambdFirst = True

        if item == ":" and isLambd and not lambdFirst:
            isLambd = False
        
        if item == "}" and isLambd:
            lambdBalance -= 1
            if lambdBalance == 0 and isLambd and lambdFirst:
                isLambd = False
                lambdFirst = False

        


        if item == "\n" and balance == 0 and not in_perns:
            hide_curly = False
    return "".join(text)