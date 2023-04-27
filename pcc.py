import input_token as token
import make_tree as tree
import coding as code
def main():
    user_input = token.input_formura()
    form = token.judge_num(user_input)
    formula = token.binary_set(form)
    tree_formula,m = tree.expr(formula,0)
    codeing = code.generator(tree_formula)


 



main()
            

