func groupAnagrams(strs []string) [][]string {
    anagramHash := make(map[[26]byte][]string)

    for _, str := range strs {
        var keySlice [26]byte
        for _, ch := range str {
            index := ch - 97
            keySlice[index]++
        }
        anagramHash[keySlice] = append(anagramHash[keySlice], str)
    }
    out := make([][]string, 0)
    for _, value := range anagramHash {
        out = append(out, value)
    }
    return out
}