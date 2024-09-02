def all_variants(text):
    n = len(text)
    for s in range(n + 1):
        for j in range(s + 1, n + 1):
            yield text[s:j]


a = all_variants("abc")
for i in a:
    print(i)
