# 🎶 EchoNest - Music Recommender

**EchoNest** is your personal music assistant, helping you discover songs you'll love based on lyrical and audio feature similarities!  
Built with **Python**, **Streamlit**, and **Machine Learning**, this app offers instant, vibe-based song recommendations at your fingertips. 🎧

---

## 🚀 Features
- 🎵 Find songs similar to your favorite track.
- 🦰 Intelligent recommendations based on **lyrics** and **content similarity**.
- ⚡ Fast and interactive web app built using **Streamlit**.
- 📚 Model trained using **TF-IDF** and **Cosine Similarity** on a lyrics dataset.

---

## 🛠 Tech Stack
- **Python** 🐍
- **Pandas**, **NLTK**, **Scikit-learn**
- **Joblib** for model persistence
- **Streamlit** for front-end
- **Cosine Similarity** for recommendation engine

---

## 📂 Project Structure
```
├── src/
│   ├── main.py          # Streamlit app frontend
│   ├── preprocess.py    # Data cleaning, vectorization, saving preprocessed data
│   ├── recommend.py     # Recommendation logic
│   └── spotify_millsongdata.csv  # Raw dataset (sampled from 10000 rows)
├── .gitignore
├── README.md
```

---

## 🦩 How It Works
1. **Preprocessing**: Cleans and vectorizes the lyrics using **TF-IDF**.
2. **Similarity Calculation**: Uses **Cosine Similarity** to find songs closest in lyrical style.
3. **Recommendation**: Displays the top 5 most similar tracks based on user input.

---

## 💾 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/kc1code/EchoNest-Music-Recommender.git
   cd EchoNest-Music-Recommender
   ```

2. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Preprocess the dataset**  
   (This step will create `df_cleaned.pkl` and `cosine_sim.pkl`)
   ```bash
   python src/preprocess.py
   ```

4. **Launch the Streamlit app**
   ```bash
   streamlit run src/main.py
   ```

5. Enjoy music recommendations! 🎶

---

## 📝 Requirements

Create a file called `requirements.txt` with the following content:

```txt
streamlit
pandas
nltk
scikit-learn
joblib
```

(You can generate this automatically by running `pip freeze > requirements.txt`.)

---

## 📸 Screenshot
![App Screenshot](https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?fit=crop&w=1350&q=80)

---

## ⭐ Future Enhancements
- Add genre-based or mood-based filters.
- Integrate Spotify API for real-time music playback.
- Build personalized playlists using ML!

---

## 🙌 Contributing
Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

# 🎧 Keep Vibin' with EchoNest!

