class Quine_McCluskey:
    def __init__(self):
        self.bin_terms = []


    def Terms(self, min_terms: list, d_c: list,v_num):
        for term in min_terms:
            bin_term = (bin(term)).split('b')[1]
            if len(bin_term) <4:
                add_ = 4-len(bin_term)
                bin_term = ("0"*add_) + bin_term
            self.bin_terms.append(bin_term)
        return self.bin_terms



MQ = Quine_McCluskey()
print(MQ.Terms([0, 2, 3, 5], [9, 4],4))

