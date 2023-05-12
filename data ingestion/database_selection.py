#GREEDY ALGORITHM

import pandas as pd

def calculate_sustainability_score(data):
    weights = {
        'New Parts Carbon Footprint (kg CO2e)': 0.2,
        'Recycled Parts Carbon Footprint (kg CO2e)': 0.2,
        'Water Usage - New Parts (liters)': 0.1,
        'Water Usage - Recycled Parts (liters)': 0.1,
        'Landfill Waste - New Parts (kg)': 0.1,
        'Landfill Waste - Recycled Parts (kg)': 0.1,
        'Energy Consumption - New Parts (kWh)': 0.1,
        'Energy Consumption - Recycled Parts (kWh)': 0.1,
        'Recycling Rate (%)': 0.05,
        'Toxicity Score - New Parts': 0.025,
        'Toxicity Score - Recycled Parts': 0.025,
        'Remanufacturing Potential': 0.025,
        'Life Cycle Assessment Score': 0.025
    }
    
    # Calculate the sustainability score for each part
    data['Sustainability Score'] = sum([data[attribute] * weight for attribute, weight in weights.items()])
    
    # Return the name of the part with the highest sustainability score
    return data.loc[data['Sustainability Score'].idxmax()]['Part Name']

def calculate_best_cost(data):
    # Calculate the cost for each part
    data['Cost'] = data['Recycled Parts Carbon Footprint (kg CO2e)'] - data['New Parts Carbon Footprint (kg CO2e)']
    
    # Return the name of the part with the lowest cost
    return data.loc[data['Cost'].idxmin()]['Part Name']

def calculate_efforts_score(data):
    weights = {
        'Recycling Rate (%)': 0.4,
        'Remanufacturing Potential (%)': 0.3,
        'Life Cycle Assessment': 0.3
    }
    
    # Calculate the efforts score for each part
    data['Efforts Score'] = sum([data[attribute] * weight for attribute, weight in weights.items()])
    
    # Return the name of the part with the highest efforts score
    return data.loc[data['Efforts Score'].idxmax()]['Part Name']

# Example usage
data = pd.read_excel('aircraft_parts_data.xlsx')
#display(calculate_sustainability_score(data))
#display(calculate_best_cost(data))
#isplay(calculate_efforts_score(data))



def calculate_best_recycling_order(data):
    # Calculate the difference between recycled parts carbon footprint and new parts carbon footprint for each part
    data['Carbon Footprint Difference'] = data['Recycled Parts Carbon Footprint (kg CO2e)'] - data['New Parts Carbon Footprint (kg CO2e)']
    
    # Sort the parts by the carbon footprint difference in descending order
    sorted_data = data.sort_values('Carbon Footprint Difference', ascending=False)
    
    # Initialize a list to store the part names in the order they should be recycled
    recycling_order = []
    
    # Add parts to the recycling order until the total carbon footprint difference is maximized
    total_difference = 0
    for index, row in sorted_data.iterrows():
        if total_difference + row['Carbon Footprint Difference'] > 0:
            recycling_order.append(row['Part Name'])
            total_difference += row['Carbon Footprint Difference']
    
    # Create a dataframe with the recycling order
    recycling_order_df = pd.DataFrame({'Part Name': recycling_order})
    
    # Add a column with the ranking of each part
    recycling_order_df['Rank'] = range(1, len(recycling_order) + 1)
    
    return recycling_order_df

data = pd.read_excel('aircraft_parts_data.xlsx')
recycling_order = calculate_best_recycling_order(data)
display(recycling_order)