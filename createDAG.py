# 判断是不是数字
def JudgeNum(num):
    if len(num):
        if num[0] == "-":
            num = num[1:]
        if num.isdigit():
            return True
        if num.count(".") == 1:
            left, right = num.split(".")
            if left.isdigit() and right.isdigit():
                return True
    return False


# 判断该节点是不是存在，有利于后续操作
def JudgeExistNode(elem, node, left, right):
    if 'left' not in node:
        return False
    if left != node['left']:
        return False
    if 'right' not in node:
        return False
    if right != node['right']:
        return False
    if elem == node['sign'] or elem in node['affi_sign']:
        return True
    else:
        return False


# 判断是不是叶子节点
def JudgeLeaf(node):
    if 'son' in node or 'left' in node or 'right' in node:
        return False
    else:
        return True


# 判断DAG里面有没有节点node
# 1. 如果没有孩子节点和左右孩子结点, 检查该节点的标记和附加标记是否匹配
# 2. 带孩子结点的整体判断
def judgeInDAG(DAG, node, son=None, left=None, right=None):
    if not son and not left and not right:
        for e in DAG:
            if node == e['sign'] or node in e['affi_sign']:
                return True
    elif son:  # 第二类，带孩子结点的整体判断，必须
        for e in DAG:
            if 'son' in e:
                if (node == e['sign'] or node in e['affi_sign']) and index(DAG, son) == e['son']:
                    return True
    else:
        for e in DAG:
            lf = index(DAG, left)
            rg = index(DAG, right)
            if JudgeExistNode(node, e, lf, rg):
                return True
    return False


# 添加附加节点
def AppendAffiSign(DAG, sign, affi_sign, left=None, right=None, son=None):
    # 有左操作数和右操作数
    if left and right:
        # 得到左右操作数的对应结点标号
        lr = index(DAG, left)
        rg = index(DAG, right)
        for elem in DAG:
            if elem['sign'] == sign or sign in elem['affi_sign']:
                # 找到内部节点, 就查看叶子节点并删除公共子表达式, 即如果当前表达式存在则直接附加
                if 'left' in elem and lr == elem['left'] and 'right' in elem and rg == elem['right']:
                    elem['affi_sign'].append(affi_sign)
                    return
    # 赋值语句或单目运算
    else:
        # 单目运算
        if son:
            son = index(DAG, son)
            for elem in DAG:
                if elem['sign'] == sign or sign in elem['affi_sign']:
                    if "son" in elem and son == elem["son"]:
                        elem['affi_sign'].append(affi_sign)
                    return
        # 赋值运算
        else:
            for elem in DAG:
                if elem['sign'] == sign or sign in elem['affi_sign']:
                    elem['affi_sign'].append(affi_sign)


# 返回附属标记含x的元素下标
def index(DAG, x):
    # 四元式中的操作数不会是运算符，参加运算的是标记或者附加标记
    if x not in ['+', '-', '/', '*']:
        for i, e in enumerate(DAG):
            if x in e['affi_sign'] or x == e['sign']:
                return i
    return None


# 删除无用的附加值
def delete(DAG, affi_sign):
    for e in DAG:
        if affi_sign in e['affi_sign']:
            e['affi_sign'].remove(affi_sign)


# 连接附属标记含x与附属标记含y的结点
def link(DAG, father, son=None, left=None, right=None):
    if son:  # 如果是1型
        e = index(DAG, son)
        father['son'] = e
        if 'father' not in DAG[e]:
            DAG[e]['father'] = index(DAG, father)
    else:
        lf = index(DAG, left)
        rg = index(DAG, right)
        father['left'] = lf
        father['right'] = rg


