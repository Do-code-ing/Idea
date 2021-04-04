from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Calculator") # 타이틀 설정
root.geometry("283x283") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
root.resizable(False, False)

frame = Frame(root)
frame.pack(side="left", fill="both", expand=True) # side= 위치, fill= 위 아래로 채우기, expand= 사방향으로 확대

txt = Text(root, width=11, height=21) # 글을 입력할 수 있는 한 줄의 텍스트 박스 생성
txt.pack()

def b1():
    txt.insert(END, "1")
def b2():
    txt.insert(END, "2")
def b3():
    txt.insert(END, "3")
def b4():
    txt.insert(END, "4")
def b5():
    txt.insert(END, "5")
def b6():
    txt.insert(END, "6")
def b7():
    txt.insert(END, "7")
def b8():
    txt.insert(END, "8")
def b9():
    txt.insert(END, "9")
def b0():
    txt.insert(END, "0")
def bclear():
    txt.delete("1.0", END)
def bdiv():
    txt.insert(END, "/")
def bmul():
    txt.insert(END, "*")
def bsub():
    txt.insert(END, "-")
def badd():
    txt.insert(END, "+")
def bpoint():
    txt.insert(END, ".")
def bback():
    back = txt.get("1.0", END)
    back = back[:-2]
    txt.delete("1.0", END)
    txt.insert(END, back)
def bequ():
    try:
        equal = txt.get("1.0", END)
        txt.delete("1.0", END)
        txt.insert(END, eval(equal))
    except SyntaxError:
        pass

# 맨 윗줄
btn_f16 = Button(frame, text="F16", width=5, height=2)
btn_f17 = Button(frame, text="F17", width=5, height=2)
btn_f18 = Button(frame, text="F18", width=5, height=2)
btn_f19 = Button(frame, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # sticky= 달라붙다, 동서남북 사방향으로, 그러면 늘어난다.
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear줄
btn_clear = Button(frame, text="clear", width=5, height=2, command=bclear)
btn_backs = Button(frame, text="<-", width=5, height=2, command=bback)
btn_div = Button(frame, text="/", width=5, height=2, command=bdiv) # div = divide 나누기
btn_mul = Button(frame, text="*", width=5, height=2, command=bmul) # mul = multiply 곱하기

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_backs.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7줄
btn_7 = Button(frame, text="7", width=5, height=2, command=b7)
btn_8 = Button(frame, text="8", width=5, height=2, command=b8)
btn_9 = Button(frame, text="9", width=5, height=2, command=b9)
btn_sub = Button(frame, text="-", width=5, height=2, command=bsub) # sub = subtraction 빼기

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4줄
btn_4 = Button(frame, text="4", width=5, height=2, command=b4)
btn_5 = Button(frame, text="5", width=5, height=2, command=b5)
btn_6 = Button(frame, text="6", width=5, height=2, command=b6)
btn_add = Button(frame, text="+", width=5, height=2, command=badd)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1줄
btn_1 = Button(frame, text="1", width=5, height=2, command=b1)
btn_2 = Button(frame, text="2", width=5, height=2, command=b2)
btn_3 = Button(frame, text="3", width=5, height=2, command=b3)
btn_enter = Button(frame, text="enter", command=bequ)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # rowspan=2 현재 row위치로 부터 아래쪽으로 몇 칸을 더함

# 0줄
btn_0 = Button(frame, text="0", width=5, height=2, command=b0)
btn_point = Button(frame, text=".", width=5, height=2, command=bpoint)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # 오른쪽으로 몇 칸을 더함
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게