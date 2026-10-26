class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
        let output = []
        let counter = 0
        let binario = ""
        for(let i=0; i<=n; i++){
            binario = i.toString(2)
            for(let j=0; j<=binario.length;j++){
                if(binario[j] == "1"){
                    counter += 1
                }
            }
            output.push(counter)
            counter = 0
        }
        return output
    }
}
