
import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px
from prophet.plot import plot_plotly, plot_components_plotly
import matplotlib.pyplot as plt

def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        /* General text color */
        .stMarkdown, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown li {{
            color: #FFFFFF; /* White text */
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        table, th, td {{
            border: 2px solid white;
            padding: 8px;
            color: white; /* White text */
        }}
        th, td {{
            text-align: left;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def load_data():
    df = pd.read_csv("Data/data_prediction.csv")
    
    df['ds'] = pd.to_datetime(df['ds'])  
    return df

def train_prophet(df):
    model = Prophet()
    model.fit(df)
    return model

def predict_solar_production(model, periods=72):
    future = model.make_future_dataframe(periods=periods, freq='h')
    forecast = model.predict(future)
    forecast['yhat'] = forecast['yhat'].clip(lower=0)
    forecast['yhat_lower'] = forecast['yhat_lower'].clip(lower=0)
    forecast['yhat_upper'] = forecast['yhat_upper'].clip(lower=0)
    return forecast

def app():

    set_background("https://img1.getimg.ai/generated/85aabc6a-d9e2-467a-b4c9-cf9c75fae27e/img-eRYeasIO8ywklOpFnwjZ2.jpeg")
   
    st.title("Solar Production Prediction")

    
    df = load_data()

    
    model = train_prophet(df)

   
    forecast = predict_solar_production(model)

  
    forecast_date = st.date_input('Select Date for Prediction', value=pd.to_datetime('2024-12-12'))

  
    forecast_for_date = forecast[forecast['ds'].dt.date == forecast_date]

    
    st.subheader(f"Solar Production Prediction for {forecast_date}")
    fig = px.line(forecast_for_date, x='ds', y='yhat', title='Solar Production Prediction',
                  labels={'ds': 'Date', 'yhat': 'Solar Production (kW)'})
    st.plotly_chart(fig)

   
    st.subheader("Forecast Components (Trend, Yearly, etc.)")
  
    fig_components = model.plot_components(forecast_for_date)
    st.pyplot(fig_components)  

    st.subheader("Full Forecast")
    fig_full_forecast = plot_plotly(model, forecast) 
    st.plotly_chart(fig_full_forecast)  

if __name__ == "__main__":
    app()
