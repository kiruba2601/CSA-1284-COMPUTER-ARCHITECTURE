def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
    print(decimalToBinary(88))
    print(decimalToBinary(186))
    print(decimalToBinary(127))
