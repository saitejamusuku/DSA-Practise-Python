def second_larg(lis):
    f_max = lis[0]
    s_max = 0
    for i in lis:
        if f_max < i:
            s_max = f_max
            f_max = lis[i]
    return s_max

if __name__ == "__main__":
    lis= list(map(int, input().split()))
    print(second_larg(lis))