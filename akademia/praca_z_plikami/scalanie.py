import pandas as pd

arkusz_1_df = pd.read_csv('do_scalania_1.csv')
arkusz_2_df = pd.read_csv('do_scalania_2.csv')

print('Arkusz 1:')
print(arkusz_1_df)
print()

print('Arkusz 2:')
print(arkusz_2_df)
print()

print('Scalone - inner:')
arkusze_polaczone_inner = arkusz_1_df.merge(arkusz_2_df, on='marka', how='inner')
# lub tak:
# arkusze_polaczone_inner = pd.merge(arkusz_1_df, arkusz_2_df, on='marka', how='inner')
print(arkusze_polaczone_inner)
print()

print('Scalone - lewe:')
arkusze_polaczone_left = arkusz_1_df.merge(arkusz_2_df, on='marka', how='left')
print(arkusze_polaczone_left)
print()

print('Scalone - prawe:')
arkusze_polaczone_right = arkusz_1_df.merge(arkusz_2_df, on='marka', how='right')
print(arkusze_polaczone_right)
print()

print('Scalone - wszystko czyli Outer:')
arkusze_polaczone_outer = arkusz_1_df.merge(arkusz_2_df, on='marka', how='outer')
print(arkusze_polaczone_outer)
print()