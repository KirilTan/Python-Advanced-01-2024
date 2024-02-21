def recursive_sum(nums_list: list, idx=0) -> int:
    if idx == len(nums_list) - 1:
        return nums_list[idx]
    return nums_list[idx] + recursive_sum(nums_list, idx + 1)


nums = [int(x) for x in input().split()]
print(recursive_sum(nums))
