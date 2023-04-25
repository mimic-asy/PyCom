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

    s = []
    for c in strip_formula:
        if len(s) == 0:
            s.append(c)
            continue

        if c.isdigit() and s[-1].isdigit():
            s[-1] = s[-1] + c
            continue

        s.append(c)
    return s

#分割した数式の記号を一つにする
def binary_set(s):
    neat_formulas = []
    front_binary = "first"
    for i in s:
        if i.isdigit():
            if front_binary != "first":
                neat_formulas.append(front_binary)
                neat_formulas.append(i)
            else:
                neat_formulas.append(i)
        else:
            if front_binary != "first":
                if i == "=":
                        set =[]
                        set.append(front_binary)
                        set.append(i)
                        front_binary = "".join(set)
                        neat_formulas.append(front_binary)

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











