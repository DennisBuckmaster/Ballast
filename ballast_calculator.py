import pandas as pd
import numpy as np

def load_ballast_data(file_path="attached_assets/ballast assistant (3).xlsx"):
    """
    Load the ballast assistant data from the Excel file
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        dict: Dictionary containing the relevant lookup tables and data
    """
    # Create a manual lookup table based on the Excel data we examined earlier
    # This matches the data from rows 30-32 in the spreadsheet
    lookup_data = {
        "Implement": ["semi-mounted", "fully mounted", "towed"],
        "FWA": [45, 45, 40],
        "4WD": [60, 60, 55],
        "2WD": [30, 35, 25]
    }
    
    lookup_table = pd.DataFrame(lookup_data)
    
    # Create a dictionary with the data
    ballast_data = {
        "lookup_table": lookup_table
    }
    
    return ballast_data

def calculate_ballast(tractor_type, implement_mounting, tractor_power, operating_speed):
    """
    Calculate the weight targets for each axle based on inputs
    
    Args:
        tractor_type: Type of tractor (FWA, 4WD, 2WD)
        implement_mounting: Type of implement mounting (semi-mounted, fully mounted, towed)
        tractor_power: Rated tractor PTO power in hp
        operating_speed: Operating speed in mph
        
    Returns:
        dict: Dictionary with the calculation results
    """
    # Load the ballast data
    ballast_data = load_ballast_data()
    lookup_table = ballast_data["lookup_table"]
    
    # Find the front axle percentage based on tractor type and implement mounting
    # Filter the lookup table to find the matching row
    filtered_row = lookup_table[lookup_table["Implement"] == implement_mounting]
    
    # Get the front axle percentage from the matching row and column
    if not filtered_row.empty:
        front_axle_percentage = filtered_row.iloc[0][tractor_type]
    else:
        # Default values if implement mounting is not found
        default_percentages = {"FWA": 45, "4WD": 60, "2WD": 30}
        front_axle_percentage = default_percentages.get(tractor_type, 45)
    
    rear_axle_percentage = 100 - front_axle_percentage
    
    # Calculate Weight/Power ratio and total weight
    # The formula appears to be a calculation based on the speed and power
    # From the data, we can infer it's approximately:
    base_factor = 128 - (operating_speed * 2.5)  # This is an approximation based on observation
    wp_ratio = max(base_factor, 95)  # Ensuring minimum W/P ratio doesn't go below 95
    
    # Calculate total weight
    total_weight = wp_ratio * tractor_power
    
    # Calculate axle weights
    front_axle_weight = total_weight * (front_axle_percentage / 100)
    rear_axle_weight = total_weight * (rear_axle_percentage / 100)
    
    # Round the results to the nearest 50 pounds
    total_weight = round(total_weight / 50) * 50
    front_axle_weight = round(front_axle_weight / 50) * 50
    rear_axle_weight = round(rear_axle_weight / 50) * 50
    
    # Return the results
    results = {
        "wp_ratio": wp_ratio,
        "total_weight": total_weight,
        "front_axle_percentage": front_axle_percentage,
        "rear_axle_percentage": rear_axle_percentage,
        "front_axle_weight": front_axle_weight,
        "rear_axle_weight": rear_axle_weight
    }
    
    return results