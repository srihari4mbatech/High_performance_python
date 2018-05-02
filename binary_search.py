def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin >= imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < midpoint:
            imin = midpoint + 1
        else:
            return midpoint


if __name__ == "__main__":
    ls = list(range(10000))
    ls.sort()
    srt_val = 79
    tk = binary_search(srt_val, ls)
    print("The sorted list index for {} is {}".format(srt_val, tk))
