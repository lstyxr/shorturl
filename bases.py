baseList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def changeBase(n,b):
    x,y = divmod(n,b)
    if x>0:
        return changeBase(x,b) + baseList[y]
    else:             
        return baseList[y]

def changeToTenBase(s,b):
    sL = list(s)
    sL.reverse()
    result = 0
    for x in range(len(sL)):
        result = result + baseList.index(sL[x])*(b**x)
    return result


def is_polydivisible(s, b):
    for x in range(len(s)):    
        if changeToTenBase(s[:x+1],b)%(x+1) != 0:
            return False
    return True


def get_polydivisible(n, b):
    count = 0
    result = 0
    while count < n:
        baseResult = changeBase(result,b)
        if is_polydivisible(baseResult,b):
            count = count + 1
        result = result + 1
    return baseResult


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

if __name__ == '__main__':
    # print(changeBase(1000000,62))
    # print(changeBase(3969,62))
    # print(changeBase(15,2))
    # print(changeBase(15,7))
    # print(changeBase(6,8))
    # print(changeBase(32,30))
    print(base62_decode("D"))