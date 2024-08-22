def all_variants(text):
    for i in range(1, len(text)+1):
        for j in range(len(text)):
            if j != j+i and j+i <= len(text):
                str_ = text[j:j+i]
                yield str_
            
a = all_variants("abc")
for i in a:
    print(i)