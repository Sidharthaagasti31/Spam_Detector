<div align='center'>
<img src="https://github.com/Sidharthaagasti31/Spam_Detector/assets/50338854/d47b535a-084f-428e-b0bf-562062244eed",alt='spam',height=70,width=70 >
</div>

# Spam_Detector
Created a webapp to detect spam sms

### OVERVIEW
This project aims to help in spam message detection . We have seen a rise in spam messages that target people and also alot of people get traped into this spam message/sms. In this project we have deployed a webapp that take an input from user and it will help people to know if the sms / message is spam or not .

### Dataset
We have dowmloaded this dataset from [kaggke.com](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). This dataset contains following features
- v1/target this tells if the sms is spam or not
- v2/text this stores the actual text
- Unnamed: 2 , Unnamed: 3,Unnamed: 4 which contains less data but more nan values which can be consilder as noise here

### Methodology

The project follows the following steps to classify spam message:
1. Data Preprocessing: The dataset is cleaned and processed to handle missing values and any inconsistencies.
2. Exploratory Data Analysis (EDA): Visualizations and statistical analysis are performed to gain insights into the dataset and understand the relationships between different features.
3. Model Selection: Various classification models are considered and evaluated to determine the most suitable one for the task.
4. Model Training: The chosen model is trained using the preprocessed dataset.
5. Model Evaluation: The trained model is evaluated using appropriate metrics to measure its performance.
6. Predictions: The model is used to predict house prices for new, unseen data
7. Stored the model using pickle to create webapp .
8. Using streamlit created webapp to detect spam message/sms

### Dependencies :
to run this locally on your Desktop you might need to install below libraries 
1. sklearn module
- pip install scikit-learn
2. nltk library
- pip install nltk
3. streamlit
- pip install streamlit

### Run using streamlit
To run it on your local server, open command prompt and run below command
`streamlit run app.py`

### Results
After testing multiple clasifier models and observing the metrics , we decides to train our data using Multinomial Naive Bayes and got precision around 99% . Then we created webapp using streamlit that uses Multinomial Naive Bayes to classify sms to spam or ham . 

![Web capture_7-6-2023_121233_localhost](https://github.com/Sidharthaagasti31/Spam_Detector/assets/50338854/d597d8ab-0a6f-4ca0-9873-abec8adbf229)