# 构造DAG
def CreateDAG(codes: list):
    DAG = []
    for code in codes:
        # x = y, 其中间代码形式为: ('=', 'y', '', 'x')
        if code[0] == '=':
            # x之前存在, 删除无用赋值
            if judgeInDAG(DAG, code[3]):
                delete(DAG, code[3])
                pass
            # 准备操作数结点, 没有则新建
            if not judgeInDAG(DAG, code[1]):
                DAG.append({'sign': code[1], 'affi_sign': [code[3]]})
            # 存在操作数节点, 则直接附加
            else:
                AppendAffiSign(DAG, code[1], code[3])
        # 若是 x = op y, 四元式是：('op', 'y', '', 't') ('=', 't', '' ,'x')
        # 取地址, 取反等
        elif code[0] == '&' or code[0] == '~':
            if judgeInDAG(DAG, code[3]):
                delete(DAG, code[3])
                pass
            # 若y不存在, 则新建结点y准备操作数
            if not judgeInDAG(DAG, code[1]):
                DAG.append({'sign': code[1], 'affi_sign': []})
            # 再查找是否存在一个结点 op，其子结点为 y
            if not judgeInDAG(DAG, code[0], son=code[1]):
                # 连接两节点
                father = {'sign': code[0], 'affi_sign': [code[3]]}
                link(DAG, father, son=code[1])
                DAG.append(father)
            else:
                AppendAffiSign(DAG, code[0], code[3], son=code[1])
        # 若是 x = y op z, 四元式是：('op', 'y', 'z', 't') ('=', 't', '' ,'x')
        elif code[1] != '' and code[2] != '':
            if judgeInDAG(DAG, code[3]):
                delete(DAG, code[3])
                pass
            # 合并已知量
            if JudgeNum(code[1]) and judgeInDAG(DAG, code[2]) and JudgeNum(DAG[index(DAG, code[2])]["sign"]):
                if code[0] == "*":
                    new_sign = str(float(code[1]) * float(DAG[index(DAG, code[2])]["sign"]))
                elif code[0] == "/" and float(DAG[index(DAG, code[2])]["sign"]) != 0:
                    new_sign = str(float(code[1]) / float(DAG[index(DAG, code[2])]["sign"]))
                elif code[0] == "+":
                    new_sign = str(float(code[1]) + float(DAG[index(DAG, code[2])]["sign"]))
                elif code[0] == "-":
                    new_sign = str(float(code[1]) - float(DAG[index(DAG, code[2])]["sign"]))
                else:
                    if judgeInDAG(DAG, new_sign):
                        AppendAffiSign(DAG, new_sign, code[3])
                    else:
                        DAG.append({'sign': new_sign, 'affi_sign': [code[3]]})
            elif JudgeNum(code[2]) and judgeInDAG(DAG, code[1]) and JudgeNum(DAG[index(DAG, code[1])]["sign"]):
                if code[0] == "*":
                    new_sign = str(
                        float(code[2]) * float(DAG[index(DAG, code[1])]["sign"]))
                elif code[0] == "/" and float(DAG[index(DAG, code[1])]["sign"]) != 0:
                    new_sign = str(
                        float(code[2]) / float(DAG[index(DAG, code[1])]["sign"]))
                elif code[0] == "+":
                    new_sign = str(
                        float(code[2]) + float(DAG[index(DAG, code[1])]["sign"]))
                elif code[0] == "-":
                    new_sign = str(
                        float(code[2]) - float(DAG[index(DAG, code[1])]["sign"]))
                else:
                    pass
                if judgeInDAG(DAG, new_sign):
                    AppendAffiSign(DAG, new_sign, code[3])
                else:
                    DAG.append({'sign': new_sign, 'affi_sign': [code[3]]})
            # 没得合并, 而且两个操作数全是常数, 就创建节点
            elif JudgeNum(code[2]) and JudgeNum(code[1]):
                if code[0] == "*":
                    new_sign = str(float(code[1]) * float(code[2]))
                elif code[0] == "/" and code[2] != 0:
                    new_sign = str(float(code[1]) / float(code[2]))
                elif code[0] == "+":
                    new_sign = str(float(code[1]) + float(code[2]))
                elif code[0] == "-":
                    new_sign = str(float(code[1]) - float(code[2]))
                else:
                    pass
                DAG.append({'sign': new_sign, 'affi_sign': [code[3]]})
            # 两个操作数都是节点, 就创建一个父节点连接起来
            else:
                if not judgeInDAG(DAG, code[0], left=code[1], right=code[2]):
                    father = {'sign': code[0], 'affi_sign': [code[3]]}
                    # 准备操作数结点
                    if not judgeInDAG(DAG, code[1]):
                        DAG.append({'sign': code[1], 'affi_sign': []})
                    if not judgeInDAG(DAG, code[2]):
                        DAG.append({'sign': code[2], 'affi_sign': []})
                    link(DAG, father, left=code[1], right=code[2])
                    DAG.append(father)
                else:
                    AppendAffiSign(DAG, code[0], code[3], code[1], code[2])
    return DAG


# 优化DAG并生成优化后代码
def optimize(DAG):
    code = []
    # 生成新代码
    for e in DAG:
        if 'son' in e:
            son = DAG[e['son']]
            # 如果没有附加结点或者是是叶子节点，生成的代码等于其标记
            if not son['affi_sign'] or JudgeLeaf(son):
                # 必须父节点有附加标记才会生成代码
                if e['affi_sign']:
                    code.append((e['sign'], son['sign'], '', e['affi_sign'][0]))
                    for i in range(1, len(e['affi_sign'])):
                        code.append(("=", e['affi_sign'][0], '', e['affi_sign'][i]))
            # 如果孩子节点有附加节点，生成的代码使用其附加标记
            else:
                if son['affi_sign'] and e['affi_sign']:
                    code.append((e['sign'], son['affi_sign'][0], '', e['affi_sign'][0]))
                    for i in range(1, len(e['affi_sign'])):
                        code.append(("=", e['affi_sign'][0], '', e['affi_sign'][i]))
        elif 'left' in e and 'right' in e:
            left = DAG[e['left']]
            right = DAG[e['right']]
            if not left['affi_sign'] or JudgeLeaf(left):
                arg1 = left['sign']
            else:
                arg1 = left['affi_sign'][0]
            if not right['affi_sign'] or JudgeLeaf(right):
                arg2 = right['sign']
            else:
                arg2 = right['affi_sign'][0]
            # 第一个附加标识符用表达式表示，后面的附加标识符统一用第一个附加标识符表示
            if e['affi_sign']:
                code.append((e['sign'], arg1, arg2, e['affi_sign'][0]))
                for i in range(1, len(e['affi_sign'])):
                    code.append(("=", e['affi_sign'][0], '', e['affi_sign'][i]))
        else:
            for elem in e["affi_sign"]:
                code.append(("=", e["sign"], " ", elem))
    return code
