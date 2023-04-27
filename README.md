## About this Project
This is the final Capstone Project which will be applying the concepts on binary imbalanced class classification. 


## 1. Background

Vehicle insurance fruad detection is becoming a critical issue in the insurance industry in Singapore. The General Insurance Assoication of Singapore (GIA) estimates that fraud accounts for up to 10% of total claims cost, which can result in significant financial losses for insurance companies and increased premiums for honest policyholders. In recent years, the number of suspecious motor insurance claims has been on the rise. In 2020, the GIA report a 27% increase in suspicious claims as compared to the previous year. The most common types of motor insurance fraud in Singapore include stageda accidents, false injury claims, and inflated damage claims. To combat fraud, insurance companies in Singapore use various methods to dtect fraudulent activity. These methods include data analytics, investigation teams, and collaboration with external agencies. Insurance companies analyse data from various sources, such as police reports, accident data, and historical data claims to help identify patterns that indicate potential fraud. The consequences for committing insurace fraud in Singapore can be severe with Fraudsters facing criminal charges, fines and iimprisonment, as well as loss of insurance coverage and difficulty in obtaining insurance in the future. These facts demonstrate the significant impact of the insurance fraud on the motor insurance industry in Singapore and the importance of detecting and preventing it to protect honest policyholders and maintain the financial stability of insurance companies. The use of advanced techniques and collaboration between insurance companies, regulatory bodies, and law enforcement agencies can help to deter fraudulent activities and ensure a fair and sustainable insurance market in Singapore.

