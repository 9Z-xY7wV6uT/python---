print("입력 진수 결정(16/10/8/2):")
a = input()
print("값 입력:")
b = input()
q = int(a)
c = hex(int(b,q))
o = oct(int(b,q))
e = bin(int(b,q))
if a == '16':
    print("16진수 ==>",c)
    print("10진수 ==>",int(c,16))
    print(" 8진수 ==>",o)
    print(" 2진수 ==>",e)

elif a == '10':
    print("16진수 ==>",hex(int(b)))
    print("10진수 ==>",b)
    print(" 8진수 ==>",oct(int(b)))
    print(" 2진수 ==>",bin(int(b)))

elif a == '8':
    print("16진수 ==>",c)
    print("10진수 ==>",int(b,8))
    print(" 8진수 ==>",o)
    print(" 2진수 ==>",e)

elif a == '2':
    print("16진수 ==>",c)
    print("10진수 ==>",int(b,2))
    print(" 8진수 ==>",o)
    print(" 2진수 ==>",e)              