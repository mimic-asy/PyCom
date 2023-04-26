TK_NUM = 995
TK_EQ = 996
TK_NE = 997
TK_LT = 998
TK_LE = 999

ND_ADD = '+'
ND_SUB = '-'
ND_MUL = '*'
ND_DIV = '/'
ND_EQ = '=='
ND_NE = '!='
ND_LT = '<'
ND_LE = '<='

class Node:
    def __init__(self,kind,lhs,rhs,val):
        self.kind = kind
        self.lhs = lhs
        self.rhs = rhs
        self.val = val

#記号チェック用
def consume(lism,op):
    if  lism != op:
        return False
    
    return True


#エラーを出す用
def expect(lism,op):

    if lism != op:
        raise ValueError(f'"{op}"ではありません')
    
#数字を返す用
def expect_number(lis,m):

    if lis[m].isdigit():
        number_node = int(lis[m])

        return number_node
        

    raise ValueError(f'"数字ではありません"')

def new_node(nodekind,val):
    node = Node(nodekind,0,0,val)
    return node


def new_binary(nodekind, lhs, rhs):
    node = Node(nodekind, lhs, rhs, 0)
    return node



def expr(lis,m):

    node,m = equality(lis,m)
    return node , m


def equality(lis,m):
    node,m = relational(lis,m)

    while m < len(lis):
        if consume(lis[m],'=='):
            m+=1
            rhs,m = relational(lis,m)
            node = new_binary(ND_EQ, node, rhs)
        elif consume(lis[m],'!='):
            m+=1
            rhs,m = relational(lis,m)
            node= new_binary(ND_NE, node, rhs)
        else:
            break    

    return node, m
        

def relational(lis,m):
    node,m = add(lis,m)

    while m < len(lis):
        if consume(lis[m], '<'):
         
            m+=1
            rhs,m = add(lis,m)
            node = new_binary(ND_LT,node,rhs)
      
        elif consume(lis[m], '<='):
           
            m+=1
            rhs,m = add(lis,m)
            node = new_binary(ND_LE,node,rhs)
        elif consume(lis[m], '>'):
           
            m+=1
            rhs,m = add(lis,m)
            node = new_binary(ND_LT,rhs,node)
            
        elif consume(lis[m], '>='):
         
            m+=1
            rhs,m = add(lis,m)
            node = new_binary(ND_LT,rhs,node)
        
        else:
            break
    return node ,m

def add(lis,m):
    node,m = mul(lis,m)
    
    while m < len(lis):
        if consume(lis[m],'+'):
            m += 1
            rhs,m = add(lis,m)
            node = new_binary(ND_ADD, node, rhs)
        elif consume(lis[m],'-'):
            m +=1
            rhs,m = add(lis,m)
            node = new_binary(ND_SUB,node,rhs)
        else:
            break
            
    return node,m

def mul(lis,m):
    node,m = unary(lis,m)
 
    while m < len(lis):
        if consume(lis[m],'*'):
            m +=1
            rhs,m = unary(lis,m)
            node = new_binary(ND_MUL,node,rhs)
        elif consume(lis[m],'/'):
            m+=1
            rhs,m = unary(lis,m)
            node = new_binary(ND_DIV,node,rhs)
        else:
            break

    return node, m
    
        
def unary(lis,m):
    if consume(lis[m],'+'):
        m += 1
        node,m = unary(lis,m)
        return node ,m
    elif consume(lis[m],'-'):
        m += 1
        rhs,m =unary(lis,m)
        return new_binary(ND_SUB,0,rhs)
    else:
        node, m = primary(lis,m) 
        return node,m


def primary(lis,m):
    if consume(lis[m],'('):
        m+=1
        node,m= expr(lis,m)
        expect(lis[m],')')
        m+=1
        return node,m
    else: 
        inta = expect_number(lis,m)
        node = new_node(TK_NUM,inta)
        m+=1
        return node,m

lis = ['12','==','22']
node,m = expr(lis,0)
print(node.kind)
left = node.lhs
print(left.kind,left.val)
right = node.rhs
print(right.kind,right.val)