def spl(l):
    pivot = l[0]
    left = 0
    right = l.index(l[-1])
    
    while(left < right):
        while(l[right] > pivot):
            print("1", right)
            right = right - 1
        while(left < right and l[left] <= pivot):
            print("2", left)
            print("3", right)
            left = left + 1
        if(left < right):
            print("Do swap")
            print("Left:",left,"right:",right)
            tmp = l[right]
            l[right] = l[left]
            l[left] = tmp

    pos = right
    l[0] = l[pos]
    l[pos] = pivot
    print("Pivot",pivot)
    print("After",l)
    return l
    
l = [55,34,54,7,5,32,23,98,56,23,44]
print("Before",l)
for x in range(0,4):
    spl(l)


