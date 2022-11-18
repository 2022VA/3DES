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
    #text = "0123456789ABCDEF"
    #key1 = "133457799BBCDFF1"
    #text = "675A69675E5A6B5A"
    #key1 = "5B5A57676A56676E"
    textb = np.asarray(list(map(int, format(int(text,16), '0>64b'))))
    key1b = np.asarray(list(map(int, format(int(key1,16), '0>64b'))))
    #key2b = bin(int(key2,16))
    #key3b = bin(int(key3,16))
    #print (key1b)
    # Izsaucam DES algoritmu ar katru no atslēgām un iepriekšējo vai sākotnējo ievadu
    res1b = des(textb, key1b)
    tconv = str(res1b).replace('[', '')
    tconv = tconv.replace(']', '')
    tconv = tconv.replace(' ', '')
    tconv = tconv.replace('\n', '')
    res1 = str(hex(int(tconv, 2))[2:])
    #print (int(res1b,2))
    #res2 = des(res1, key2)
    #res3 = des(res2, key3)
    
    return render(request, 'result.html', {"textb": textb, "keyb": key1b, "text": text, "key": key1, "resultb": res1b, "result": res1})

def decrypt(request):
    crtext = request.POST['crtext']
    key1 = request.POST['key1']
    key2 = request.POST['key2']
    key3 = request.POST['key3']
    # TODO šeit jāraksta kods
    res = "Here is the decrypted block, with crypted text:" + crtext + " and key1:" + key1 + " and key2:" + key2+ " and key3:" + key3
    return render(request, 'result.html', {"result": res})

# --------------------------- computations
key_PC1 =  [57, 49, 41, 33, 25, 17,  9,
             1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27,
            19, 11,  3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29,
            21, 13,  5, 28, 20, 12,  4]


key_PC2 =  [14, 17, 11, 24,  1,  5,
             3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8,
            16,  7, 27, 20, 13,  2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

key_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

EBit = [32,  1,  2,  3,  4,  5,
         4,  5,  6,  7,  8,  9,
         8,  9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32,  1]

RP =   [16,  7, 20, 21, 
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6, 
        22, 11,  4, 25]

SBox =[ 
		#1
		[[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
		 [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8], 
		 [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
		 [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]],

		#2
		[[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
		 [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
		 [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
		 [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]],

		#3
		[[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
		 [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
		 [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
		 [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],

		#4
		[[ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
		 [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
		 [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
		 [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]],

		#5
		[[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
		 [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
		 [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
		 [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]],

		#6
		[[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
		 [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
		 [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
		 [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],

		#7
		[[ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
		 [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
		 [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
		 [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]],

		#8
		[[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
		 [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
		 [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
		 [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]
	]

IPm1 = [40,  8, 48, 16, 56, 24, 64, 32,
        39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25]

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
    #print ("keys:")
    #print (keys)
    #print ("----------------")
    data = initial_perm(text) # initial permutation

    for i in range(16):
        #print ("Round: ", i+1)
        data_new = round(data, keys[i])
        data = data_new
        #print (i)
        #print (data)
    data = np.roll(data_new, 32)
    after_final_perm = final_perm(data)
    #print (after_final_perm)
    return after_final_perm

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

def initial_perm(text):
    in_perm = np.zeros(64, dtype=int)
    index = 0
    for x in IP:
        in_perm[index] = text[x-1]
        index += 1
    return in_perm

def final_perm(text):
    fi_perm = np.zeros(64, dtype=int)
    index = 0
    for x in IPm1:
        fi_perm[index] = text[x-1]
        index += 1
    return fi_perm

def xor(a, b):
    #print (a)
    #print (b)
    xor_res = np.logical_xor(a, b).astype(int)
    #print (xor_res)
    return xor_res

def ebit(r):
    #print(r)
    expanded = np.zeros(48, dtype=int)
    index = 0
    for x in EBit:
        expanded[index] = r[x-1]
        index += 1
    #print (expanded)
    return expanded

def sbox_parse(data, table):
    #print ("Pd:", data)
    #print ("Pt:", table)
    row = data[0]*2+data[5]
    #print ("Pr:", row)
    column = data[1]*8+data[2]*4+data[3]*2+data[4]
    #print ("Pc:", column)
    out = SBox[table][row][column]
    #print ("Po:", out)
    outb = np.asarray(list(map(int, format(out, '0>4b'))))
    return outb

def sbox(data):
    sbox_matrix = np.reshape(data, (-1, 6))
    sbox_out = np.zeros((8, 4), dtype=int)
    for i in range(8):
        sbox_out[i] = sbox_parse(sbox_matrix[i], i)
    return sbox_out.flatten()

def round_perm(data):
    res = np.zeros(32, dtype=int)
    index = 0
    for x in RP:
        res[index] = data[x-1]
        index += 1
    return res

def rfunction(r0, key):
    # E-bit
    eb = ebit(r0)
    # Eout xor key
    postxor = xor(eb, key)
    postsbox = sbox(postxor)
    rfunc_out = round_perm(postsbox)
    #print("EB   : ", eb)
    #print("KEY  : ", key)
    #print("PXOR : ", postxor)
    #print("PSBOX: ", postsbox)
    #print("OUT   : ", rfunc_out)
    # Sbin
    # Round Permutation
    return rfunc_out

def round(data, key):
    l0 = data[0:32]
    r0 = data[32:64]
    #print ("L0: ", l0)
    #print ("R0: ", r0)
    #print ("Ky: ", key)
    l1 = r0
    fresult = rfunction(r0, key)
    #print ("Fres: ", fresult)
    r1 = xor(l0, fresult)
    #print ("L1: ", l1)
    #print ("R1: ", r1)
    rres = np.zeros(64, dtype=int)
    rres[0:32] = l1
    rres[32:64] = r1

    return rres