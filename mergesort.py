def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)#current position in a,b

    while i+j < m+n:#i+j is no of elements sorted so far

        if i==m:#'a[]' is empty,add 'b[]' to 'c[]'
            c.append(b[j])
            j=j+1

        elif j==n:#'b[]' is empty,add 'a[]' to 'c[]'
            c.append(a[i])
            i=i+1

        elif a[i]<=b[j]:#head of 'a[]' is smaller
            c.append(a[i])
            i=i+1

        elif a[i]>b[j]:#head of 'b[]' is smaller
            c.append(b[j])
            j=j+1

    return(c)


def mergesort(a,l,r):
    #sort the slice a[left:right]

    if r-l <= 1:#Base case
        return(a[l:r])

    if r-l > 1:#recursive call

        mid=(l+r)//2
        left=mergesort(a,l,mid)
        right=mergesort(a,mid,r)

        return(merge(left,right)
