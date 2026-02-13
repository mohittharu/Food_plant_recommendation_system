🌱 Food Plant Recommendation System

A machine learning–powered web application that recommends the most suitable food crop/plant based on soil parameters using a trained Random Forest model.
The application is built with Python, Scikit-learn, and Streamlit.


🚀 Features

🌾 Predicts the most suitable food plant/crop

📊 Provides prediction confidence

🧠 Machine Learning model (Random Forest)

🖥️ Interactive Streamlit web interface

🧪 Trained using real agricultural soil data

📦 Clean and modular project structure


🏗️ Project Structure
Food_Plant_Recommendation_System/
│
├── data/
│   ├── Food_data.csv
│   └── food.ipynb
│
├── src/
│   ├── Classifier/
│   │   ├── Random_forest_v1.joblib
│   │   └── Scaler_1.joblib
│   │
│   ├── main.py              # ML prediction logic
│   └── streamlit_app.py     # Streamlit frontend
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore


⚙️ Tech Stack

Python 3.10+

Scikit-learn

NumPy

Joblib

Streamlit

Pandas (for data processing)


📥 Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Food_Plant_Recommendation_System.git
cd Food_Plant_Recommendation_System

2️⃣ Create a virtual environment (recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application

From the project root:

python -m streamlit run src/streamlit_app.py


Then open your browser at:

http://localhost:8501


🧪 Model Details

Algorithm: Random Forest Classifier

Preprocessing: Standard Scaler

Inputs: Soil and nutrient parameters

Output: Recommended crop + confidence score


📊 Input Parameters

The model expects soil features in a specific order:

pH

Soil EC

Phosphorus

Potassium

TSP (Triple Super Phosphate)

⚠️ Ensure inputs match the training data order for accurate predictions.


📌 Example Output

🌾 Recommended Crop: Rice

🔒 Confidence: 92.45%

🐳 Docker Support (Optional)

Build image:

docker build -t food-plant-recommender .


Run container:

docker run -p 8501:8501 food-plant-recommender

📈 Future Improvements

🌍 Deployment on Streamlit Cloud / Render

📊 Confidence visualization

🧾 Label decoding for crop names

🧠 Model retraining pipeline

🔐 Input validation

📱 Mobile-friendly UI


🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch

Commit your changes

Open a Pull Request


📄 License

This project is licensed under the MIT License.


👨‍💻 Author

Mohit
📌 Machine Learning & Data Science Enthusiast

#LinkedIn
⭐ If you like this project, don’t forget to star the repository!
 LinkedIn :https://www.linkedin.com/in/mohit-chaudhari-343940328/
