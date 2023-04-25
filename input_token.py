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
    for i in s:
        if i.isdigit():
            neat_formulas.append(i)
            continue

        if (i == '=' and neat_formulas[-1] == '='
            or neat_formulas[-1] == '!' or neat_formulas == '<'
            or neat_formulas[-1] == '>'):
            neat_formulas[-1] = neat_formulas[-1] + i
            continue
        
        neat_formulas.append(i)

 
    return neat_formulas











