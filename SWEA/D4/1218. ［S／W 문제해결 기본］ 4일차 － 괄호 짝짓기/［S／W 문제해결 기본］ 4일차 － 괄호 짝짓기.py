for test_case in range(10):
    test_len = int(input())
    str_seq = list(map(str, input()))

    bigyo = []
    is_balanced = True

    for i in range(len(str_seq)):
        if str_seq[i] in '([{<':
            bigyo.append(str_seq[i])
        elif str_seq[i] in ')]}>':
            if bigyo:
                last = bigyo[-1]
                if (last == '(' and str_seq[i] == ')') or \
                   (last == '[' and str_seq[i] == ']') or \
                   (last == '{' and str_seq[i] == '}') or \
                   (last == '<' and str_seq[i] == '>'):
                    bigyo.pop()
                else:
                    is_balanced = False
                    break
            else:
                is_balanced = False
                break


    result = 1 if is_balanced and not bigyo else 0
    print(f'#{test_case+1} {result}')