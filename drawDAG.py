from graphviz import Digraph


def draw(codes):
    dot = Digraph(comment='The Round Table', filename='result', format='png', strict=False)
    idx = 1
    for code in codes:
        s = code['sign'] + '|' + ''.join(code['affi_sign'])
        dot.node(str(idx), s, color="#00ff00")
        idx += 1
    for i, code in enumerate(codes):
        if 'son' in code:
            # dot.edge(str(i+1), str(code['son'][0] + 1))
            dot.edge(str(i + 1), str(code['son'] + 1))
        if 'left' in code:
            dot.edge(str(i + 1), str(code['left'] + 1))
        if 'right' in code:
            dot.edge(str(i + 1), str(code['right'] + 1))
    dot.render()
