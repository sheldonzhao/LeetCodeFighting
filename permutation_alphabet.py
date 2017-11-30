def recursion(string, index, re_string):
    if len(string) == index:
        print(re_string)
        return
    else:
        r1, r2 = [], []
        for i in re_string:
            r1.append(i + string[index])
            if string[index].isupper():
                r2.append(i + string[index].lower())
            else:
                r2.append(i + string[index].upper())
        re_string = r1 + r2
        index += 1
        recursion(string, index, re_string)


string = 'abc'
re_string = ['']
ans = recursion(string, 0, re_string)
print(ans)
