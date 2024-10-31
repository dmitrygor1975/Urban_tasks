
def all_variants(text):
    for x in range (0,len(text)):
        for y in range(x+1,len(text)+1):
            res = text[x:y]
            yield res

sub_str = all_variants('abcde')

for a in sub_str:
    print(a)

