# Soil Quality Checker

This is a **Soil Quality Checker** application built using **Streamlit**. The application predicts the type of soil based on its chemical properties such as pH, Nitrogen, Phosphorus, Potassium, and Organic Carbon content.

## Features

- User-friendly web interface to input soil parameters.
- Predicts the soil type using a trained machine learning model.
- Provides instant results for soil quality analysis.

## Dataset

The application uses a dataset containing soil properties and their corresponding soil types. The dataset includes the following features:
- `pH`: Acidity or alkalinity of the soil.
- `Nitrogen`: Nitrogen content in mg/kg.
- `Phosphorus`: Phosphorus content in mg/kg.
- `Potassium`: Potassium content in mg/kg.
- `Organic_Carbon`: Organic carbon content in percentage.
- `Soil_Type`: The type of soil (e.g., Sandy, Loamy, Clay).

## Installation

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/your-repo/soil-quality-checker.git
   cd soil-quality-checker
2.pip install -r requirements.txt
3.streamlit run app.py
File structure:
soil-quality-checker/
├── [app.py](http://_vscodecontentref_/0)                 # Streamlit application code
├── soil_quality_model.pkl # Trained machine learning model
├── soil_data.csv          # Dataset (optional, for reference)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
