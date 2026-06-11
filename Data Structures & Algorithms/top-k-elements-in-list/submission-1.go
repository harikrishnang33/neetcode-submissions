func topKFrequent(nums []int, k int) []int {
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }
    freq := make([][]int, len(nums)+1)
    for num, cnt := range count {
        freq[cnt] = append(freq[cnt], num)
    }

    out := make([]int, 0)
    for i := len(freq)-1 ; i > 0; i-- {
        for _, num := range freq[i] {
            out = append(out, num)
            if len(out) == k {
                return out
            }
        }
    }
    return []int{}
}
