import pandas as pd

df = pd.read_excel('aircraft_parts_data.xlsx')

carbon_footprint_weight = 0.35
water_usage_weight = 0.2
landfill_waste_weight = 0.1
energy_consumption_weight = 0.15
toxicity_score_weight = 0.1
recycling_rate_weight = 0.1

def calculate_sustainability_score(row):
    carbon_footprint_score = (row['New Parts Carbon Footprint (kg CO2e)'] - row['Carbon Footprint Saved (kg CO2e)']) / row['New Parts Carbon Footprint (kg CO2e)']
    water_usage_score = (row['Water Usage - New Parts (liters)'] - row['Water Usage Saved (liters)']) / row['Water Usage - New Parts (liters)']
    landfill_waste_score = (row['Landfill Waste - New Parts (kg)'] - row['Landfill Waste Saved (kg)']) / row['Landfill Waste - New Parts (kg)']
    energy_consumption_score = (row['Energy Consumption - New Parts (kWh)'] - row['Energy Consumption Saved (kWh)']) / row['Energy Consumption - New Parts (kWh)']
    toxicity_score_difference = row['Toxicity Score - New Parts'] - row['Toxicity Score - Recycled Parts']
    recycling_rate_score = row['Recycling Rate (%)'] / 100
    
    sustainability_score = carbon_footprint_score * carbon_footprint_weight \
                            + water_usage_score * water_usage_weight \
                            + landfill_waste_score * landfill_waste_weight \
                            + energy_consumption_score * energy_consumption_weight \
                            + toxicity_score_difference * toxicity_score_weight \
                            + recycling_rate_score * recycling_rate_weight
    
    return sustainability_score

df = df.head(10)

df['Sustainability Score'] = df.apply(calculate_sustainability_score, axis=1)

data = df.sort_values('Sustainability Score', ascending=False)


for index, row in data.iterrows():
    part_name = row['Part Name']
    mat_comp = row['Material Composition']
    age = row['Age (years)']
    condition=True
    if(row['Condition']=='Used'):
        condition:False
    location = row['Location']
    manufacturer = row['Manufacturer']
    aircraft_mod = row['Aircraft Model']
    sus = row['Sustainability Score']

    print(part_name, mat_comp, age, condition, location, manufacturer, aircraft_mod, sus)
