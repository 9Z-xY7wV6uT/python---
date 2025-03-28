print("1.입력한 수식 계산 2.두 수 사이의 합계:")
a = input()

if a == '1': 
    print("***수식을 입력하세요:")
    b = input()
    c = eval(b)
    print("{0}의 결과는 {1}입니다".format(b,c))

elif a == '2':
    print("***첫번쨰 숫자를 입력하세요:")
    num_f = input()
    print("***두번쨰 숫자를 입력하세요:")
    num_s = input()
    sigmaNum = (int(num_s)*(int(num_s)+1)/2)-((int(num_f)-1)*(int(num_f))/2)
    print("{0}+...+{1}는 {2}입니다.".format(num_f,num_s,sigmaNum))

else :
    print("1과2 중 하나를 선택하여 입력하여 주세요.")
