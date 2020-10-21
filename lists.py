names = ['bastian','tiffany','leilani']
transportation_list = []

def print_lists(names):
    for i in names:
        print(i)

def greeting():
    for i in names:
        print("here is the name: ", i)

def trans_list():
    transportation_list.append('I')
    print(transportation_list)
    transportation_list.append('Hate')
    print(transportation_list)
    transportation_list.append('plumbing issues')
    print(transportation_list)
    transportation_list.insert(0, 'Bastian')
    transportation_list.remove('I')
    print(transportation_list)
    print(transportation_list.pop())

def guest(names):
    new_name = 'bastian'
    if new_name in names:
        print('Sorry ',new_name,' cant make it.')
    else:
        for i in names:
            print("Please join my dinner party",i)


#print_lists(names)
#greeting()
#trans_list()
guest(names)