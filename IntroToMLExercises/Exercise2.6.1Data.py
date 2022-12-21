import pandas as pd
import numpy as np
soldata = pd.read_csv("https://raw.githubusercontent.com/whitead/dmol-book/main/data/curated-solubility-dataset.csv")
soldata.head()

for column in soldata[['ID', 'Name', 'InChI', 'InChIKey', 'SMILES', 'Solubility', 'SD', 'Ocurrences', 'Group', 'MolWt', 'MolLogP', 'MolMR', 'HeavyAtomCount', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms', 'NumRotatableBonds', 'NumValenceElectrons', 'NumAromaticRings', 'NumSaturatedRings', 'NumAliphaticRings', 'RingCount', 'TPSA', 'LabuteASA', 'BalabanJ', 'BertzCT']]:
    columnSeriesObj = soldata[column]
    columnmax = np.amax(columnSeriesObj)
    columnmin = np.amin(columnSeriesObj)
    print(columnmax, columnmin)