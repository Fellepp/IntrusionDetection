"""
Dij = Partial edit distance matrix
VPj = Vertical positive delta vector: VPj[i]= 1 iff D[i, j] = D[i-1, j] = 1
VNj = Vertical negative delta  vector: VNj[i]= 1 iff D[i, j] = D[i-1, j] = -1
HPj = Horizontal positive delta vector: HPj[i]= 1 iff D[i, j] = D[i, j-1] = 1
HNj = Horizontal negative delta vector: HNj[i]= 1 iff D[i, j] = D[i, j-1] = -1
D0j = Diagonal zero delta vector: VPj[i]= 1 iff D[i, j] = D[i-1, j] = 1
PM = Pattern match vector: For every character in alfabet, PM[i] = 1 iff Pat[i] = char
"""


def HeikkiMyers(x, y, k):
    # Preprocess

    m = len(x) + 1
    n = len(y) + 1

    # Init all vectors
    VP = [0] * n
    VP[0] = int("1" * len(x), 2)
    VN = [0] * n
    HP = [0] * n
    HN = [0] * n
    D0 = [0] * n
    PM = {}
    D_MJ = len(x)

    # Find the alfabet in x+y
    for character in str(x + y):
        PM[character] = 0
    # Find the match for PM on x
    for iteration, character in enumerate(x):
        zerosBefore = (m - iteration) * "0"
        zerosAfter = iteration * "0"
        PM[character] = PM[character] | int(zerosBefore + "1" + zerosAfter, 2)

    # Search
    for j, character in enumerate(y):
        j += 1
        # 1. D0_j computed from PM_j, VP_j-1 and VN_j-1
        D0[j] = (((PM[character] & VP[j - 1]) + VP[j - 1]) ^ VP[j - 1]) | PM[character] | VN[j - 1]

        # 2. HP_j and HN_j computed from D0_j, VP_j-1 and VN_j-1
        HP[j] = VN[j - 1] | ((D0[j] | VP[j - 1]) ^ int("1" * m, 2))
        HN[j] = D0[j] & VP[j - 1]

        # 3. D_MJ computed from D_M[j-1] and HP_j[m], HN_j[m]
        if HP[j] & int("1" + "0" * (len(x) - 1), 2):
            D_MJ += 1
        if HN[j] & int("1" + "0" * (len(x) - 1), 2):
            D_MJ -= 1

        # Ends at text position j when D_M[j] <= k
        if D_MJ <= k:
            return j

        # 4. VP_j and VN_j computed from D0_j, HP_j and HN_j
        VP[j] = (HN[j] << 1) | ((D0[j] | (HP[j] << 1)) ^ int("1" * m, 2))
        VN[j] = D0[j] & (HP[j] << 1)
    return 0


pat = "annual"
text = "annealing"
k = 2

match = HeikkiMyers(pat, text, k)
print(match)
