# 💻 Laptop Price Predictor (🇹🇳)

Welcome to the **Laptop Price Predictor** project! 

This project aims to predict laptop prices in Tunisia by analyzing data scraped from multiple popular e-commerce websites. The model **predicts** laptop prices based on various features like brand, specifications, and other attributes. After prediction, it also **recommends** similar laptops with matching features.

Whether you're a buyer curious about market prices or a seller looking for pricing benchmarks, **this project is for you.** 😉✅

---

## 🚀 Project Overview

### 🎯 Objectives

1.  Scrape real laptop data from popular Tunisian e-commerce websites.
2.  **Clean and analyze the data (EDA)** to understand key pricing factors.
3.  Build a machine learning model **(Random Forest Regressor, XGBoost Regression)** to predict laptop prices.
4.  Evaluate the model using **cross-validation** techniques.
5.  Develop an **Advanced recommendation system** to suggest similar laptops.
6.  Deploy the application via **Streamlit** for easy user access.

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
  - `scikit-learn`, `xgboost` (for modeling)
  - `BeautifulSoup`, `requests` (for web scraping)
  - `Streamlit` (for deployment)
- **Deployment**: Streamlit Cloud / local


## 📊 Demo

🚧 Deployment link will be shared here when live.

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
Built with 💙 by **ibtihel** Data Science & Machine Learning Enthusiast

Feel free to reach out for feedback or collaboration!


🔗 [LinkedIn](https://www.linkedin.com/in/ibtihel-dhaouadi/) | 📧 ibtihel.dhaouadi98@gmail.com

---
