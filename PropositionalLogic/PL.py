import re

def tt_entails(KB, alpha):
    
    symbols = proposition_symbols_in(KB, alpha)
    return tt_check_all(KB, alpha, symbols, {})

def tt_check_all(KB, alpha, symbols, model):
    
    if not symbols:
        if pl_true(KB, model):
            return pl_true(alpha, model)
        else:
            return True 
            
    P, rest = symbols[0], symbols[1:]
    return (
        tt_check_all(KB, alpha, rest, model | {P: True}) and
        tt_check_all(KB, alpha, rest, model | {P: False})
    )

# --- Required Helper Functions ---

def proposition_symbols_in(KB, alpha):
    
    combined = f"{KB} {alpha}"
    
    tokens = set(re.findall(r'\b[A-Z][A-Za-z0-9_]*\b', combined))
    tokens.discard('True')
    tokens.discard('False')
    return sorted(tokens)

def pl_true(sentence, model):
   
    expr = sentence
    
    for sym, val in model.items():
        expr = re.sub(rf'\b{sym}\b', str(val), expr)
        
    expr = expr.replace('~', ' not ')
    expr = expr.replace('&', ' and ')
    expr = expr.replace('|', ' or ')
   
    while '<->' in expr:
        expr = re.sub(r'(\([^()]+\)|True|False|not\s+\w+)\s*<->\s*(\([^()]+\)|True|False|not\s+\w+)', r'(\1 == \2)', expr)
    while '->' in expr:
        expr = re.sub(r'(\([^()]+\)|True|False|not\s+\w+)\s*->\s*(\([^()]+\)|True|False|not\s+\w+)', r'((not \1) or \2)', expr)
        
    return bool(eval(expr))


if __name__ == "__main__":
    # Modus Ponens test: (P -> Q) and P entails Q
    KB = "(P -> Q) & P"
    alpha = "Q"
    print(f"Does '{KB}' entail '{alpha}'? -> {tt_entails(KB, alpha)}")  # Output: True

    # Invalid inference test: (P -> Q) and Q does NOT entail P
    KB2 = "(P -> Q) & Q"
    alpha2 = "P"
    print(f"Does '{KB2}' entail '{alpha2}'? -> {tt_entails(KB2, alpha2)}")  # Output: False
