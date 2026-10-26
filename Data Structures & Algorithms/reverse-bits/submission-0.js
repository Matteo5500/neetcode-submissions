class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number} - a positive integer
     */
    reverseBits(n) {
        let binario = n.toString(2)
        let lunga = binario.padStart(32, "0")
        let reversed = lunga.split("").reverse().join("")
        let decim = parseInt(reversed, 2)
        return decim
}
}