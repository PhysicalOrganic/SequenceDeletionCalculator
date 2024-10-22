# SequenceDeletionCalculator
This repository contains the code required to compute possible deletions of monomers from a sequence-defined oligourethane. The script is written in Python and has been tested with Python 3.11.0. No third party packages are required.

## Usage
First, define your monomer library in the monomers.py file by including the 3-letter and one letter codes in the `THREE_LETTER_CODES` dictionary. Then specify the monomer 1-letter code and the monomer mass in the `ONE_LETTER_CODE_MASS_PAIRS` dictionary. Then specify the adducts you intend to see in your mass spectrum by defining them as `Adduct` objects in the adducts.py file.
<br>
<br>
Run the Python script with the required arguments.

    python3 SequenceDeletionCalculator.py -i AyyA

Specify the sequence with either 1-letter codes (above) or using 3-letter codes (below)

**Note**: 3-letter codes must be specified in quotation marks.

    python3 SequenceDeletionCalculator.py -i "Ala d2Tyr d2Tyr Ala"