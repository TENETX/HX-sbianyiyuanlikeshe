from createDAG import CreateDAG, optimize
from drawDAG import draw


# 把字符串的四元式转成list四元式:(OP, arg1, arg2, result)
def transfer(s):
    res = []
    lines = s.split('\n')
    for line in lines:
        factors = line.split(',')
        if len(factors) == 4:
            res.append((factors[0], factors[1], factors[2], factors[3]))
        else:
            return '', False
    return res, True


def startrun(code):
    DAG = CreateDAG(code)
    codes = optimize(DAG)
    draw(DAG)
    return DAG, codes


if __name__ == '__main__':
    startrun()
