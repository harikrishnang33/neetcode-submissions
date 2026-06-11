func topKFrequent(nums []int, k int) []int {
    frequentHash := make(map[int]int)
    for _, num := range nums {
        frequentHash[num]++
    }
    type Pair struct {
        Key int
        Value int
    }
    var pairs []Pair
    for k, v := range frequentHash {
        pairs = append(pairs, Pair{k,v})
    }
    sort.Slice(pairs, func (i, j int) bool {
        return pairs[i].Value > pairs[j].Value
    })
    out := make([]int, 0)
    for _, pair := range pairs {
        out = append(out, pair.Key)
        k--
        if k == 0 {
            return out
        }
    }
    return []int{}
}
