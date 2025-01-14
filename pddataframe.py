import pandas as pd

data = { 
    "calories": [420, 380, 390, 500, 450],
    "duration": [50, 40, 45, 32, 56]
}
myvar = pd.DataFrame(data)

print(myvar)