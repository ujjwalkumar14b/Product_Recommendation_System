# Product Recommendation System
![Deployment Screenshot](https://github.com/ujjwalkumar14b/Product_Recommendation_System/blob/main/static/deployment_1.jpg)

## Overview
This project recommend products based on user preference. It is done by collaborative, content-based, hybrid filtering techniques and popularity techniques.The solution includes end-to-end data preprocessing pipeline, feature engineering, model training and evaluation and web deployment using Flask and Bootstrap.


## Project Structure
```
Product_Recommendation_System/
│
├── app.py                                      # Flask application
├── Product_Recommendation_System.ipynb         # Model training notebook
├── Product_Recommendation_System.csv           # Dataset
├── model_cf_item.pkl                           # Item Collaborative model
├── model_cf_user.pkl                           # User Collaborative model
├── model_content.pkl                           # Content-based model
├── model_popular.pkl                           # Popularity model
├── model_products.pkl                          # Product model
├── templates/
│   └── index.html                              # Frontend UI
├── deployment.png                              # App preview
├── requirements.txt                            # Requirements
├── setup.py                                    # Package Installation
└── README.md
```

## Installation
```
git clone https://github.com/ujjwalkumar14b/Product_Recommendation_System.git
cd Product_Recommendation_System
pip install -r requirements.txt
python app.py
```

## Machine Learning Pipeline
### 1. Importing Libraires and Data Collection
* NumPy, Pandas
* Matplotlib, Seaborn
* Scikit-Learn (Cosine Similarity, TF-IDF Vectorizer)
* `Product_Recommendation_System.csv`

### 2. Data Preprocessing
* Missing value handling using `SimpleImputer`
* Feature scaling using `StandardScaler`
* One-hot encoding for categorical variables

### 3. Feature Engineering
* df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
* df['Year'] = df['InvoiceDate'].dt.year
* df['Month'] = df['InvoiceDate'].dt.month
* df['Hour'] = df['InvoiceDate'].dt.hour
* df[*'TotalPrice'] = df['Quantity'] * df['UnitPrice']

### 4. Models Used
* Cosine Similarity
* TF-IDF Vectorizer

### 5. Model Evaluation and Final Model Selection 
* Precision@K
* Hybrid filtering techniques

### 6. Model Deploymwent
* Web Application using HTML, CSS, Bootstrap, Flask
* The application can be deployed on Render


## Author
Ujjwal Kumar
GitHub: [https://github.com/ujjwalkumar14b](https://github.com/ujjwalkumar14b)

## License
This project is open-source and available under the MIT License.
