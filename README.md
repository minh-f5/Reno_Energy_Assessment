
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
![IMG](.//Images/correlation.png)

![IMG](.//Images/img1.png)
![IMG](.//Images/4.png)

 
### 2. Model Training using Prophet 📈
- Use **Prophet** to train a time-series model with historical solar production data.
- Ensure the model considers external factors like **temperature** and **irradiation** to improve the forecast accuracy.

### 3. Making Predictions 🔮
- Generate predictions for **12/12/2024**, which is the target forecast date.
  
### 4. Visualization after prediction 🖼️
- Display the forecast using **Plotly** for interactive line charts.
- Showcase the forecast components like **trend**, **seasonality**, and **holidays**.

# Extra
![IMG](.//Images/prediction1.png)
![IMG](.//Images/Forecast_Actual3M.png)


  
 ### 5. Deployment Streamlit 🚀

- Create a user-friendly web interface with **Streamlit** to allow users to interact with the model’s results.
- Let users select dates for customized predictions.       

Check out my app built with [Streamlit 🌐](https://minh-f5-reno-energy-assessment-api-deploymentapp-4orfb0.streamlit.app/).

### 6. Future Improvements 🚀 
In the future, the solar production prediction model can be extended and improved in several ways to provide more granular and accurate predictions:

1. Prediction by Quarter, Season, and Year
The current model predicts solar production at a daily level. However, future versions of the model could predict solar production by quarter, season, or even year. These time frames could allow businesses and energy providers to plan better for periods of high or low energy demand.
The inclusion of seasonal factors ( winter, summer...) could help refine predictions, as solar production varies significantly across seasons.
Quarterly and yearly predictions would allow for long-term forecasting, aiding in annual planning and resource allocation.

2. Incorporating Additional Factors
Currently, the model uses temperature and irradiation data. However, several other factors could be integrated into the prediction model to enhance its accuracy. These include:
Cloud cover: Cloudy weather significantly impacts solar power production, so incorporating cloud coverage data would improve the model.
Weather forecasts: Adding short-term weather forecasts can improve the model’s ability to make near-term predictions.
Wind speed and humidity: These environmental factors can also influence solar panel efficiency.
Panel efficiency: Changes in panel efficiency, either due to aging or dust accumulation, could be factored in for more precise predictions.
Economic factors: Incorporating economic indicators like energy prices or policy changes related to renewable energy could provide further context for energy generation.

3. Use of Advanced Machine Learning Models
While Prophet is effective for time-series predictions, advanced models such as LSTM (Long Short-Term Memory networks) or XGBoost could be explored to handle the intricacies of environmental data more effectively, especially when dealing with long-term predictions.
Ensemble models combining multiple algorithms could also be tested to improve prediction accuracy and robustness.

4. Real-Time Predictions
Real-time solar energy predictions using up-to-date data would allow for dynamic forecasting, helping energy producers adjust to changing weather patterns in real-time.
Integration with IoT devices and real-time data streams could further enhance the prediction system, making it adaptable and efficient.





![Solar Energy GIF](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXNjZngzdjBmeGNldGI3c295ajQxcnI2ODFmeXNzYzlsaWhiNWU2diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aixsw4G7b0sQ95rFiW/giphy.gif)