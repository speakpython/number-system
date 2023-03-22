#https://speakpython.codes/number-system/2023/03/21/converting-hexadecimal-to-decimal-numbers.html#hextodecimal---custom-function

def hexToDecimal(hex):
    decimalValue = 0
    for i in range(len(hex)):
        ch = hex[i]
        
        if 'A' <= ch <= 'F' or '0' <= ch <= '9':
            decimalValue = decimalValue * 16 + hexCharToDecimal(ch)
        else:
            return None
    
    return decimalValue

def hexCharToDecimal(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    return int(ch)


#https://speakpython.codes/number-system/2023/03/21/converting-hexadecimal-to-decimal-numbers.html#driver-code---function-calling

hexData = input('Enter a hex number: ').strip()
decimal = hexToDecimal(hexData.upper())

print("The decimal value for hex number",hexData,"is",decimal) if decimal else  print("Incorrect hex number.")