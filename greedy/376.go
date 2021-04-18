func wiggleMaxLength(nums []int) int {
	var count int 
	number := len(nums)
	if number < 2 {
		return number
	}
	preDif := nums[1] - nums[0]
	if preDif == 0{
		count = 1
	} else {
		count = 2
	}
	for i:=2; i<number; i++{
		dif := nums[i] - nums[i-1]
		if (preDif >= 0 && dif < 0) || (preDif <= 0 && dif > 0){
			count++
			preDif = dif
		}
	}
	return count
}