password = 'a123456'
x = 3
while x > 0:
    pwd = input('entry password:')
    if pwd == password:
    	print('welcome!')
    	break
    else:
        x = x - 1
        print('wrong! left', x,'time')
        if x == 0:
        	break
