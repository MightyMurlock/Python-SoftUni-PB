skumriya_price = float(input())
tsatsa_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = skumriya_price + (skumriya_price * 0.6)
safrid_price = tsatsa_price + (tsatsa_price * 0.8)
midi_price = 7.5

palamud_total = palamud_kg * palamud_price
safrid_total = safrid_kg * safrid_price
midi_total = midi_kg * midi_price

total = palamud_total + safrid_total + midi_total
print(f"{total:.2f}")