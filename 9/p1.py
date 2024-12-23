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
        while left < right and disk_list[left] != ".":
            left += 1
        while left < right and disk_list[right] == ".":
            right -= 1
        
        if left >= right:
            break

        disk_list[left], disk_list[right] = disk_list[right], disk_list[left]
        left += 1
        right -= 1

    return disk_list  

if __name__ == "__main__":
    lines = open("9/i1").read().splitlines()
    disk_list = get_disk_list(lines[0])
    res_disk_list = compress_disk_list(disk_list)
    res = 0
    for i, id in enumerate(res_disk_list):
        if id == ".":
            break
        res += i * id
    print(res)