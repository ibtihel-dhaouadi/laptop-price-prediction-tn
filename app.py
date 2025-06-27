import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Laptop Price Predictor 🇹🇳💻", page_icon="💻", layout="wide")

# Load models and encoder
xgb_model = joblib.load('src/Models/xgb_best_tuned_model.joblib') 
knn_model =  joblib.load('src/Models/knn_recommendation_model.joblib') 
encoder = joblib.load('src/Models/target_encoder.joblib')
recommendation_encoder = joblib.load('src/Models/target_encoder_recommendation.joblib')
feature_matrix = np.load('src/Models/feature_matrix.npy')

store_logos = {
    'Mytek': 'https://mk-media.mytek.tn/media/logo/stores/1/LOGO-MYTEK-176PX-INVERSE.png',
    'Batam': 'https://batam.com.tn/static/version1749717782/frontend/Batam/modern-ecommerce/fr_FR/images/logo.svg',
    'agora': 'https://agora.tn/fr/img/logo-1701742001.jpg',
    'tunisianet': 'https://www.tunisianet.com.tn/img/tunisianet-logo-1611064619.jpg',
    'SpaceNet': 'https://spacenet.tn/img/logo-footer.svg',
    'graiet': 'https://www.keejob.com/media/recruiter/recruiter_31647/logo-31647-20250128-085805.png',
}

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
st.markdown("<h1 style='text-align: center;'>💻 Laptop Price Predictor & Recommender 🇹🇳</h1>", unsafe_allow_html=True)

