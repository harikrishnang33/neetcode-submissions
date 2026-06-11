func groupAnagrams(strs []string) [][]string {
    anagramHash := make(map[string][]string)

    for _, str := range strs {
        keySlice := make([]byte, 26)
        for _, ch := range str {
            index := int(ch) - 97
            keySlice[index]++
        }
        anagramHash[string(keySlice)] = append(anagramHash[string(keySlice)], str)
    }
    out := make([][]string, 0)
    for _, value := range anagramHash {
        out = append(out, value)
    }
    return out
}