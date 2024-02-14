class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val diffs = mutableMapOf<Int, Int>()
        for (i in 0..<nums.size) {
            val targetDiff = target - nums[i];
            if (diffs.containsKey(targetDiff)) {
                return intArrayOf(diffs[targetDiff]!!, i)
            }
            diffs[nums[i]] = i;
        }
        return intArrayOf();
    }
}