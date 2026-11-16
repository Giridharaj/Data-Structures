def compute_lps_array(pattern):
    m=len(pattern)
    lps=[0]*m
    k=0
    for q in range(1,m):
        while(k>0 and pattern[k]!=pattern[q]):
            k=lps[k-1]
        if pattern[k]==pattern[q]:
            k+=1
        lps[q]=k
    return lps

def kmp_search(text,pattern):
    n=len(text)
    m=len(pattern)
    if m==0 or n==0 or m>n:
        return []

    lps=compute_lps_array(pattern)
    q=0
    matches=[]
    for i in range(n):
        while(q>0 and pattern[q]!=text[i]):
            q=lps[q-1]
        if pattern[q]==text[i]:
            q+=1
        if q==m:
            matches.append(i-m+1)
            q=lps[q-1]

    return matches

text='AAABAACAADAABADA'
pattern='CAAD'

matches=kmp_search(text,pattern)
print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"Pattern found at starting indices: {matches}")

