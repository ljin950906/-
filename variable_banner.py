##Variable Banner

def variable_banner(name):
    len_name = len(name)
    num_stars = len_name + 2
    a = '*'*num_stars
    print(a+'\n'+'*'+name+'*'+'\n'+a)