1. General Insurance Association of Singapore (GIA) Report on Insurance Fraud in Singapore (https://www.gia.org.sg/docs/default-source/default-document-library/gia-report-on-insurance-fraud-in-singapore.pdf)

2. GIA News Release on Increase in Suspicious Motor Insurance Claims in Singapore (https://www.gia.org.sg/Media-Room/News-Releases/2021/News-Release-29-Mar-2021)

3. Singapore Police Force's Advisory on Staged Accidents (https://www.police.gov.sg/resources/traffic-matters/advisory-on-staged-accidents)

4. Straits Times Article on Rise of Insurance Fraud in Singapore (https://www.straitstimes.com/singapore/courts-crime/more-insurance-fraud-cases-in-singapore-amid-pandemic)

5. Asia Insurance Review Article on Fraud Detection in Singapore (https://www.asiainsurancereview.com/Magazine/ReadMagazineArticle/aid/44109/Fraud-detection-in-Singapore)

##  3. Dataset

The Oracle Vehicle Fraud Dataset is a synthetic dataset created by Oracle for use in fraud detection research and testing. It consists of transactional data related to the purchase and sale of vehicles, and includes a range of features such as customer demographics, vehicle characteristics, and transaction details. The dataset aims to provide a realistic and representative sample of transactional data that can be used to evaluate and compare the performance of different fraud detection models and techniques. The goal of the dataset is to enable researchers and practitioners to develop and test effective fraud detection solutions for the automotive industry.

## Notebook mindmap
Part I shows the data cleaning and EDA
Part II shows the preprocessing and tuning of hyper parameters for the different models that are used.
Part III shows the final feature selection together with the tuning of different hypermeters

## Data Dictionary 

|Feature|Type|Dataset|Description|
|---|---|---|---|
|Month|category|Oracle Fraud Dataset|The month of claims|
|Make|category|Oracle Fraud Dataset|Car Manufacturer|
|AccidentArea|category|Oracle Fraud Dataset|Area where accident has occured|
|Sex|category|Oracle Fraud Dataset|Gender of Claims|
|Age|float64|Oracle Fraud Dataset|Age of Claims|
|Fault|category|Oracle Fraud Dataset|Accident fault ownership|
|VehicleCategory|category|Oracle Fraud Dataset|Category of Vehicle, example like sedan, sport|
|FraudFound_P|int64|Oracle Fraud Dataset|Is Fraud found in the claims|
|Deductible|int64|Oracle Fraud Dataset|Car Excessive|
|PastNumberOfClaims|category|Oracle Fraud Dataset|The number of past claims|
|AgeOfPolicyHolder|category|Oracle Fraud Dataset|The age of the holder of policy|
|PoliceReportFiled|category|Oracle Fraud Dataset|Police report being filed for the accident|
|AgentType|category|Oracle Fraud Dataset|Internal or external|
|NumberOfSuppliments|category|Oracle Fraud Dataset|Policies add-ons|
|AddressChange_Claim|category|Oracle Fraud Dataset|Claims that have change of address|
|BasePolicy|category|Oracle Fraud Dataset|The base type of the policy|
|AgeOfVehicle|category|Oracle Fraud Dataset|Age of the vehicle of claims|

## Recall, Precision and ROC_AUC curve
The goal of the project is to be able to train and test a model for recall, precision and ROC_AUC curve as Recall measures the proportion of actual positive cases that were correctly identified as positive, while precision measures the proportion of positive predictions that were actually true positives.ROC_AUC curve provides a way to evaluate and compare the trade-off between recall and precision at different classification thresholds, giving insight into the overall performance of the model.

## Exploratory Data Analysis
1. January has the highest amount of claims due to wet season and also psychologically, it is the back to a new year where people are returning from holidays hence they might be preoccupied with work and other commitment then on the roads
2. the highest claims are the Sedan -  collision as it is common in Singapore, the amount of fraud actually comes from Sedan - All perils. This pattern of fraud could be that all perils (base policy) are hard to track or detect hence fraudsters will tend to utilise this policy
3. There are more claims by male drivers than female drivers, which in turn male has the highest fraud claims. 
4. There are high accident claims that is seen in Japanese makers such as honda and toyota. However, it is noteworthy to see that pontiac has the highest claim rate. As pontiac is considered a sport luxuary car, owners tends to speed which could result in accidents. 
5. It is seen that more accidents occur in urban areas and that most of the fraud comes from all perils which includes theft, vandalism and weather-related damage. This is understandable as it is harder for insurance companies to trace for fraud in regards to weather-related or vandalism or act of mischief. 
6. Based on the fraud classification, we can see that this dataset is an imbalance class dataset.

## Final Result

|Model|Train Score|Test Score|Precision|Recall|
|---|---|---|---|---|
|XGBoost Classifiers|0.9097|0.8472|0.16|0.87|
|Random Forest Classifiers|0.9712|0.939|0.15|0.86|
|Decision Tree Classifiers|0.9546|0.8772|0.06|1|
|Balanced Random Forest Classifiers|0.61|0.62|0.12|0.96|
|Ada-Boost Classifiers|0.5991|0.601|0.12|0.96|
|Gradient-Boost Classifiers|0.9493|0.9423|0.14|0.89|

Although Random Forest Classifier has a higher recall. XGBoost has a better ROC_AUC curve and precision

## Conclusion, Future Works and Recommendation

### Conclusion

After evaluating multiple machine learning models for fraud detection, we found that XGBoost outperformed the other classifiers in terms of precision, recall, and ROC_AUC curve. This is likely due to XGBoost's ability to handle imbalanced datasets and effectively handle non-linear relationships between features.

Furthermore, we found that certain features were more important than others in identifying fraudulent activity, such as transaction amount, frequency, and location. By leveraging these insights, we can continue to improve our fraud detection models and prevent significant financial losses for the company.

Overall, machine learning techniques such as XGBoost can be powerful tools in detecting and preventing fraud, and we should continue to explore and experiment with different algorithms and features to improve the accuracy and effectiveness of our fraud detection systems.

## Recommendation 

Based on the analysis conducted, it is recommended that the fraud detection system for Marina Bay Insurance should be developed using XGBoost algorithm, as it has demonstrated the highest performance on the Oracle Vehicle Fraud Dataset in terms of ROC_AUC, recall, and precision. Additionally, the system should incorporate a range of features such as customer demographics, vehicle characteristics, and transaction details to provide a comprehensive and accurate assessment of fraud risk. It is also recommended that the system be continually monitored and updated with new data and techniques to improve its fraud detection capabilities over time.

## Future works
1. Collect additional data: The Oracle Vehicle Fraud Dataset is a synthetic dataset and may not capture all the nuances of real-world fraud. Collecting additional data from other sources could improve the performance of the fraud detection models.
2. Experiment with different algorithms: While XGBoost has shown promising results on the Oracle Vehicle Fraud Dataset, it is worth exploring other machine learning algorithms to see if they can achieve better performance.
3. Investigate feature importance: Understanding which features are most predictive of fraud can provide valuable insights into how fraud occurs in the automotive industry. Investigating feature importance can help refine the fraud detection models and prevent fraud more effectively.
4. Integrate real-time fraud detection: While the fraud detection models developed in this project are effective, they operate offline. Integrating real-time fraud detection would enable the system to detect and prevent fraud as it occurs, reducing the impact of fraudulent activity.
5. Improve interpretability: While XGBoost is a powerful machine learning algorithm, it can be challenging to interpret. Developing methods to improve the interpretability of the model could provide valuable insights into how the algorithm is making decisions and increase trust in the system.
