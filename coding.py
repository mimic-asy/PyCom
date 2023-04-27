import make_tree as tree
def generator(lis):
    if lis.kind == tree.TK_NUM:
        print("     push" ,lis.val)
        return
    
    generator(lis.lhs)
    generator(lis.rhs)

    print( "     pop rdi")
    print( "     pop rax")

    if lis.kind == tree.ND_ADD:
        print("     add rax, rdi")
    if lis.kind == tree.ND_SUB:
        print("     sub rax, rdi")
    if lis.kind == tree.ND_MUL:
        print("     imul rax, rdi")
    if lis.kind == tree.ND_DIV:
        print("     idiv rax, rdi")
    if lis.kind == tree.ND_EQ:
        print("     cmp rax, al")
        print("     sete al")
        print("     movzb rax, al")
    if lis.kind == tree.ND_NE:
        print("     cmp rax, al")
        print("     setne al")
        print("     movzb rax, al")
    if lis.kind == tree.ND_LT:
        print("     cmp rax, al")
        print("     setl al")
        print("     movzb rax, al")
    if lis.kind == tree.ND_LE:
        print("     cmp rax, al")
        print("     setle al")
        print("     movzb rax, al")
    
    print("     push rax")
    
