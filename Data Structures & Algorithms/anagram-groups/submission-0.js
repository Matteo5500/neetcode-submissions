class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        if(strs.length < 1 || strs.length >10000){
            return "strs have to be between 1 and 10000"
        }
        for(let i=0; i<strs.length; i++){
            if(strs[i].length >100){
                return "Element can't be longer than 100 characters"
            }
        }
        let result = {}
        for(let i=0; i<strs.length;i++){
            let sortedElement = strs[i].split("").sort().join("")
            if(!result[sortedElement]){
                result[sortedElement] = []
            }
            result[sortedElement].push(strs[i])
        }
        return Object.values(result)
    }
}
