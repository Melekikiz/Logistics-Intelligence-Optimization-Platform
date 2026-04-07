# Logistics-Intelligence-Optimization-Platform

**An interactive logistics decision support system for cost optimization, delay root-cause analysis, and scenario-based operational planning.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://logistics-intelligence-optimization-platform-bp8oraszptyggvrz2.streamlit.app/)

**AI-Driven Decision Support System for Cost, Delay & Route Optimization**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

<img width="1680" height="837" alt="1" src="https://github.com/user-attachments/assets/31286e94-acf7-4d18-95ea-55e5551aac5b" />


# Executive Overview

Logistics operations function under highly volatile conditions.
This platform is a Decision Support System (DSS) designed to bridge the gap between raw logistics data and strategic action.

It analyzes end-to-end operational efficiency by correlating:

Fuel prices
Port congestion
Weather risks
Deadhead ratios
Route performance

into a single actionable dashboard.


# Business Problem & Objective

Traditional logistics management often analyzes variables in silos. This leads to:

Unseen Financial Leakage

Hidden costs from deadhead (empty return) trips.

Reactive Decision Making

Failing to anticipate port congestion or seasonal delay impacts.

Cost Inefficiency

Inability to simulate fuel price volatility on profitability.

Project Objective

To empower operational managers with a data-driven decision tool that:

Models operational costs
Identifies delay root causes
Simulates external risks
Provides automated strategic recommendations



# Data Model & Architecture

The system utilizes a realistic synthetic dataset designed to simulate complex supply chain scenarios.

Spatial Data

Origin

Destination

Route Distance

Operational Data

Cargo Type (Dry, Cold Chain, Hazardous, Oversized)

Port Congestion Level

Temporal Data

Planned Duration

Actual Duration

Weather Conditions



# Operational Cost & Stress Test Modeling

### 🧮 Dynamic Cost Model
The core of the system calculates the total operational impact using:

$$Total\ Cost = Fuel + Delay + Handling + Fixed + Deadhead$$

Cost Components

Fuel Cost
Distance-based consumption model with dynamic fuel pricing.

Delay Cost
Penalty calculated from planned vs actual duration.

Handling Cost
Cargo-type dependent operational cost.

Fixed Cost
Vehicle and operational overhead.

Deadhead Cost
Empty return ratio based hidden cost.

# Stress Test Variables
Fuel Price Sensitivity

Real-time simulation of fuel price index changes.

Deadhead Loss Analysis

Calculation of financial drain caused by unoptimized return loads.

Winter Multiplier

Automated 25% delay penalty for seasonal risk assessment.

# Visual Analytics & Root Cause Identification
<img width="1680" height="837" alt="2" src="https://github.com/user-attachments/assets/35a66999-ee96-44a5-8915-105f0d3b06c9" />
<img width="1680" height="837" alt="3" src="https://github.com/user-attachments/assets/deca9da6-09b1-4009-9433-1741b6c90cec" />


The platform identifies where operational losses occur:

Route Analysis

Identifies high-cost corridors.

Weather Variance

Box plots showing transit duration volatility.

Correlation Heatmap

Identifies root causes of delay (e.g., port congestion).

# Decision Support Engine

The system provides automated recommendations:

Route Optimization

Flags corridors exceeding delay thresholds.

Financial Consolidation

Identifies shipment merge opportunities.

Gate-in Optimization

Suggests night-shift operations for congested ports.

Seasonal Buffer Planning

Recommends buffer time during winter operations.

This transforms the dashboard into a Decision Support System.
<img width="1680" height="837" alt="4" src="https://github.com/user-attachments/assets/8ba206c3-f080-4878-8256-ac734c08d617" />

# Strategic Intervention Simulator (What-If)

Interactive scenario simulation:

Users can adjust:

Fuel price

Deadhead ratio

Congestion reduction

Winter mode

The system calculates:


Cost impact

Delay reduction

Potential savings

Example:

"What if we reduce congestion by 10%?"

The platform instantly calculates savings.

# Business Impact & ROI

Expected operational improvements:

10–20% cost reduction potential
Reduced SLA breaches
Improved route efficiency
Reduced deadhead losses
Better operational planning

# Dashboard Features
Executive Summary

KPI Panel

Stress Test Controls

Route Cost Analysis

Delay Distribution

Cost Breakdown

Correlation Analysis

Decision Engine

Scenario Simulator

# Tech Stack

Python

Pandas

Streamlit

Plotly Express

# How to Run

Clone repository:

git clone https://github.com/Melekikiz/Logistics-Intelligence-Optimization-Platform.git

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py


# Future Roadmap
Predictive Delay Modeling (ML)

Real-time Port Congestion API

Fleet Utilization Optimization

Route Optimization Algorithm

Demand Forecasting

# Final Note

This project demonstrates how logistics data can be transformed into an operational decision support system.

Instead of only visualizing data, the platform provides actionable insights and scenario-based optimization recommendations.


## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Contact
Melek İkiz  
LinkedIn: https://www.linkedin.com/in/melek-ikiz-520065373/  
Email: mellikiz.33@gmail.com
