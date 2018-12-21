a=[5,4,3,2,1]

def partion(a,low,high):
    i=low-1
    pi=a[high]
    for j in range(low,high):
        if a[j]<=pi:
            i=i+1
            a[i],a[j]=a[j],a[i]

    a[i+1],a[high]=a[high],a[i+1]
    return i+1


def quick_sort(a,low,high):
    if low<high:
        pi=partion(a,low,high)

        quick_sort(a,low,pi-1)
        quick_sort(a,pi+1,high)



quick_sort(a,0,len(a)-1)
print(a)





