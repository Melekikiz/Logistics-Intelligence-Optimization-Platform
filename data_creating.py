import pandas as pd
import numpy as np
import random

n_rows = 1500
ports = ['Mersin', 'Ambarli', 'Izmir', 'Kocaeli', 'Iskenderun']
cargo_types = ['Dry', 'Cold_Chain', 'Hazardous', 'Oversized']
weather_types = ['Clear', 'Rainy', 'Stormy']

data = {
    'shipment_id': [f'SHP-{i:05d}' for i in range(n_rows)],
    'origin': [random.choice(ports) for _ in range(n_rows)],
    'destination': [random.choice(ports) for _ in range(n_rows)],
    'cargo_type': [np.random.choice(cargo_types, p=[0.5, 0.2, 0.2, 0.1]) for _ in range(n_rows)],
    'weather': [np.random.choice(weather_types, p=[0.7, 0.2, 0.1]) for _ in range(n_rows)],
    'port_congestion_level': [random.randint(1, 10) for _ in range(n_rows)] # 1: Boş, 10: Kilit
}

df = pd.DataFrame(data)

df = df[df['origin'] != df['destination']].reset_index(drop=True)


dist_map = {p: i*200 + 150 for i, p in enumerate(ports)} 
df['distance_km'] = df.apply(lambda x: abs(dist_map[x['origin']] - dist_map[x['destination']]) + random.randint(-50, 50), axis=1)


df['gate_in_wait_hrs'] = df['port_congestion_level'] * np.random.uniform(0.5, 1.5)


def calculate_duration(row):
    base_speed = 70 # km/h
    if row['weather'] == 'Rainy': base_speed -= 15
    if row['weather'] == 'Stormy': base_speed -= 30
    return (row['distance_km'] / base_speed) + row['gate_in_wait_hrs']

df['actual_duration_hrs'] = df.apply(calculate_duration, axis=1)
df['planned_duration_hrs'] = (df['distance_km'] / 70) + 2 

def calculate_cost(row):
    base_fuel_price = 44.20
    cargo_multiplier = {'Dry': 1.0, 'Cold_Chain': 1.4, 'Hazardous': 1.6, 'Oversized': 2.0}
    
    fuel_cost = (row['distance_km'] / 100) * 35 * base_fuel_price 
    fixed_cost = 3500 
    delay_penalty = max(0, row['actual_duration_hrs'] - row['planned_duration_hrs']) * 250 
    
    total = (fuel_cost + fixed_cost + delay_penalty) * cargo_multiplier[row['cargo_type']]
    return round(total, 2)

df['total_cost_try'] = df.apply(calculate_cost, axis=1)

df.to_csv('logistics_data.csv', index=False)
print("Success :", len(df))