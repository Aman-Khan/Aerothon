import pandas as pd
import mysql.connector

con = mysql.connector.connect(username='aero', password='aero123', host='localhost')
    
cursor = con.cursor(buffered=True)
cursor.execute('USE aero_db')
# cursor.execute('SHOW TABLES')
# data = cursor.fetchall()
# print(data)


# Read Excel file
df = pd.read_excel('aircraft_parts_data.xlsx')

columns = df.columns.tolist()
# print(columns)
data = df.head(1)

for index, row in data.iterrows():
    try:
        part_name = row['Part Name']
        mat_comp = row['Material Composition']
        age = row['Age (years)']
        condition=True
        if(row['Condition']=='Used'):
            condition:False
        location = row['Location']
        manufacturer = row['Manufacturer']
        aircraft_mod = row['Aircraft Model']
        
        query1 = f"INSERT INTO part_tb(part_name, mat_comp, age, condi, location, manufacturer, aircraft_mod) VALUES ('{part_name}', '{mat_comp}', {age}, {condition}, '{location}', '{manufacturer}', '{aircraft_mod}')"
    
        cursor.execute(query1)
        con.commit()

        last_id = cursor.lastrowid

        pot_usecase = row['Potential Use Cases']
        remanufacPotential = row['Remanufacturing Potential']
        renewableContent= row['Renewable Material Content (%)']
        recycleRate = row['Recycling Rate (%)']
        lca = row['Life Cycle Assessment Score']
        
        query2 = f"INSERT INTO sustain_data VALUES ({last_id}, '{pot_usecase}', {remanufacPotential}, {renewableContent}, {recycleRate}, {lca})"
        cursor.execute(query2)
        con.commit()

        nCarbonFP = row['New Parts Carbon Footprint (kg CO2e)']
        nWaterUsage = row['Water Usage - New Parts (liters)']
        nLandFill = row['Landfill Waste - New Parts (kg)']
        nEneConsum = row['Energy Consumption - New Parts (kWh)']
        nToxicScore = row['Toxicity Score - New Parts']
        
        query3 = f"INSERT INTO recycle_data VALUES ({last_id}, {nCarbonFP}, {nWaterUsage}, {nLandFill}, {nEneConsum}, {nToxicScore})"
        cursor.execute(query3)
        con.commit()

        rCarbonFP = row['Recycled Parts Carbon Footprint (kg CO2e)']
        rWaterUsage = row['Water Usage - Recycled Parts (liters)']
        rLandFill = row['Landfill Waste - Recycled Parts (kg)']
        rEneConsum = row['Energy Consumption - Recycled Parts (kWh)']
        rToxicScore = row['Toxicity Score - Recycled Parts']
        
        query4 = f"INSERT INTO new_manu_data VALUES ({last_id}, {nCarbonFP}, {nWaterUsage}, {nLandFill}, {nEneConsum}, {nToxicScore})"
        cursor.execute(query4)
        con.commit()
    except: raise mysql.connector.errors.ProgrammingError
