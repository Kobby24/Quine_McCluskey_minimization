def value(num, bits):
    return f"{num:0{bits}b}"


def cluster_minterms_by_ones(minterms, bits):
    cluster = {}
    for minterm in minterms:
        bin = value(minterm, bits)
        ones_total = bin.count('1')
        cluster.setdefault(ones_total, []).append(bin)
    return cluster


def add_terms(term1, term2):
    diff = 0
    result = []
    for bit1, bit2 in zip(term1, term2):
        if bit1 != bit2:
            diff += 1
            result.append('-')
        else:
            result.append(bit1)
        if diff > 1:
            return None
    return ''.join(result)


def identify_prime_implicants(minterms, bits):
    current_cluster = cluster_minterms_by_ones(minterms, bits)
    prime_implicants = set()

    while current_cluster:
        next_groups = {}
        used = set()

        cluster_keys = sorted(current_cluster.keys())
        for i in range(len(cluster_keys) - 1):
            cluster1 = current_cluster[cluster_keys[i]]
            cluster2 = current_cluster[cluster_keys[i + 1]]

            for term1 in cluster1:
                for term2 in cluster2:
                    add = add_terms(term1, term2)
                    if add:
                        used.add(term1)
                        used.add(term2)
                        next_groups.setdefault(add.count('1'), []).append(add)

        for cluster in current_cluster.values():
            for term in cluster:
                if term not in used:
                    prime_implicants.add(term)

        current_cluster = next_groups

    return prime_implicants


def is_covered(prime, minterm):
    return all(p == '-' or p == m for p, m in zip(prime, minterm))


def identify_essential_implicants(prime_implicants, minterms, bits):
    covered = {minterm: [] for minterm in minterms}

    for prime in prime_implicants:
        for minterm in minterms:
            if is_covered(prime, value(minterm, bits)):
                covered[minterm].append(prime)

    essential = set()
    for minterm, primes in covered.items():
        if len(primes) == 1:
            essential.add(primes[0])

    return essential


def convert_to_sop(implicants):
    terms = []
    for implicant in implicants:
        term = []
        for i, bit in enumerate(implicant):
            if bit == '1':
                term.append(chr(65 + i))
            elif bit == '0':
                term.append(f"{chr(65 + i)}'")

        terms.append(''.join(term))
    return ' + '.join(terms)


def quine_mccluskey(minterms, dont_cares, bits):
    all_terms = sorted(set(minterms + dont_cares))
    prime_implicants = identify_prime_implicants(all_terms, bits)
    essential_implicants = identify_essential_implicants(prime_implicants, minterms, bits)
    return convert_to_sop(essential_implicants)


# Test Case
if __name__ == "__main__":
    variables = 4
    minterms = [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]
    dont_cares = [4, 15]

    print(f"Original Function: F(A, B, C, D) = Σm({', '.join(map(str, minterms))})")
    print(f"Dont_care terms: D = {dont_cares}")

    result = quine_mccluskey(minterms, dont_cares, variables)
    print("Minimized SOP Form:", result)