def vowel(x):
    x=x.lower()
    set_1=set()
    y=["a","e","i","o","u"]
    for i in x:
        if i in y:
            set_1.add(i)
            print(set_1)
        else:
            pass
    
            
    if(len(y)==len(set_1)):
        print('Accept')
    else:
        print("Not Accept")
x="SEEquoiaL"
print(vowel(x))
        
        
