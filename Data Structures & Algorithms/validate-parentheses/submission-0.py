
class Solution:
    def isValid(self, s: str) -> bool:
        pila = []  # La nostra lista di appoggio (lo Stack)
        mappa = {")": "(", "]": "[", "}": "{"}
        
        for carattere in s:

            if carattere in ['(', '[', '{']:
                pila.append(carattere) 
                
            else:
                if not pila :
                    return False
                
                ultimo_aperto = pila[-1]

                if ultimo_aperto == mappa[carattere]:
                    pila.pop()
                else:
                    return False

        return len(pila) == 0 
