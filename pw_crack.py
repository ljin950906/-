user_data= {'name':"ljin0906", 'pw':'qnrgkstks56', 'ip':'10-255-255-9'}

def get_data(dic):
    user_name = dic['name']
    user_pw = dic['pw']
    user_ip = dic['ip']
    return (user_name, user_pw, user_ip)


def password_crack():
    user_name, user_pw, user_ip = get_data(user_data)
    #creating alphabet list (lower)
    alphabets = []
    for letter in range(97,123):
        alphabets.append(chr(letter))

    #list of numbers
    nums = ['0','1','2','3','4','5','6','7','8','9']

    #별표시
    ex = ''
    for ch in user_pw:
        ex += '*'
    print("The password is set as " + ex)

    #case to store password
    broken_pw = []


    #solving the problem
    for ch in user_pw:
        if ch in nums:
            for num in nums:
                if ch!=num:
                    pass
                else:
                    broken_pw.append(ch)
                
        elif ch in alphabets:
            for alp in alphabets:
                if ch != alp:
                    pass
                else:
                    broken_pw.append(ch)
                
        else:
            print("This password is too strong for me to crack atm")
    print("Password cracked!")
    print("Password is...")
    print(broken_pw)
    return None


password_crack()
