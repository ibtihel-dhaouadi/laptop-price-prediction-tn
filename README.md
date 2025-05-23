# 💻 Laptop Price Predictor (🇹🇳)

Welcome to the **Laptop Price Predictor** project! This tool helps you estimate the price of a laptop in Tunisia based on its specifications. Whether you're a buyer curious about market prices or a seller looking for pricing benchmarks, this project is for you.

---

## 🚀 Project Overview

This project includes:

1. **Web Scraping** 🕸️: Automatically gathers laptop data from [BestBuyTunisie.tn](https://www.bestbuytunisie.tn) including brand, CPU, RAM, storage, GPU, screen size, and price.
2. **Data Preprocessing** ⚙️: Clean and prepare data for training
3. **Machine Learning** 🤖: A prediction model (e.g. Linear Regression, Random Forest) trained to estimate laptop prices based on specifications.
4. **Streamlit App** 🌐: A clean and interactive UI so anyone can predict laptop prices easily.
5. **Coming Soon** ⏳: A **Recommendation System** that suggests laptops with similar specs or predicted prices.



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
- Add more Tunisian e-commerce websites for better data diversity
- Develop a content-based recommendation system
- Optimize model for better prediction accuracy
- Deploy using Docker / Cloud Platform (Heroku, AWS, etc.)



## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/ibtihel-dhaouadi/laptop-price-prediction-tn/issues).



## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.



## 📧 Contact
Built with 💙 by **ibtihel**

Feel free to reach out for feedback or collaboration!

---

🔗 [LinkedIn](https://www.linkedin.com/in/ibtihel-dhaouadi/)

📧 ibtihel.dhaouadi98@gmail.com


