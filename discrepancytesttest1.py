with open("discrepancytestdomsamfixbp16.csv", "r") as r1:
    for lines in r1:
        if list(lines.split(","))[-2]!=list(lines.split(","))[-1]:
            if list(lines.split(","))[1]!="basepos" and list(lines.split(","))[1]!="coverage" and list(lines.split(","))[1]!="Variant frequency":
                print(lines)
