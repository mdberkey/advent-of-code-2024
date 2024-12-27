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
    
    return disk_list, id

def compress_disk_list(disk_list, num_files):

    def get_next_free_block(disk_list, i):
        free_start = free_end = i
        # move to start of free space
        while free_start < len(disk_list) and disk_list[free_start] != ".":
            free_start += 1
        free_end = free_start
        # get end of free space (exclusive)
        while free_end < len(disk_list) and disk_list[free_end] == ".":
            free_end += 1 
        return free_start, free_end

    def get_next_file_block(disk_list, i):
        block_start = block_end = i
        # move to end of block (exclusive)
        while block_end >= 0 and disk_list[block_end] == ".":
            block_end -= 1
        block_end += 1
        # get start of block
        block_start = block_end - 1
        while block_start >= 0 and disk_list[block_start] == disk_list[block_end-1]:
            block_start -= 1 
        block_start += 1
        return block_start, block_end

    # iterate through file blocks, on each, iterate open free space and attempt move.
    next_bval = len(disk_list) - 1
    seen_ids = set()
    for _ in range(num_files):
        block_start, block_end = get_next_file_block(disk_list, next_bval)
        next_bval = block_start - 1
        
        while next_bval >= 0 and disk_list[block_start] in seen_ids:
            block_start, block_end = get_next_file_block(disk_list, next_bval)
            next_bval = block_start - 1
        seen_ids.add(disk_list[block_start])
        block_size = block_end - block_start

        free_size = -1
        next_fval = 0
        while free_size < block_size and next_fval < len(disk_list) and next_fval < block_start:
            free_start, free_end = get_next_free_block(disk_list, next_fval)
            next_fval = free_end
            free_size = free_end - free_start
        
        # if no large enough free space, continue to other blocks        
        if free_size < block_size or free_start > block_end - 1:
            continue
            
        # swap free space with block
        for i in range(block_size):
             disk_list[free_start+i], disk_list[block_start+i] = disk_list[block_start+i], disk_list[free_start+i]
    return disk_list  

if __name__ == "__main__":
    lines = open("9/i1").read().splitlines()
    disk_list, num_files = get_disk_list(lines[0])
    res_disk_list = compress_disk_list(disk_list, num_files)
    res = 0
    for i, id in enumerate(res_disk_list):
        if id != ".":
            res += i * id
    print(res)
