from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "No file"
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Calculate descriptive statistics
    desc_stats = df.describe().to_json()

    # Select the 10 important features (update based on your specific important features)
    important_features = ['Life_expectancy', 'Adult_Mortality', 'infant_deaths', 'percentage_expenditure', 
                          'Hepatitis_B', 'Measles', 'BMI', 'Polio', 'GDP', 'Schooling']

    selected_df = df[important_features]

    # Calculate the correlation matrix
    correlation_matrix = selected_df.corr().to_json()

    return jsonify({
        "descriptive_statistics": desc_stats,
        "correlation_matrix": correlation_matrix
    })

if __name__ == '__main__':
    app.run(debug=True)
