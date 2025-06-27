# 💻 Laptop Price Predictor (🇹🇳)

Welcome to the **Laptop Price Predictor** project! 

This project aims to predict laptop prices in Tunisia by analyzing data scraped from multiple popular e-commerce websites. The model **predicts** laptop prices based on various features like brand, specifications, and other attributes. After prediction, it also **recommends** similar laptops with matching features.

Whether you're a buyer curious about market prices or a seller looking for pricing benchmarks, **this project is for you.** 😉✅

---

## 🚀 Project Overview

### 🎯 Objectives

1.  Scrape real laptop data from popular **Tunisian e-commerce websites**.
2.  **Clean and analyze the data (EDA)** to identify key pricing factors.
3.  Prepare data for modeling with **Target Encoding** and **log-transforming the price** for better model performance.
4.  Use **LazyRegressor** to compare models and select the best one **(XGBoost performed best)**.
5.  Train and tune an XGBoost Regressor using grid search and parameter tuning.
6.  Evaluate model performance with **cross-validation** and test metrics.
7.  Develop a **content-based recommendation system** suggesting similar laptops based on features.
8.  Build and deploy a user-friendly **Streamlit web app** for easy price prediction and product recommendations.

### 📊 Data Collection

Laptop data was scraped from several top Tunisian retailers:
- [Mytek](https://www.mytek.tn)
- [Graiet](https://www.graiet.tn)
- [Batam](https://www.batam.com.tn)
- [Agora](https://agora.tn/fr/)
- [Spacenet](https://www.spacenet.tn)
- [Tunisianet](https://www.tunisianet.com.tn/)

The data collected includes various laptop features such as: **Brand**, **Model RAM size**, **Storage type (HDD/SSD)**, **Processor (CPU) type and speed**, **Graphics card (GPU)**, **Screen size**, **Operating System** and **Price**.

## 🛠️ Tech Stack

- **Python 3.10+**
- **Libraries**:
  - `pandas`, `numpy` (data handling)
  - `Matplotlib`, `Seaborn` (visualization)
  - `scikit-learn`, `xgboost`, `lazypredict` (for modeling)
  - `BeautifulSoup`, `requests` (for web scraping)
  - `Streamlit` (for deployment)
- **Deployment**: Streamlit Cloud / local


## 📊 Demo

Try the live app here : **Streamlit Cloud:** [Demo on Streamlit Cloud](https://laptop-price-prediction-tn.streamlit.app/)

How to Use ?
1. Launch the app via Streamlit.
2. Input laptop specifications such as brand, screen size, processor, RAM, storage, GPU, OS, and gaming preference.
3. Click "Predict Price" to get an estimated laptop price.
4. Explore recommended similar laptops with their specs and prices for comparison.

[![App Screenshot](https://github.com/ibtihel-dhaouadi/laptop-price-prediction-tn/blob/main/app%20capture.png)](https://laptop-price-prediction-tn.streamlit.app/) 
## 📦 How to Run Locally (Installation)

```bash
# Clone the repository
git clone https://github.com/ibtihel-dhaouadi/laptop-price-prediction-tn.git
cd laptop-price-predictor-tn

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

```



## 📂 Project Structure
```bash
├── data/                 # Collected dataset (CSV/JSON)
├── notebooks/            # Jupyter notebooks for EDA and model building
├── src/                  # Source code (scrapers, preprocessors, models)
├── app.py                # Streamlit app
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```



## 📌 Future Work
- 🛒 Add more Tunisian e-commerce websites for better data diversity
- 🔁 Automated Daily Scraping to keep the data up to date
- 🧠 Integrate **user reviews and ratings** from sites and social media to improve recommendations
- 🔐 Add authentication and dashboard for vendors



## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/ibtihel-dhaouadi/laptop-price-prediction-tn/issues).



## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.


## 📧 Contact
Built with ❤️ by **ibtihel** (june 2025)

Feel free to reach out for feedback or collaboration!


You can also visit my 🧑‍💻 [GitHub](https://github.com/ibtihel-dhaouadi) profile or 🏆 [Kaggle](https://www.kaggle.com/dhaouadiibtihel98) profile for more projects

