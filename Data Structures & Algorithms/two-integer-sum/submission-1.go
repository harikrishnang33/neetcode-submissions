func twoSum(nums []int, target int) []int {
    indexMap := make(map[int]int)
    for i, num := range nums {
        indexMap[num] = i
    }
    for i, num := range nums {
        j, ok := indexMap[target - num]
        if i != j && ok {
            return []int{i, j}
        }
    }
    return []int{}
}
