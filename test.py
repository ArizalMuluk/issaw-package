import numpy as np

from issaw import sawnorm, sawpref

decision_matrix = np.array(
    [
    [8, 7, 6, 9],  # Alternatif 1
    [6, 8, 7, 5],  # Alternatif 2
    [7, 6, 8, 7],  # Alternatif 3
    [9, 5, 7, 8],  # Alternatif 4
])

tipec = ["benefit", "cost", "benefit", "benefit"]


# Tentukan bobot untuk setiap kriteria
weights = [0.25, 0.25, 0.25, 0.25]  # Bobot sama dalam contoh ini

# Hitung skor SAW
scores = sawnorm(decision_matrix, tipec)
akhir = sawpref(scores, weights)


# Cetak hasilnya
print(scores)
print(akhir)

