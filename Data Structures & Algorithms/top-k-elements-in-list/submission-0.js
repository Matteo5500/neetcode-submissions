class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let result = {}
        for(let num of nums){
            if(!result[num]){
                result[num] = 0
            }
            result[num] +=1
        }
        let coppie = Object.entries(result).sort((a,b)=>b[1]-a[1])
        return coppie.slice(0,k).map(coppia => Number(coppia[0]))
    }
}
