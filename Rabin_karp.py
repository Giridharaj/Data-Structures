def rabin_karp(text,pattern,d=256,q=101):
    n=len(text)
    m=len(pattern)
    matches=[]

    if m==0 or m>n:
        return matches

    h=pow(d,m-1,q)
    p_hash=0
    t_hash=0

    for i in range(m):
        p_hash=(d*p_hash+ord(pattern[i]))%q
        t_hash=(d*t_hash+ord(text[i]))%q

    for i in range(n-m+1):
        if p_hash==t_hash:
            if text[i:i+m]==pattern:
                matches.append(i)
        if i<n-m:
            t_hash=(d*(t_hash-ord(text[i])*h+ord(text[i+m])))%q

            if t_hash<0:
                t_hash+=q

    return matches

if __name__=='__main__':
    text='power is a state of mind'
    pattern='state'

    result=rabin_karp(text,pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Pattern found at indices: {result}")