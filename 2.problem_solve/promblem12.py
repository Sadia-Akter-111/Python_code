def merge_array(a, b):
    n = len(a)
    m = len(b)

    i = 0
    j = 0
    merge = []

    while i < n and j < m:
        if a[i] < b[j]:
            if len(merge) == 0 or merge[-1] != a[i]:
                merge.append(a[i])
            i += 1

        elif a[i] > b[j]:
            if len(merge) == 0 or merge[-1] != b[j]:
                merge.append(b[j])
            j += 1

        else:
            if len(merge) == 0 or merge[-1] != a[i]:
                merge.append(a[i])
            i += 1
            j += 1

    while i < n:
        if len(merge) == 0 or merge[-1] != a[i]:
            merge.append(a[i])
        i += 1

    while j < m:
        if len(merge) == 0 or merge[-1] != b[j]:
            merge.append(b[j])
        j += 1

    return merge


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

print(merge_array(a, b))