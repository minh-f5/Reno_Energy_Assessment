
# 🌞 Solar Production Prediction for Liège 🌞

## 📊 Overview

In this project, we aim to **predict solar production** in the region of **Liège**, Belgium, using historical data on **temperature** 🌡️ and **irradiation** ☀️. By leveraging the power of **Prophet** (a time series forecasting tool), we will build a model that forecasts solar energy production.

You’ll find the following resources to guide your prediction:

- **Temperature and Irradiation Data** 📈
- **Historical Solar Production Data** from **Elia Open Data** 🌍: 
  [Elia Solar Data for Liège](https://opendata.elia.be/explore/dataset/ods032/table/?sort=datetime&refine.region=Li%C3%A9ge)

## 🔧 Tools & Technologies

- **Prophet** 🌟: A forecasting tool developed by Facebook, great for time-series data.
  - [Prophet Documentation](https://facebook.github.io/prophet/docs/quick_start.html)
- **Python** 🐍: The primary language for processing and analyzing the data.
- **Pandas** 📊: For data manipulation.
- **Plotly** 📉: For beautiful and interactive visualizations.
- **Streamlit** 🎨: To deploy the app and display the forecast.

## 🧑‍💻 Goals

The main objectives for this project are:

1. **Load CSV Data** using Python and **Prophet**:
   - Historical solar production data
   - Temperature and Irradiation data
2. **Connect to Elia API** 🔌 and get real-time solar production data (without downloading it).
3. **Train the Prophet Model** using historical data until **11/12/2024**.
4. **Predict Solar Production** for **12/12/2024** 🌞.
5. **Visualize** the model’s predictions and components using **interactive plots**.

## 🛠️ Steps to Complete

### 1. Data Preparation 📅
* Step 1:
- Load historical **temperature**, **irradiation** from IRM.csv
- Connect it into a single DataFrame using Python's **Pandas** 📊.
- Clean the data by handling any missing values or duplicates.
- Combine temperature and irradiation data into a single structure that can be used for modeling.

* Step 2: 
- Use Elia's Open Data API to pull historical solar production data for the region of **Liège** 📈.
- The Elia data is collected every 15 minutes, so we will need to transform this data to an hourly frequency to match the data in **IRM.csv** ⏳.
- Perform the following transformations on the data from Elia:
    + Resample the data to hourly intervals, calculating the average solar production within each hour.
    + Align the time series to match the format of **IRM.csv**, ensuring the **datetime** column is in the correct format for modeling.

- Clean and preprocess the data by handling missing values, ensuring date formats are correct, and merging datasets.

* Step 3: Visualization before Train Model


![Image Description](images/correlation.png)

![Image Description](images/img1.png)

![Image Description](images/4.png)





  
### 2. Model Training using Prophet 📈
- Use **Prophet** to train a time-series model with historical solar production data.
- Ensure the model considers external factors like **temperature** and **irradiation** to improve the forecast accuracy.

### 3. Making Predictions 🔮
- Generate predictions for **12/12/2024**, which is the target forecast date.
  
 4. Visualization 🖼️
- Display the forecast using **Plotly** for interactive line charts.
- Showcase the forecast components like **trend**, **seasonality**, and **holidays**.

* This is the extra work
![Image Description](images/prediction1.png)



![Image Description](images/Forecast_Actual3M.png)


  
 5. Deploy with Streamlit 🚀
- Create a user-friendly web interface with **Streamlit** to allow users to interact with the model’s results.
- Let users select dates for customized predictions.       

- Check out the live Streamlit app here:

[Solar Production Prediction App](https://minh-f5-reno-energy-assessment-api-deploymentapp-4orfb0.streamlit.app/)




 🚀 


![Solar Energy GIF](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXNjZngzdjBmeGNldGI3c295ajQxcnI2ODFmeXNzYzlsaWhiNWU2diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aixsw4G7b0sQ95rFiW/giphy.gif)

