# 10진수 > f진수
n = 10 # 10진법인 수
f = 2 # 진법
m = "" # f진법의 수 담을 문자열
while n > 0:
    a, b = divmod(n, f)
    m += str(b)
    n = a
real_m = m[::-1] # 거꾸로 세야해요.
print(real_m)

# f진수 > 10진수
d_num_m = int(real_m, f)
print(d_num_m)