# Updated Info
with st.expander("ℹ️ About this app"):
    st.markdown("""
        - **Price Prediction**: Get instant estimates for laptops using real listings from the Tunisian market (2025) and a powerful **XGBoost model** with Target Encoding and Log-Price transformation.

        - **Laptop Recommendations**: Discover similar laptops tailored to your input with a **content-based KNN** recommendation system.

        - **Trained on real data** with over 2,000 laptop listings.

        - Dataset available on [GitHub](https://github.com/ibtihel-dhaouadi/laptop-price-prediction-tn).
                
        <br>

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
# Prediction button and price in center column of a 3-column layout
_, center_col, _ = st.columns([1, 1, 1])  # three equal columns, use only center

with center_col:
    if st.button("🚀 Predict Price"):

        # Prepare input and predict (your existing code) ...
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

        input_encoded = encoder.transform(input_df)
        log_pred = xgb_model.predict(input_encoded)
        price_pred = np.expm1(log_pred)[0]

        # Display result centered inside center_col (using markdown with center text)
        st.markdown(f"""
            <h3 style='text-align:center;'>💰 Estimated Price: <span style='color:#FFC107;'>{price_pred:,.0f} TND</span></h3>
        """, unsafe_allow_html=True)

        # Interpretation messages
        if price_pred < 1000:
            st.success("🟢 Budget option — great for daily tasks!")
        elif price_pred < 2500:
            st.info("🟡 Mid-range — balanced for work and play.")
        else:
            st.warning("🔴 High-end device — great for gaming!")


# Recommendations section - full width
st.markdown("<h4 '>🔎 Similar Laptops You May Like</h4>", unsafe_allow_html=True)

# Load full dataset with all metadata
full_df = pd.read_csv(csv_path)
full_df = full_df.drop_duplicates(subset=['store','brand', 'screen_size', 'processor', 'ram', 'SSD', 'HDD', 'gpu', 'os', 'gamer', 'price'])

# Prepare input for KNN (add predicted price) - check if price_pred exists (predict button clicked)
try:
    input_for_knn = input_df.copy()
    input_for_knn['price'] = price_pred  # Use latest predicted price
    input_vector = recommendation_encoder.transform(input_for_knn).values

    distances, indices = knn_model.kneighbors(input_vector, n_neighbors=6)
    similar_laptops = full_df.iloc[indices[0][1:]]

    card_columns = st.columns(5)
    default_logo_url = 'https://via.placeholder.com/60?text=No+Logo'

    for i, (_, row) in enumerate(similar_laptops.iterrows()):
        logo_url = store_logos.get(row['store'], default_logo_url)
        with card_columns[i]:
            st.markdown(f"""
                <style>
                .card {{
                    background-color: white;
                    color: black;
                    border-radius: 12px;
                    padding: 0;
                    box-shadow: 0 1px 4px rgba(0,0,0,0.1);
                    transition: box-shadow 0.3s ease;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    text-align: center;
                    overflow: hidden;
                    position: relative;
                    height: 360px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    margin-top: 20px;
                }}
                .card:hover {{
                    box-shadow: 0 -6px 12px rgba(255, 111, 0, 0.3);
                    transform: scale(1.06);
                }}
                .card-img {{
                    height: 100%;
                    overflow: hidden;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background-color: #f9f9f9;
                }}
                .card-img img {{
                    width:  140px;
                    height: 100%;
                    object-fit: cover;
                    transition: transform 0.3s ease;
                }}
               
                .card-body {{
                    padding: 10px 12px;
                    flex-grow: 1;
                    position: relative;
                }}
                .card-title {{
                    font-size: 14px;
                    font-weight: bold;
                    margin-bottom: 5px;
                    min-height: 34px;
                }}
                .store-logo {{
                    height: 40px;
                    position: absolute;
                    top: -130px;
                    right: 10px;
                    border-radius: 6px;
                    object-fit: contain;
                    box-shadow: 0 0 5px rgba(0,0,0,0.1);
                    background-color: hsla(50, 33%, 25%, 0.75);
                }}
                .specs {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 4px 8px;
                    font-size: 12px;
                    color: #333;
                    text-align: left;
                    margin-top: 6px;
                    margin-bottom: 8px;
                }}
                .card-footer {{
                    background-color: #FF7043;
                    color: white;
                    padding: 8px 0;
                    font-weight: bold;
                    font-size: 15px;
                }}
                a.card-link {{
                    text-decoration: none;
                }}
                </style>

                <a href="{row['link']}" class="card-link" target="_blank">
                    <div class="card">
                        <div class="card-img">
                            <img 
                                src="{row['image_url']}" 
                                onerror="this.onerror=null;this.src='https://via.placeholder.com/300x140?text=No+Image';"
                                alt="Laptop Image">
                        </div>
                        <div class="card-body">
                            <div class="card-title">{row['name'][:20] + '...' if len(row['name']) > 20 else row['name']}</div>
                            <img src="{logo_url}" alt="{row['store']} Logo" class="store-logo" />
                            <div class='badge-type {"gaming" if row["gamer"] == 1 else "work"}'>
                                {"🎮 Gaming Laptop" if row["gamer"] == 1 else "📚 Work / Study Laptop"}
                            </div>
                            <div class="specs">
                                <div>🖥️ {row['screen_size']}"</div>
                                <div>💻 {row['os']}"</div>
                                <div>⚙️ {row['processor']}</div>
                                <div>📦 {row['SSD']} GB SSD</div>
                                <div>💾 {row['ram']} GB RAM</div>
                                <div>🗃️ {row['HDD']} GB HDD</div>
                            </div>
                            <div style="font-size: 12px;">🎲 {row['gpu'][:20] + '...' if len(row['gpu']) > 20 else row['gpu']}</div>
                        </div>
                        <div class="card-footer">
                            {row['price']:,.0f} TND
                        </div>
                    </div>
                </a>
            """, unsafe_allow_html=True)





 
except NameError:
    # price_pred not defined because predict button not clicked yet
    st.info("Please predict a price first to see recommendations.")



# --------------------- Footer ---------------------
st.markdown("""
---
<div class='footer'>
    <center>Made with ❤️ by Ibtihel Dhaouadi · 2025</center>
</div>
""", unsafe_allow_html=True)
