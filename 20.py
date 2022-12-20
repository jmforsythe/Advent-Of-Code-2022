def get_new_location(n, cur, val):
    x = cur + val
    if val == 0:
        return x
    if 0<x<n-1:
        return x
    if val > 0:
        return x % (n-1) - 1
    elif val < 0:
        return (x-1) % (n-1) + 1

def main():
    nums = [int(line) for line in open("20.dat").read().splitlines()]
    n = len(nums)
    ptrs = [i for i in range(n)]
    for i in range(n):
        ptr_loc = ptrs.index(i)
        val = nums[i]
        new_loc = get_new_location(len(ptrs), ptr_loc, val)
        ptrs.insert(new_loc+1, i)
        if new_loc > ptr_loc:
            assert(ptrs[ptr_loc] == i)
            ptrs.pop(ptr_loc)
        else:
            assert(ptrs[ptr_loc+1] == i)
            ptrs.pop(ptr_loc+1)
    modified = [nums[i] for i in ptrs]
    x = modified.index(0)
    print(sum(modified[(x+i)%n] for i in (1000,2000,3000)))

    nums2 = [i*811589153 for i in nums]
    ptrs2 = [i for i in range(n)]
    for j in range(10):
        for i in range(n):
            ptr_loc = ptrs2.index(i)
            val = nums2[i]
            new_loc = get_new_location(len(ptrs2), ptr_loc, val%(n-1))
            ptrs2.insert(new_loc+1, i)
            if new_loc > ptr_loc:
                assert(ptrs2[ptr_loc] == i)
                ptrs2.pop(ptr_loc)
            else:
                assert(ptrs2[ptr_loc+1] == i)
                ptrs2.pop(ptr_loc+1)
    modified2 = [nums2[i] for i in ptrs2]
    x = modified2.index(0)
    print(sum(modified2[(x+i)%n] for i in (1000,2000,3000)))


if __name__ == "__main__":
    main()
