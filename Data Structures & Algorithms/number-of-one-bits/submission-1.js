class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
        let counter = 0
        let binario = n.toString(2)
        for(let i=0;i<binario.length;i++){
            if(binario[i] == "1"){
                counter += 1
            }
        }
        return counter
    }
}
