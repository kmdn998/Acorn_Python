import random

com = random.choice(["가위", "바위", "보"])
user = input("(가위,바위,보) 중에서 하나를 선택: ")

if user == "가위":
    if com == "가위":     #중첩 조건문: 코드 이해, 수정 쉬워짐
        print("컴퓨터:", com, ", 사용자: 가위")
        print("무승부입니다.")

    elif com == "바위":
        print("컴퓨터:", com, ", 사용자: 가위")
        print("컴퓨터가 이겼습니다.")

    else:
        print("컴퓨터:", com, ", 사용자: 가위")
        print("사용자가 이겼습니다.")

elif user == "바위":
    if com == "가위":
        print("컴퓨터:", com, ", 사용자: 바위")
        print("사용자가 이겼습니다.")

    elif com == "바위":
        print("컴퓨터:", com, ", 사용자: 바위")
        print("무승부입니다.")

    else:
        print("컴퓨터:", com, ", 사용자: 바위")
        print("컴퓨터가 이겼습니다.")

else:
    if com == "가위":
        print("컴퓨터:", com, ", 사용자: 보")
        print("컴퓨터가 이겼습니다.")

    elif com == "바위":
        print("컴퓨터:", com, ", 사용자: 보")
        print("사용자가 이겼습니다.")

    else:
        print("컴퓨터:", com, ", 사용자: 보")
        print("무승부입니다.")