# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# This software is licensed under the MIT License.
# See the LICENSE file for more information.

'''
Contains monomer definitions
'''

# monomer: mass pairs
ONE_LETTER_CODE_MASS_PAIRS = {
    'A': 101.04768,  # A = Ala
    'a': 103.06023,  # a = d2Ala
    'B': 115.06333,  # B = Abu = Aminobutyric acid (Et side chain)
    'b': 117.07588,  # b = d2Abu
    'V': 129.07898,  # V = Val
    'v': 131.09153,  # v = d2Val
    'S': 131.05824,  # S = Ser (OMe)
    's': 133.07080,  # s = d2Ser (OMe)
    'L': 143.09463,  # L = Leu
    'l': 145.10718,  # l = d2Leu
    'D': 145.03751,  # D = Asp (unprotected COOH)
    'K': 158.10553,  # K = Lys
    'E': 159.05316,  # E = Glu (unprotected COOH)
    'P': 177.07898,  # P = Phe
    'p': 179.09153,  # p = d2Phe
    'C': 183.12593,  # C = Cha
    'c': 185.13848,  # c = d2Cha
    'H': 191.09463,  # H = HoPhe = Homophenylalaninol
    'h': 193.10718,  # h = d2HoPhe
    'Y': 193.07389,  # Y = Tyr (unprotected Phenol)
    'y': 195.08645,  # y = d2Tyr (unprotected Phenol)
}

THREE_LETTER_CODES = {
    'Ala': 'A',
    'd2Ala': 'a',
    'Abu': 'B',
    'd2Abu': 'b',
    'Val': 'V',
    'd2Val': 'v',
    'Ser': 'S',
    'd2Ser': 's',
    'Leu': 'L',
    'd2Leu': 'l',
    'Asp': 'D',
    'Lys': 'K',
    'Glu': 'E',
    'Phe': 'P',
    'd2Phe': 'p',
    'Cha': 'C',
    'd2Cha': 'c',
    'HoPhe': 'H',
    'd2HoPhe': 'h',
    'Tyr': 'Y',
    'd2Tyr': 'y'
}
