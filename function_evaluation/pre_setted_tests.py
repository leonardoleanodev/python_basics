def main_test(module):
    """
    return a number of score of the test
    """
    test_scores = []
    reasons = ''

    try:
        func = module.numero_magico
    except:
        reasons += "nome da funcao incorreto."
    # A
    try:
        score = test_a(func)
        test_scores.append(score)
        if score == 0:
            reasons += test_a.__doc__
    except:
        reasons += test_a.__doc__
    # B
    try:
        score = test_b(func)
        test_scores.append(score)
        if score == 0:
            reasons += test_b.__doc__
    except:
        reasons += test_b.__doc__
    # C
    try:
        score = test_c(func)
        test_scores.append(score)
        if score == 0:
            reasons += test_c.__doc__
    except:
        reasons += test_c.__doc__
    # D
    try:
        score = test_d(func)
        test_scores.append(score)
        if score == 0:
            reasons += test_d.__doc__
    except:
        reasons += test_d.__doc__
    
    # E
    try:
        score = test_e(func)
        test_scores.append(score)
        if score == 0:
            reasons += test_e.__doc__
    except:
        reasons += test_e.__doc__

    # F
    try:
        score = test_f(func)
        test_scores.append(score)
        if score == 0:
            reasons += test_f.__doc__
    except:
        reasons += test_f.__doc__

    print(test_scores)
    score = sum(test_scores)
    return score, reasons

def test_a(func):
    """nao passou pelo 'nao valido'
    """
    if func(2.2)=='nao valido':
        return 1
    return 0

def test_b(func):
    """nao passou pelo 'magico'
    """
    if func(3)=='magico':
        return 1
    return 0

def test_c(func):
    """nao passou pelo 'menor'
    """
    if func(2)=='menor':
        return 1
    return 0

def test_d(func):
    """nao passou pelo 'maior'
    """
    if func(4)=='maior':
        return 1
    return 0

def test_e(func):
    """nao passou pelo 'muito menor'
    """
    if func(7)=='muito maior':
        return 1
    return 0

def test_f(func):
    """nao passou pelo 'muito menor'
    """
    if func(1)=='muito menor':
        return 1
    return 0


