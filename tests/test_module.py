seq_ele = [None, 1,2, None, 3]
replace_value: (int|str) = "hello"  

SEQ_LEN = len(seq_ele)
for _ in range(SEQ_LEN):
    if None in seq_ele:
        idx = seq_ele.index(None) 
        seq_ele[idx] = replace_value 
    elif "" in seq_ele:
        idx = seq_ele.index("") 
        seq_ele[idx] = replace_value 
    else:
        break; 
print(seq_ele)




