def check(L):
    s=''
    for a in L :
        s+=', '+a
    return s[2:]

def comma_code(L):
    if not L:
        return ''  # handle empty list
    
    if len(L) == 1:
        return L[0]  # single item, no commas needed
    
    # Join all but last item, then add ', and' + last item
    return ', '.join(L) 

# Tests
spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))
# Output: apples, bananas, tofu, and cats

# Additional test cases:
print(comma_code(['apples', 'bananas']))
# Output: apples, and bananas

print(comma_code(['apples']))
# Output: apples

print(comma_code([]))

spam = ['apples', 'bananas', 'tofu', 'cats']
print(check(spam))
