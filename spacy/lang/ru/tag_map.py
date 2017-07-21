# coding: utf8
from __future__ import unicode_literals

from ..symbols import POS, ADV, NOUN, ADP, PRON, SCONJ, PROPN, DET, SYM, INTJ
from ..symbols import PUNCT, NUM, AUX, X, CONJ, ADJ, VERB, PART, SPACE, CCONJ


# Add a tag map
# Documentation: https://spacy.io/docs/usage/adding-languages#tag-map
# Universal Dependencies: http://universaldependencies.org/u/pos/all.html
# The keys of the tag map should be strings in your tag set. The dictionary must
# have an entry POS whose value is one of the Universal Dependencies tags.
# Optionally, you can also include morphological features or other attributes.


TAG_MAP = {
    "ADV":      {POS: ADV},
    
    "NNSNom":   {POS: NOUN, "Number" : "sing", "Case" : "nom"},
    "NNSAcc":   {POS: NOUN, "Number" : "sing", "Case" : "acc"},
    "NNSGen":   {POS: NOUN, "Number" : "sing", "Case" : "gen"},
    "NNSDat":   {POS: NOUN, "Number" : "sing", "Case" : "dat"},
    "NNSInstr": {POS: NOUN, "Number" : "sing", "Case" : "instr"},
    "NNSPrep":  {POS: NOUN, "Number" : "sing", "Case" : "prep"},
    "NNPNom":   {POS: NOUN, "Number" : "plur", "Case" : "nom"},
    "NNPAcc":   {POS: NOUN, "Number" : "plur", "Case" : "acc"},
    "NNPGen":   {POS: NOUN, "Number" : "plur", "Case" : "gen"},
    "NNPDat":   {POS: NOUN, "Number" : "plur", "Case" : "dat"},
    "NNPInstr": {POS: NOUN, "Number" : "plur", "Case" : "instr"},
    "NNPPrep":   {POS: NOUN, "Number" : "plur", "Case" : "prep"},
    "ADP":      {POS: ADP},
    
    "PRON": {POS : "PRON"},
    
    "PRONPrs1SgNom": {POS : "PRON", "Number": "sing", "Person" : "1", "Case" : "Nom", "PronType" : "Prs"},
    "PRONPrs1SgAcc": {POS : "PRON", "Number": "sing", "Person" : "1", "Case" : "Acc", "PronType" : "Prs"},
    "PRONPrs1SgGen": {POS : "PRON", "Number": "sing", "Person" : "1", "Case" : "Gen", "PronType" : "Prs"},
    "PRONPrs1SgDat": {POS : "PRON", "Number": "sing", "Person" : "1", "Case" : "Dat", "PronType" : "Prs"},
    "PRONPrs1SgInstr": {POS : "PRON", "Number": "sing", "Person" : "1", "Case" : "Instr", "PronType" : "Prs"},
    "PRONPrs1SgPrep": {POS : "PRON", "Number": "sing", "Person" : "1", "Case" : "Prep", "PronType" : "Prs"},
    
    "PRONPrs2SgNom": {POS : "PRON", "Number": "sing", "Person" : "2", "Case" : "Nom", "PronType" : "Prs"},
    "PRONPrs2SgAcc": {POS : "PRON", "Number": "sing", "Person" : "2", "Case" : "Acc", "PronType" : "Prs"},
    "PRONPrs2SgGen": {POS : "PRON", "Number": "sing", "Person" : "2", "Case" : "Gen", "PronType" : "Prs"},
    "PRONPrs2SgDat": {POS : "PRON", "Number": "sing", "Person" : "2", "Case" : "Dat", "PronType" : "Prs"},
    "PRONPrs2SgInstr": {POS : "PRON", "Number": "sing", "Person" : "2", "Case" : "Instr", "PronType" : "Prs"},
    "PRONPrs2SgPrep": {POS : "PRON", "Number": "sing", "Person" : "2", "Case" : "Prep", "PronType" : "Prs"},
    
    "PRONPrs3SgMNom": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Nom", "PronType" : "Prs", "gender" : "M"},
    "PRONPrs3SgMAcc": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Acc", "PronType" : "Prs", "gender" : "M"},
    "PRONPrs3SgMGen": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Gen", "PronType" : "Prs", "gender" : "M"},
    "PRONPrs3SgMDat": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Dat", "PronType" : "Prs", "gender" : "M"},
    "PRONPrs3SgMInstr": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Instr", "PronType" : "Prs", "gender" : "M"},
    "PRONPrs3SgMPrep": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Prep", "PronType" : "Prs", "gender" : "M"},
    
    "PRONPrs3SgFNom": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Nom", "PronType" : "Prs", "gender" : "F"},
    "PRONPrs3SgFAcc": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Acc", "PronType" : "Prs", "gender" : "F"},
    "PRONPrs3SgFGen": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Gen", "PronType" : "Prs", "gender" : "F"},
    "PRONPrs3SgFDat": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Dat", "PronType" : "Prs", "gender" : "F"},
    "PRONPrs3SgFInstr": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Instr", "PronType" : "Prs", "gender" : "F"},
    "PRONPrs3SgFPrep": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Prep", "PronType" : "Prs", "gender" : "F"},
   
    "PRONPrs3SgNNom": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Nom", "PronType" : "Prs", "gender" : "N"},
    "PRONPrs3SgNAcc": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Acc", "PronType" : "Prs", "gender" : "N"},
    "PRONPrs3SgNGen": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Gen", "PronType" : "Prs", "gender" : "N"},
    "PRONPrs3SgNDat": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Dat", "PronType" : "Prs", "gender" : "N"},
    "PRONPrs3SgNInstr": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Instr", "PronType" : "Prs", "gender" : "N"},
    "PRONPrs3SgNPrep": {POS : "PRON", "Number": "sing", "Person" : "3", "Case" : "Prep", "PronType" : "Prs", "gender" : "N"},
    
    "PRONPrs1PlNom": {POS : "PRON", "Number": "plur", "Person" : "1", "Case" : "Nom", "PronType" : "Prs"},
    "PRONPrs1PlAcc": {POS : "PRON", "Number": "plur", "Person" : "1", "Case" : "Acc", "PronType" : "Prs"},
    "PRONPrs1PlGen": {POS : "PRON", "Number": "plur", "Person" : "1", "Case" : "Gen", "PronType" : "Prs"},
    "PRONPrs1PlDat": {POS : "PRON", "Number": "plur", "Person" : "1", "Case" : "Dat", "PronType" : "Prs"},
    "PRONPrs1PlInstr": {POS : "PRON", "Number": "plur", "Person" : "1", "Case" : "Instr", "PronType" : "Prs"},
    "PRONPrs1PlPrep": {POS : "PRON", "Number": "plur", "Person" : "1", "Case" : "Prep", "PronType" : "Prs"},
    
    "PRONPrs2PlNom": {POS : "PRON", "Number": "plur", "Person" : "2", "Case" : "Nom", "PronType" : "Prs"},
    "PRONPrs2PlAcc": {POS : "PRON", "Number": "plur", "Person" : "2", "Case" : "Acc", "PronType" : "Prs"},
    "PRONPrs2PlGen": {POS : "PRON", "Number": "plur", "Person" : "2", "Case" : "Gen", "PronType" : "Prs"},
    "PRONPrs2PlDat": {POS : "PRON", "Number": "plur", "Person" : "2", "Case" : "Dat", "PronType" : "Prs"},
    "PRONPrs2PlInstr": {POS : "PRON", "Number": "plur", "Person" : "2", "Case" : "Instr", "PronType" : "Prs"},
    "PRONPrs2PlPrep": {POS : "PRON", "Number": "plur", "Person" : "2", "Case" : "Prep", "PronType" : "Prs"},
    
    "PRONPrs3PlNomSg": {POS : "PRON", "Number": "plur", "Person" : "3", "Case" : "Nom", "PronType" : "Prs"},
    "PRONPrs3PlAccSg": {POS : "PRON", "Number": "plur", "Person" : "3", "Case" : "Acc", "PronType" : "Prs"},
    "PRONPrs3PlGen": {POS : "PRON", "Number": "plur", "Person" : "3", "Case" : "Gen", "PronType" : "Prs"},
    "PRONPrs3PlDat": {POS : "PRON", "Number": "plur", "Person" : "3", "Case" : "Dat", "PronType" : "Prs"},
    "PRONPrs3PlInstr": {POS : "PRON", "Number": "plur", "Person" : "3", "Case" : "Instr", "PronType" : "Prs"},
    "PRONPrs3PlPrep": {POS : "PRON", "Number": "plur", "Person" : "3", "Case" : "Prep", "PronType" : "Prs"},
    
    "PRONPoss1SgMNomSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1SgMAccSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1SgMGenSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1SgMDatSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1SgMInstrSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1SgMPrepSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    
    "PRONPoss1SgFNomSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1SgFAccSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1SgFGenSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1SgFDatSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1SgFInstrSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1SgFPrepSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    
    "PRONPoss1SgNNomSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1SgNAccSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1SgNGenSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1SgNDatSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1SgNInstrSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1SgNPrepSg": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},

    "PRONPoss1SgNomPl": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1SgAccPl": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1SgGenPl": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1SgDatPl": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1SgInstrPl": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1SgPrepPl": {POS : "PRON", "PossNumber": "sing", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Number" : "plur"},

    "PRONPoss2SgMNomSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2SgMAccSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2SgMGenSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2SgMDatSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2SgMInstrSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2SgMPrepSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    
    "PRONPoss2SgFNomSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2SgFAccSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2SgFGenSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2SgFDatSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2SgFInstrSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2SgFPrepSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    
    "PRONPoss2SgNNomSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2SgNAccSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2SgNGenSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2SgNDatSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2SgNInstrSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2SgNPrepSg": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},

    "PRONPoss2SgNomPl": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2SgAccPl": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2SgGenPl": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2SgDatPl": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2SgInstrPl": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2SgPrepPl": {POS : "PRON", "PossNumber": "sing", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Number" : "plur"},
    
    "PRONPoss3Sg": {POS : "PRON", "PossNumber": "sing", "Person" : "3", "PronType" : "Poss"},
    
    "PRONPoss1PlMNomSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1PlMAccSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1PlMGenSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1PlMDatSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1PlMInstrSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss1PlMPrepSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    
    "PRONPoss1PlFNomSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1PlFAccSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1PlFGenSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1PlFDatSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1PlFInstrSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss1PlFPrepSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    
    "PRONPoss1PlNNomSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1PlNAccSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1PlNGenSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1PlNDatSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1PlNInstrSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss1PlNPrepSg": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},

    "PRONPoss1PlNomPl": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Nom", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1PlAccPl": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Acc", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1PlGenPl": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Gen", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1PlDatPl": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Dat", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1PlInstrPl": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Instr", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss1PlPrepPl": {POS : "PRON", "PossNumber": "plur", "Person" : "1", "Case" : "Prep", "PronType" : "Poss", "Number" : "plur"},

    "PRONPoss2PlMNomSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2PlMAccSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2PlMGenSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2PlMDatSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2PlMInstrSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    "PRONPoss2PlMPrepSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Gender" : "M", "Number" : "sing"},
    
    "PRONPoss2PlFNomSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2PlFAccSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2PlFGenSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2PlFDatSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2PlFInstrSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
    "PRONPoss2PlFPrepSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Gender" : "F", "Number" : "sing"},
   
    "PRONPoss2PlNNomSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2PlNAccSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2PlNGenSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2PlNDatSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2PlNInstrSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},
    "PRONPoss2PlNPrepSg": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Gender" : "N", "Number" : "sing"},

    "PRONPoss2PlNomPl": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Nom", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2PlAccPl": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Acc", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2PlGenPl": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Gen", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2PlDatPl": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Dat", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2PlInstrPl": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Instr", "PronType" : "Poss", "Number" : "plur"},
    "PRONPoss2PlPrepPl": {POS : "PRON", "PossNumber": "plur", "Person" : "2", "Case" : "Prep", "PronType" : "Poss", "Number" : "plur"},

    "PRONPoss3Pl": {POS : "PRON", "PossNumber": "plur", "Person" : "3", "PronType" : "Poss"},
    
    "PRONIndMNomSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "M", "Case" : "Nom"}
    "PRONIndMAccSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "M", "Case" : "Acc"}
    "PRONIndMGenSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "M", "Case" : "Gen"}
    "PRONIndMDatSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "M", "Case" : "Dat"}
    "PRONIndMInstrSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "M", "Case" : "Instr"}
    "PRONIndMPrepSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "M", "Case" : "Prep"}
    
    "PRONIndFNomSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "F", "Case" : "Nom"}
    "PRONIndFAccSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "F", "Case" : "Acc"}
    "PRONIndFGenSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "F", "Case" : "Gen"}
    "PRONIndFDatSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "F", "Case" : "Dat"}
    "PRONIndFInstrSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "F", "Case" : "Instr"}
    "PRONIndFPrepSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "F", "Case" : "Prep"}    

    "PRONIndNNomSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "N", "Case" : "Nom"}
    "PRONIndNAccSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "N", "Case" : "Acc"}
    "PRONIndNGenSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "N", "Case" : "Gen"}
    "PRONIndNDatSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "N", "Case" : "Dat"}
    "PRONIndNInstrSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "N", "Case" : "Instr"}
    "PRONIndNPrepSg": {POS : "PRON", "PronType" : "Ind", "Number" : "sing", "Gender" : "N", "Case" : "Prep"}  
    
    "PRONIndNomPl": {POS : "PRON", "PronType" : "Ind", "Number" : "plur", "Case" : "Nom"}
    "PRONIndAccPl": {POS : "PRON", "PronType" : "Ind", "Number" : "plur", "Case" : "Acc"}
    "PRONIndGenPl": {POS : "PRON", "PronType" : "Ind", "Number" : "plur", "Case" : "Gen"}
    "PRONIndDatPl": {POS : "PRON", "PronType" : "Ind", "Number" : "plur", "Case" : "Dat"}
    "PRONIndInstrPl": {POS : "PRON", "PronType" : "Ind", "Number" : "plur", "Case" : "Instr"}
    "PRONIndPrepPl": {POS : "PRON", "PronType" : "Ind", "Number" : "plur", "Case" : "Prep"}
    
    "PRONRelMNomSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "M", "Case" : "Nom"}
    "PRONRelMAccSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "M", "Case" : "Acc"}
    "PRONRelMGenSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "M", "Case" : "Gen"}
    "PRONRelMDatSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "M", "Case" : "Dat"}
    "PRONRelMInstrSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "M", "Case" : "Instr"}
    "PRONRelMPrepSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "M", "Case" : "Prep"}
    
    "PRONRelFNomSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "F", "Case" : "Nom"}
    "PRONRelFAccSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "F", "Case" : "Acc"}
    "PRONRelFGenSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "F", "Case" : "Gen"}
    "PRONRelFDatSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "F", "Case" : "Dat"}
    "PRONRelFInstrSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "F", "Case" : "Instr"}
    "PRONRelFPrepSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "F", "Case" : "Prep"}    

    "PRONRelNNomSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "N", "Case" : "Nom"}
    "PRONRelNAccSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "N", "Case" : "Acc"}
    "PRONRelNGenSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "N", "Case" : "Gen"}
    "PRONRelNDatSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "N", "Case" : "Dat"}
    "PRONRelNInstrSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "N", "Case" : "Instr"}
    "PRONRelNPrepSg": {POS : "PRON", "PronType" : "Rel", "Number" : "sing", "Gender" : "N", "Case" : "Prep"}  
    
    "PRONRelNomPl": {POS : "PRON", "PronType" : "Rel", "Number" : "plur", "Case" : "Nom"}
    "PRONRelAccPl": {POS : "PRON", "PronType" : "Rel", "Number" : "plur", "Case" : "Acc"}
    "PRONRelGenPl": {POS : "PRON", "PronType" : "Rel", "Number" : "plur", "Case" : "Gen"}
    "PRONRelDatPl": {POS : "PRON", "PronType" : "Rel", "Number" : "plur", "Case" : "Dat"}
    "PRONRelInstrPl": {POS : "PRON", "PronType" : "Rel", "Number" : "plur", "Case" : "Instr"}
    "PRONRelPrepPl": {POS : "PRON", "PronType" : "Rel", "Number" : "plur", "Case" : "Prep"}
    
    "SCONJ":    {POS: SCONJ},
    
    "PROPNSgNom":    {POS: PROPN, "NounType": "prop", "Number": "sing", "Case": "Nom"},
    "PROPNSgAcc":    {POS: PROPN, "NounType": "prop", "Number": "sing", "Case": "Acc"},
    "PROPNSgGen":    {POS: PROPN, "NounType": "prop", "Number": "sing", "Case": "Gen"},
    "PROPNSgDat":    {POS: PROPN, "NounType": "prop", "Number": "sing", "Case": "Dat"},
    "PROPNSgInstr":    {POS: PROPN, "NounType": "prop", "Number": "sing", "Case": "Instr"},
    "PROPNSgPrep":    {POS: PROPN, "NounType": "prop", "Number": "sing", "Case": "Prep"},
    "PROPNPlNom":    {POS: PROPN, "NounType": "prop", "Number": "plur", "Case": "Nom"},
    "PROPNPlAcc":    {POS: PROPN, "NounType": "prop", "Number": "plur", "Case": "Acc"},
    "PROPNPlGen":    {POS: PROPN, "NounType": "prop", "Number": "plur", "Case": "Gen"},
    "PROPNPlDat":    {POS: PROPN, "NounType": "prop", "Number": "plur", "Case": "Dat"},
    "PROPNPlInstr":    {POS: PROPN, "NounType": "prop", "Number": "plur", "Case": "Instr"},
    "PROPNPlPrep":    {POS: PROPN, "NounType": "prop", "Number": "plur", "Case": "Prep"},
    
    "DET":      {POS: DET},
    "SYM":      {POS: SYM},
    "INTJ":     {POS: INTJ},
    "PUNCT":    {POS: PUNCT},
    "NUMNom":      {POS: NUM, "Case" : "Nom"},
    "NUMAcc":      {POS: NUM, "Case" : "Acc"},
    "NUMGen":      {POS: NUM, "Case" : "Gen"},
    "NUMDat":      {POS: NUM, "Case" : "Dat"},
    "NUMInstr":      {POS: NUM, "Case" : "Instr"},
    "NUMPrep":      {POS: NUM, "Case" : "Prep"},
    "AUX":      {POS: AUX},
    "X":        {POS: X},
    "CONJ":     {POS: CONJ},
    "CCONJ":    {POS: CCONJ},
    
    "ADJMSgNomFull":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJMSgAccFull":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Acc", "ADJType" : "FULL"},
    "ADJMSgGenFull":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Gen", "ADJType" : "FULL"},
    "ADJMSgDatFull":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Dat", "ADJType" : "FULL"},
    "ADJMSgInstrFull":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Instr", "ADJType" : "FULL"},
    "ADJMSgPrepFull":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Prep", "ADJType" : "FULL"},
    
    "ADJFSgNomFull":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJFSgNomFull":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJFSgNomFull":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJFSgNomFull":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJFSgNomFull":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJFSgNomFull":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    
    "ADJNSgNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJNSgNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJNSgNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJNSgNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJNSgNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJNSgNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "FULL"},
    
    "ADJPlNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJPlNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJPlNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJPlNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJPlNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "FULL"},
    "ADJPlNomFull":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "FULL"},
    
    "ADJMSgNomShort":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Nom", "ADJType" : "Short"},
    "ADJMSgAccShort":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Acc", "ADJType" : "Short"},
    "ADJMSgGenShort":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Gen", "ADJType" : "Short"},
    "ADJMSgDatShort":      {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Dat", "ADJType" : "Short"},
    "ADJMSgInstrShort":    {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Instr", "ADJType" : "Short"},
    "ADJMSgPrepShort":     {POS: ADJ, "Gender": : "M", "Number" : "sing", "Case" : "Prep", "ADJType" : "Short"},
    
    "ADJFSgNomShort":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Nom", "ADJType" : "Short"},
    "ADJFSgAccShort":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Acc", "ADJType" : "Short"},
    "ADJFSgGenShort":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Gen", "ADJType" : "Short"},
    "ADJFSgDatShort":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Dat", "ADJType" : "Short"},
    "ADJFSgInstrShort":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Instr", "ADJType" : "Short"},
    "ADJFSgPrepShort":      {POS: ADJ, "Gender": : "F", "Number" : "sing", "Case" : "Prep", "ADJType" : "Short"},
    
    "ADJNSgNomShort":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Nom", "ADJType" : "Short"},
    "ADJNSgAccShort":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Acc", "ADJType" : "Short"},
    "ADJNSgGenShort":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Gen", "ADJType" : "Short"},
    "ADJNSgDatShort":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Dat", "ADJType" : "Short"},
    "ADJNSgNomShort":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Instr", "ADJType" : "Short"},
    "ADJNSgNomShort":      {POS: ADJ, "Gender": : "N", "Number" : "sing", "Case" : "Prep", "ADJType" : "Short"},
    
    "ADJPlNomShort":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Nom", "ADJType" : "Short"},
    "ADJPlAccShort":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Acc", "ADJType" : "Short"},
    "ADJPlGenShort":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Gen", "ADJType" : "Short"},
    "ADJPlDatShort":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Dat", "ADJType" : "Short"},
    "ADJPlInstrShort":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Instr", "ADJType" : "Short"},
    "ADJPlPrepShort":      {POS: ADJ, "Gender": : "N", "Number" : "plur", "Case" : "Prep", "ADJType" : "Short"},
    
    "ADJComp": {POS:ADJ, "ADJType":"Comp"}
    
    "VERB":     {POS: VERB},
    "PART":     {POS: PART},
    "SP":     	{POS: SPACE}
}
