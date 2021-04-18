func findContentChildren(g []int, s []int) int {
	if len(g) ==0 || len(s) ==0{
		return 0
	}
	sort.Ints(g)
	sort.Ints(s)
	count := 0
	s_pointer, g_pointer := len(s) - 1, len(g) - 1
	for s_pointer >= 0 && g_pointer >= 0 {
		if g[g_pointer] <= s[s_pointer]{
			count++
			s_pointer--
		}
		g_pointer--
	}
	return count

}