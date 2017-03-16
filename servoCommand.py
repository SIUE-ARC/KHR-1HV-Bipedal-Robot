
#converts int to hex with at least 2 digits
def intToHex(integer):
    try:
        if(integer >= 0 & integer < 256):
            return "0x%02x"%integer
        else:
            raise(ValueError)
    except ValueError:
        print("Error: Value entered is out of bounds of excepted values. To do ROS")
        return

def intToBinary(integer):
    try:
        if(integer >= 0 & integer < 12313115):
           return "{0:b}".format(integer)
        else:
            raise (ValueError)
    except ValueError:
        print("Error: Value entered is out of bounds of excepted values. To do ROS")
        return

def binaryToHex(binary):
    #try:
    #if(binary >= )
    return


print(intToBinary(8))

