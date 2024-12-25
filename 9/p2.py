def get_disk_list(diskmap):
    if len(diskmap) % 2 == 1:
        diskmap += "0"
    disk_list = []
    id = 0
    for i in range(1, len(diskmap), 2):
        block_space = int(diskmap[i-1])
        free_space = int(diskmap[i])
        disk_list.extend([id] * block_space)
        disk_list.extend(["."] * free_space)
        id += 1
    
    return disk_list

def compress_disk_list(disk_list):
    left = 0
    right = len(disk_list) - 1

    while left < right:
        while left < right and disk_list[right] == ".":
            right -= 1
        f_end = f_start = right
        while disk_list[f_start] == disk_list[f_end]:
            f_start -= 1
        f_start += 1
        f_size = f_end - f_start + 1

        while left < right and disk_list[left] != ".":
                left += 1
        s_start = s_end = left

        # fix
        while s_end < f_start and s_end - s_start + 1 < f_size:
            while s_end < f_start and disk_list[s_end] != ".":
                s_end += 1
                s_start = s_end
            
            while s_end < f_start and disk_list[] == ".":
                left += 1
                s_end = left 

        if left >= right or s_end - s_start <= f_size:
            continue

        for i in range(f_size):
            disk_list[f_start+i], disk_list[s_start+i] = disk_list[s_start+i], disk_list[f_start+i]

        left += 1
        right -= 1
    print(left, right)

    return disk_list  

if __name__ == "__main__":
    lines = open("9/i0").read().splitlines()
    disk_list = get_disk_list(lines[0])
    res_disk_list = compress_disk_list(disk_list)
    print(disk_list)
    res = 0
    for i, id in enumerate(res_disk_list):
        if id == ".":
            break
        res += i * id
    print(res)
