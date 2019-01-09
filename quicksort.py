def Quicksort(a,l,r):#sort a[l:r]
    if r-l <= 1:#base case
        return()
    #partition with respect to pivot, a[l]
    yellow = l+1
    for green in range(l+1,r):
        if a[green] <= a[l]:
            (a[yellow],a[green]) = (a[green],a[yellow])
            yellow = yellow+1
    #move pivot in place
    (a[l],a[yellow-1]) = (a[yellow-1],a[l])
    Quicksort(a,l,yellow-1)
    Quicksort(a,yellow,r)
