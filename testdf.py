import pandas as pd

slovnik = {'Day': [1, 2, 3, 4, 5],
           'Navstevnost': [54, 63, 21, 84, 95],
           'Bounce': [65, 67, 66, 63, 59]}

df = pd.DataFrame(slovnik).set_index('Day')
print(df)
