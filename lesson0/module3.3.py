def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = (1,'One',True)
values_disc = {'1': 1,'One': 'строка','True':True}
print_params(*values_disc)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)