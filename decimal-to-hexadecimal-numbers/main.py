#https://speakpython.codes/number-system/2023/03/22/decimal-to-hexadecimal-numbers.html#decimaltohex---custom-function


def decimalToHex(decimalValue):
    hex = ""
    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex

def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return str(hexValue)
    return chr(hexValue - 10 + ord('A'))


#https://speakpython.codes/number-system/2023/03/22/decimal-to-hexadecimal-numbers.html#driver-code---function-calling


decimalValue = int(input("Enter a decimal Value: "))
print("The hex number for decimal", decimalValue, "is", decimalToHex(decimalValue))