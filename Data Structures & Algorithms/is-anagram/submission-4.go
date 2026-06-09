func isAnagram(s string, t string) bool {
    sHash := make(map[rune]int)
    tHash := make(map[rune]int)

    for _, str := range s {
        sHash[str]++
    }
    for _, str := range t {
        tHash[str]++
    }

    for key, _ := range sHash {
        if sHash[key] != tHash[key] {
            return false
        }
    }
    for key, _ := range tHash {
        if tHash[key] != sHash[key] {
            return false
        }
    }
    return true
}
