import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Laptop Price Predictor 🇹🇳💻", page_icon="💻", layout="wide")

# Load model and encoder
model = joblib.load('src/Models/xgb_best_tuned_model.joblib')
encoder = joblib.load('src/Models/target_encoder.joblib')

# Load dataset
csv_path = 'data/tunisia_laptop_prices_2025.csv'
df = pd.read_csv(csv_path)
df.drop(['reference','store', 'link', 'name', 'image_url'], axis=1, inplace=True)

# Prepare categorical options
brand_options = sorted(df['brand'].unique())
processor_options = sorted(df['processor'].unique())
gpu_options = sorted(df['gpu'].unique())
os_options = sorted(df['os'].unique())
ram_options = [
    2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 128
]
# Inject CSS to style the button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FFB300;  /* amber/yellow */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        transition: background-color 0.3s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #FFA000;  /* darker amber on hover */
        color: #fff;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Header with subtext
st.markdown("<h1 style='text-align: center;'>💻 Tunisia Laptop Price Predictor 🇹🇳</h1>", unsafe_allow_html=True)
# Optional Info
with st.expander("ℹ️ About this app"):
    st.markdown("""
        - This model is trained using real laptop listings from the Tunisian market (2025).
        - It uses advanced machine learning (XGBoost Regressor) with Target Encoding and Log-Price Transform.
        - Dataset is available on [GitHub](https://github.com/ibtihel-dhaouadi/laptop-price-prediction-tn).
        - Coming soon: a personalized laptop recommendation engine based on your needs! 🔮💡
    """, unsafe_allow_html=True)


# Three-column layout
col1, col2, col3 = st.columns(3)

with col1:
    brand = st.selectbox("🏷️ Brand", brand_options)
    screen_size = st.slider("📏 Screen Size (inches)", 10.0, 20.0, 15.6, 0.1)
    processor = st.selectbox("⚙️ Processor", processor_options)

with col2:
    ram = st.selectbox("💾 RAM (GB)", ram_options)
    SSD = st.number_input("📦 SSD (GB)", min_value=0, max_value=1024, value=256, step=256)
    HDD = st.number_input("🗃️ HDD (GB)", min_value=0, max_value=2048, value=0, step=256)

with col3:
    gpu = st.selectbox("🎮 GPU", gpu_options)
    os = st.selectbox("🖥️ Operating System", os_options)
    gamer = st.radio(
        "🎯 Gaming Laptop?",
        options=[0, 1],
        format_func=lambda x: "Yes 🎮" if x == 1 else "No",
        horizontal=True
    )

st.markdown("<br>", unsafe_allow_html=True)
center_col = st.columns([1, 1, 1])[1]
with center_col:
    if st.button("🚀 Predict Price"):

        # Prepare input
        input_df = pd.DataFrame([{
            'brand': brand,
            'screen_size': screen_size,
            'processor': processor,
            'ram': ram,
            'SSD': SSD,
            'HDD': HDD,
            'gpu': gpu,
            'os': os,
            'gamer': gamer
        }])

        # Encode and predict
        input_encoded = encoder.transform(input_df)
        log_pred = model.predict(input_encoded)
        price_pred = np.expm1(log_pred)[0]

        # Display result
        st.markdown(f"""
            <h3 style='text-align:center;'>💰 Estimated Price: <span style='color:#FFC107;'>{price_pred:,.0f} TND</span></h3>
        """, unsafe_allow_html=True)

        # Interpretation
        if price_pred < 1000:
            st.success("🟢 Budget option — great for daily tasks!")
        elif price_pred < 2500:
            st.info("🟡 Mid-range — balanced for work and play.")
        else:
            st.warning("🔴 High-end device — great for gaming or heavy workloads!")


# --------------------- Footer ---------------------
st.markdown("""
---
<div class='footer'>
    <center>Made with ❤️ by Ibtihel Dhaouadi · 2025</center>
</div>
""", unsafe_allow_html=True)
