def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 == 1:
            return x

def find_it2(seq):
    return [x for x in seq if seq.count(x) % 2 == 1][0]

def main(): # Defining main function
    arr = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    dup = find_it(arr)
    print (dup)
    dup2 = find_it2(arr)
    print (dup2)

if __name__=="__main__":
    main()
