
def rev(s):
    if len(s) == 0 or len(s) == 1: 
        return s

    else:
        
        head = s[0]
        tail = s[1:]
        return rev(tail) + head
    
print('Original Word: pots&pans ')
print('Reversed: ',rev('pots&pans'))
