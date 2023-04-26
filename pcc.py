import input_token as token
import make_tree as tree
def main():
    user_input = token.input_formura()
    form = token.judge_num(user_input)
    print(form) 
    formula = token.binary_set(form)
    print(formula)
    tree_formula,m = tree.expr(formula,0)
    print(tree_formula.kind)
    left = tree_formula.lhs
    right = tree_formula.rhs
    print(left.kind, left.lhs, left.rhs, left.val)
    print(right.kind,right.lhs, right.rhs, right.val)


 



main()
            

