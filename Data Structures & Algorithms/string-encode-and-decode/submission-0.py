class Solution:

    def encode(self, strs: List[str]) -> str:
        stringa = ""
        for parola in strs:
            stringa += str(len(parola)) + "#" + parola
        return stringa

    def decode(self, s: str) -> List[str]:
        lista = []
        i = 0
        while i<len(s):
            indice_cancelletto = s.find("#", i)
            lunghezza = int(s[i:indice_cancelletto])
            inizio_parola = indice_cancelletto + 1
            fine_parola = inizio_parola + lunghezza
            parola = s[inizio_parola:fine_parola]
            lista.append(parola)
            i=fine_parola
        
        return lista
