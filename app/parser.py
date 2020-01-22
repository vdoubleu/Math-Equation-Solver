def make_map(exponents, coefficients):
    polynomial = {}
    for i in range(len(exponents)):
        polynomial[exponents[i]] = coefficients[i]
    return polynomial


def clean_string(s):
    i = 0
    size = len(s)
    while i < size:
        diff = ord(s[i]) - ord('0')
        if s[i] not in ['x', '^', '+', '-'] and (diff < 0 or diff > 9):
            s = s[0:i:] + s[i+1::]
            i -= 1
            size -= 1
        elif i == 0 and s[i] == 'x':
            s = '1' + s
            size += 1
            i+= 1
        elif i > 0 and s[i] == 'x' and (ord(s[i-1]) - ord('0') > 9 or ord(s[i-1]) - ord('0') < 0):
            s = s[:i] + '1' + s[i:]
            size += 1
            i += 1
        i += 1
    return s

def add_constants(s):
    sum = 0
    multiplier = 1
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        diff = ord(c) - ord('0')
        if 0 <= diff <= 9:
            sum += diff*multiplier
            multiplier *= 10
    return sum


def parse_coeff(s):
    coefficients = []
    pos = s.find('x')
    s = s[0:pos:] + s[pos+1::]

    while pos > 0 and pos <= len(s):
        pos -= 1
        coeff = ''

        if pos >= 0:
            c = s[pos]
            diff = ord(c) - ord('0')
            count = 0
        
            while 0 <= diff <= 9:
                count += 1
                coeff += c
                s = s[0:pos:] + s[pos+1::]
                pos -= 1
                if (pos >= 0):
                    c = s[pos]
                else:
                    pos = 0
                    break
                diff = ord(c) - ord('0')
        
            if count == 0:
                coeff = '1'
        
        else:
            coeff = '1'
            pos = 0
        
        coeff = coeff[::-1]

        x = int(coeff)
        if c == '-':
            x *= -1
        
        coefficients.append(x)

        coeff = ''
        pos = s.find('x', pos)

        if pos >= 0:
            s = s[0:pos:] + s[pos+1::]
        
    coefficients.append(add_constants(s))
    return coefficients


def parse_exponents(s):
    exponents = []
    pos = s.find('x')

    while (0 <= pos < len(s)):
        power = ''

        if pos + 1 < len(s) and s[pos+1] == '^':
            pos += 1
            s = s[0:pos:] + s[pos+1::]
            
            c = s[pos]
            diff = ord(c) - ord('0')

            while 0 <= diff <= 9:
                power += c
                s = s[0:pos:] + s[pos+1::]

                if pos < len(s):
                    c = s[pos]
                else:
                    break
                diff = ord(c) - ord('0')
        
        else:
            power = '1'
            pos += 1
        
        x = int(power)
        exponents.append(x)
        power = ''
        pos = s.find('x', pos)

    exponents.append(0)
    coefficients = parse_coeff(s)
    return make_map(exponents, coefficients)