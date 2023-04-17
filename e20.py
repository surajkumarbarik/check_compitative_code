def isValid(s):
    para = {"(":")","[":"]","{":"}"}
    lst = [i for i in s]
    response = False
    for sym in lst:
        if sym in para:
            if para[sym] in lst[lst.index(sym):]:
                response = True
            else:
                return False
        elif sym in para.values():
            # if (k for k, v in para.items() if v == sym) in lst[:lst.index(sym)]:
            response = any(k in lst[:lst.index(sym)] for k, v in para.items() if v == sym)
            if response== False:
                return False
        else:
            return False
    return response



s= "([]))" #dbl close one open to be handled
print(isValid(s))