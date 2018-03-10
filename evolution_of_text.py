import random
def list_to_str(text_list):
    ans = ''
    for i in range(0,len(text_list)):
        ans += text_list[i]
    print(ans)

def evolution_of_text():
    target_text = str(input('Enter the target text: \n'))
    chars = []
    counter = 0
    for i in range(32,123):
        chars.append(chr(i))
    answer = []
    for i in range(0,len(target_text)):
        answer.append(random.choice(chars))
    while list(target_text) != answer:
        list_to_str(answer)
        for i in range(0,len(target_text)):
            if answer[i] == target_text[i]:
                pass
            else:
                answer[i] = random.choice(chars)

        counter += 1
    answer_str = ''
    for i in range(0, len(answer)):
        answer_str += answer[i]

    print(answer_str)
    print(counter)


evolution_of_text()
