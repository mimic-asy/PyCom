import make_tree as tree


#入力した数式を分割する
def input_formura():
    input_formula = input("数式を入力してください")
    strip_formula = list(filter(lambda x: x != ' ', input_formula))
    strip_formula.append('end')
    print(strip_formula)
    return strip_formula

#分割した数式の数字が２桁以上の場合、合体させる
def judge_num(strip_formula):
    frontnum = "first"

    organized_numbers= []
    for i in strip_formula:
        if i.isdigit():
            if frontnum == "first":
                frontnum = i
            else:
                frontnum = "".join([frontnum, i])
            continue

        if frontnum != "first":
            organized_numbers.append(frontnum)
            
        if i != "end":
            organized_numbers.append(i)
            frontnum = "first"
        
    return organized_numbers

#分割した数式の記号を一つにする
def binary_set(organized_numbers):
    neat_formulas = []
    front_binary = "first"
    set = []
    for i in organized_numbers:
        if i.isdigit():
            if front_binary != "first":
                neat_formulas.append(front_binary)
                neat_formulas.append(i)
            else:
                neat_formulas.append(i)
        else:
            if front_binary != "first":
                if i == "=":
                        set.append(front_binary)
                        set.append(i)
                        front_binary = "".join(set)
                        neat_formulas.append(front_binary)
                        set.clear()
                        front_binary = "first"
                else:
                    neat_formulas.append(front_binary)
                    neat_formulas.append(i)
                    front_binary = "first"
            
            else: 
                if i == "<" or i == "=":
                    front_binary = i
                else:
                    neat_formulas.append(i)
 
    return neat_formulas











