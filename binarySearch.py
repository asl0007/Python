def binarySearch(seq,v,l,r):
    #Search for 'v' in seq[l:r], sequence is sorted
    if (r-l==0):
        return(False)
    mid = (l+r)//2
    if (v==seq[mid]):
        return(True)
    if (v<seq[mid]):
        return(binarySearch(seq,v,l,mid))
    else:
        return(binarySearch(seq,v,mid+1,r))

