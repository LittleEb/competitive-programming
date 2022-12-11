def countSwaps(a):
    # Write your code here
    swaps = 0
    if n > 1:
        for i in range (n):
            for j in range (0, n-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    swaps+=1
                    firstelement = a[0]
                    lastelement = a[-1]
                else:
                    firstelement = a[0]
                    lastelement = a[-1]

        print('Array is sorted in', swaps, 'swaps.')
        print ('First Element:', firstelement)
        print ('Last Element:', lastelement)
    else:
        print('Array is sorted in', swaps, 'swaps.')
        
        
   

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
