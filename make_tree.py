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
    print("now expr , lis[",m,"] = ",lis[m])
    print("-> equaloity")
    setting = equality(lis,m)
    return setting[0]


def equality(lis,m):
    setting = relational(lis,m)
    node = setting[0]
    m = setting[1]

    for i in range(len(lis)):
        if consume(lis[i],'=='):
            m = i
            m+=1
            node = new_binary(ND_EQ, node, relational(lis,m))
        elif consume(lis[i],'!='):
            m = i
            m+=1
            node = new_binary(ND_NE, node, relational(lis,m))    
        else:
            print("now equality , lis[",m,"] = ",lis[m])
            print("-> relational")
            return node, m
        

def relational(lis,m):
    setting = add(lis,m)
    node = setting[0]
    m = setting[1]
    for i in range(len(lis)):
        if consume(lis[i], '<'):
            m = i
            m+=1
            node = new_binary(ND_LT,node,add(lis,m))
      
        elif consume(lis[i], '<='):
            m = i
            m+=1
            node = new_binary(ND_LE,node,add(lis,m))
        elif consume(lis[i], '>'):
            m = i
            m+=1
            node = new_binary(ND_LT,add(lis,m),node)
            
        elif consume(lis[i], '>='):
            m = i
            m+=1
            node = new_binary(ND_LT,add(lis,m),node)
        else:
            print("now relational , lis[",m,"] = ",lis[m])
            print("-> add")
            return node ,m

def add(lis,m):
    setting = mul(lis,m)
    node = setting[0]
    m = setting[1]
    for i in range(len(lis)):
        if consume(lis[i],'+'):
            print("now add , lis[",m,"] = ",lis[m])
            n = i +1
            node = new_binary(ND_ADD, node, mul(lis, n))
        elif consume(lis[i],'-'):
            n = i +1
            node = new_binary(ND_SUB,node,mul(lis,n))
        else:
            print("now add , lis[",m,"] = ",lis[m])
            print("-> mul")
            return node,m

def mul(lis,m):
    setting = unary(lis,m)
    node = setting[0]
    m = setting[1]    
    for i in range(len(lis)):
        if consume(lis[i],'*'):
            m = i
            m+=1
            node = new_binary(ND_MUL,node,unary(lis,m))
        elif consume(lis[i],'/'):
            m = i
            m+=1
            node = new_binary(ND_DIV,node,unary(lis,m))
        else:
            print("now mul , lis[",m,"] = ",lis[m])
            print("-> unary")
            return node,m
        
def unary(lis,m):
    if consume(lis[m],'+'):
        m += 1
        print("-> second unary")
        return unary(lis,m)
    elif consume(lis[m],'-'):
        m+= 1
        return new_binary(ND_SUB,0,unary(lis,m))
    else:
        print("now unary , lis[",m,"] = ",lis[m])
        print("-> primary")
        return primary(lis,m),m


def primary(lis,m):
    if consume(lis[m],'('):
        m+=1
        node = expr(lis,m)
        expect(lis[m],')')
        m+=1
        return node,m
    else: 
        inta = expect_number(lis,m)
        node = new_node(TK_NUM,inta)
        print("now primary ",node)
        m+=1
        return node,m

lis = ['1','+','2']

print(expr(lis,0))