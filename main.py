class Quine_McCluskey:
    def __init__(self):
        self.bin_terms = []

    def Terms(self, min_terms: list, d_c: list, v_num):
        for term in min_terms:
            bin_term = (bin(term)).split('b')[1]
            if len(bin_term) < 4:
                add_ = 4 - len(bin_term)
                bin_term = ("0" * add_) + bin_term
            self.bin_terms.append(bin_term)
        return self.bin_terms

    def Groups(self):
        terms = self.Terms([0, 1, 3, 7, 8, 9, 11, 15], [9, 4], 4)
        groups = {}
        for term in terms:
            try:
                G = groups[f'G{term.count("1")}']

            except KeyError:
                groups[f'G{term.count("1")}'] = [term]
            else:
                G.append(term)

        return groups

    def Comparing(self):
        groups = self.Groups()
        n = 1
        for group,term in groups.items():
            if n < len(groups):
                nxt_term = list(groups.keys())[n]
                n += 1
                print(term,groups[nxt_term])




MQ = Quine_McCluskey()
MQ.Comparing()
