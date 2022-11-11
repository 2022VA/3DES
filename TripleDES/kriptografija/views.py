from django.shortcuts import render
import numpy as np

# Create your views here.
def index(request):
    return render(request, 'index.html')

def encrypt(request):
    text = request.POST['text']
    key1 = request.POST['key1']
    key2 = request.POST['key2']
    key3 = request.POST['key3']
    # TODO šeit jāraksta kods
    # Repeat with Keys 1,2,3:
    #  Create key 1-16 schedule & print
    #  Initial permutation
    #  Perform rounds 1-16, where
    #   split data in half to leftN & rightN
    #   left dataN1 = right dataN
    #   right dataN1 = left tataN XOR function(right dataN, keyN)
    #   function = expand, xor, sbox, permutate
    #  Inverse initial permutation

    # Pārvēršam ievaddatus binārā formātā
    key1 = "133457799BBCDFF1"
    #textb = bin(int(text,16))
    key1b = np.asarray(list(map(int, format(int(key1,16), '0>64b'))))
    #key2b = bin(int(key2,16))
    #key3b = bin(int(key3,16))
    #print (key1b)
    # Izsaucam DES algoritmu ar katru no atslēgām un iepriekšējo vai sākotnējo ievadu
    res1 = des(text, key1b)
    #res2 = des(res1, key2)
    #res3 = des(res2, key3)
    
    res = "Here is the encrypted block, with inputs text:" + text + " and key1:" + key1 + " and key2:" + key2+ " and key3:" + key3
    return render(request, 'result.html', {"result": res})

def decrypt(request):
    crtext = request.POST['crtext']
    key1 = request.POST['key1']
    key2 = request.POST['key2']
    key3 = request.POST['key3']
    # TODO šeit jāraksta kods
    res = "Here is the decrypted block, with crypted text:" + crtext + " and key1:" + key1 + " and key2:" + key2+ " and key3:" + key3
    return render(request, 'result.html', {"result": res})

# --------------------------- computations
key_PC1 =  [57,    49,   41,    33,    25,   17,    9,
             1,    58,   50,    42,    34,   26,   18,
            10,     2,   59,    51,    43,   35,   27,
            19,    11,    3,    60,    52,   44,   36,
            63,    55,   47,    39,    31,   23,   15,
             7,    62,   54,    46,    38,   30,   22,
            14,     6,   61,    53,    45,   37,   29,
            21,    13,    5,    28,    20,   12,    4]


key_PC2 =  [14,    17,   11,    24,     1,    5,
             3,    28,   15,     6,    21,   10,
            23,    19,   12,     4,    26,    8,
            16,     7,   27,    20,    13,    2,
            41,    52,   31,    37,    47,   55,
            30,    40,   51,    45,    33,   48,
            44,    49,   39,    56,    34,   53,
            46,    42,   50,    36,    29,   32]

key_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def des(text, key):
    out = np.zeros(64, dtype=int)
    # create Key Permuted choice 1 using PC-1 and get from 64 bit key to 58 bits
    perm_key = permutate_key(key)
    # calculate c0 and d0
    c0 = perm_key[0:28]
    d0 = perm_key[28:56]
    cn = c0
    dn = d0
    joined = np.zeros(56, dtype=int)
    keys = np.zeros([16, 48], dtype=int)
    # calculate rest of the 48 bit subkeys
    keys_index = 0
    for i in range (1,17):
        cn = np.roll(cn,-key_shift[i-1])
        dn = np.roll(dn,-key_shift[i-1])
        keys[keys_index] = permuted_choice2(cn, dn)
        keys_index += 1
    # initial permutation
    # round 1-16:
    # split
    # e-bits & S-box
    # 
    return out

def permutate_key(key):
    pkey = np.zeros(64, dtype=int)
    index = 0
    for x in key_PC1:
        pkey[index] = key[x-1]
        index += 1
    return pkey[0:56]

def permuted_choice2(cn, dn):
    p2key = np.zeros(56, dtype=int)
    cd = np.concatenate((cn, dn))
    index = 0
    for x in key_PC2:
        p2key[index] = cd[x-1]
        index += 1
    return p2key[0:48]
