class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prezzo_minimo = prices[0]
        profitto_max = 0
        for prezzo in prices:
            if prezzo < prezzo_minimo:
                prezzo_minimo = prezzo
            elif prezzo - prezzo_minimo > profitto_max:
                profitto_max = prezzo - prezzo_minimo
            
        return profitto_max