import pandas as pd
import numpy as np

df = pd.read_csv("energy_usage.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['energy_kwh'] = pd.to_numeric(df['energy_kwh'], errors='coerce')

df = df.dropna(subset=['timestamp', 'device_id', 'room_id', 'energy_kwh'])

df.to_csv("cleaned_energy_usage.csv", index=False)

device_rows = []
for device_id, group in df.groupby('device_id'):
    values = group['energy_kwh'].to_numpy()
    device_rows.append({
        'device_id': device_id,
        'total_energy_kwh': np.sum(values),
        'avg_energy_kwh': np.mean(values)
    })

device_summary = pd.DataFrame(device_rows)
print("Energy per device:")
print(device_summary)

room_summary = df.groupby('room_id')['energy_kwh'].agg(['sum', 'mean', 'count'])
print("\nEnergy per room:")
print(room_summary)