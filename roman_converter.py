# converts roman literals to arabic int number
def convert(s:str) -> int:
    s = s.upper()
    if not all(ch in "IVXLCDM" for ch in s):
        raise(ValueError)
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    number=0
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[(i+1)]]:
            number-=roman[s[i]]
        else:
            number+=roman[s[i]]
    return number+roman[s[-1]]