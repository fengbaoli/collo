def encrypt(key, s):
    b = bytearray(str(s).encode("gbk"))
    n = len(b)
    c = bytearray(n*2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key
        c1 = b2 % 16
        c2 = b2 // 16
        c1 = c1 + 65
        c2 = c2 + 65
        c[j] = c1
        c[j+1] = c2
        j = j+2
    return c.decode("gbk")
if __name__=="__main__":
   import sys
   key = int(sys.argv[1])
   s =   sys.argv[2]
   code = encrypt(key, s)
   print code