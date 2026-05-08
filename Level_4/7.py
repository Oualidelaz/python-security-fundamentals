# Define XOR key
# Any character value will work
# calculate length of input string
# perform XOR operation of key
# with every character in string

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101


def xorEncryptDecrypt(data):
    key = "P"
    length = len(data)
    
    for i in range(length):
        data = (
            data[:i] + chr(
                ord(data[i]) ^ ord(key)
            ) + data[i+1:]
        )
        print(data[i], end="")
    return data


if __name__ == '__main__':
    sampleString = "GeeksforGeeks";

    # Encrypt the string
    print("Encrypted String: ", end = "");
    sampleString = xorEncryptDecrypt(sampleString);
    print("\n");

    # Decrypt the string
    print("Decrypted String: ", end = "");
    xorEncryptDecrypt(sampleString);