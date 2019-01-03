#Simple GCD Program
->factors of 'm'
->factors of 'n'
->common factors
->return largest value in cf i.e. rightmost value denoted by -1

def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i==0):
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if(n%j==0):
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])

e.g gcd(14,63)
fm=[1,2,7,14]
fn=[1,3,7,,9,21,63]
cf=[1,7]
answer=7

#Naive GCD

1)By calculating a list of common factor and return the rightmost element.

    def gcd(m,n):
        cf=[]
        for i in range(1,min(m,n)+1):
            if(m%i==0 and n%i==0):
                cf.append(i)
        return(cf[-1])
        
e.g gcd(14,63)
cf=[1,7]
answer=7
    
2)By using most Recent Common Factor

    def gcd(m,n):
        for i in range (1,min(m,n)+1):
            if(m%i==0 and n%i==0):
                mrcf=i
        return(mrcf)

3)Backtrace

    def gcd(m,n):
        i=min(m,n)
        while i>0:
            if(m%i==0 and n%i==0):
                return(i)
            else:
                i=i-1
                
                

#GCD program using Euclid algorithm
i.e m=qn+r 
where m=dividend
q=quotient
n=divisor
r=remainder

def gcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    while(m%n)!=0:
        (m,n)=(n,m%n)
        return(n)
        
            
