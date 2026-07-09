import numpy as np
import pandas as pd

# Contoh NumPy
nilai = np.array([75, 80, 85, 90, 95])
print("Rata-rata nilai:", np.mean(nilai))

# Contoh Pandas
df = pd.DataFrame({
    "Material": ["Semen", "Pasir", "Baja"],
    "Harga": [70000, 250000, 14500000]
})

print("\nData Material:")
print(df)
