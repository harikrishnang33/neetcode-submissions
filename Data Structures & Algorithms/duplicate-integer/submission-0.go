func hasDuplicate(nums []int) bool {
    numsMap := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        if numsMap[nums[i]] == 1 {
            return true;
        } else {
            numsMap[nums[i]] = 1;
        }
    }
    return false;
}
