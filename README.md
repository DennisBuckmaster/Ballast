# Tractor Ballast Calculator

An interactive web application that helps farmers and equipment operators calculate the optimal ballast weight distribution for tractors based on tractor type, implement mounting, power rating, and operating speed.

## Features

- Select tractor type (FWA, 4WD, 2WD)
- Choose implement mounting method (semi-mounted, fully mounted, towed)
- Input tractor PTO power
- Set operating speed
- Calculate optimal ballast requirements
- View weight distribution visualization
- Get detailed explanations of ballast requirements

## Technology Stack

- Streamlit for the web interface
- Pandas for data processing
- Plotly for interactive visualizations

## How to Run Locally

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run ballast_app.py
   ```

3. Open the app in your browser (typically at `http://localhost:8501`)

## Deployment

This application is deployed on Streamlit Community Cloud and can be accessed [here](https://your-app-url-here).

## Background

This calculator is based on established agricultural engineering principles for optimizing tractor ballast to improve:
- Traction and reduced wheel slip
- Soil compaction management
- Fuel efficiency
- Stability and safety
- Tire wear reduction
