**🎬 AI Movie Recommendation System**
### TMDB Movies Dataset 2024 @kaggle

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📝 Brief Description
This Movie Recommendation System transforms raw TMDB movie data into a rich semantic space where films are connected by meaning, not just metadata. Using advanced NLP techniques, it captures plot nuances, genre overlaps, and thematic depth to deliver highly relevant suggestions—mirroring the intelligent recommendation experience of platforms like Netflix and Amazon Prime, where every choice feels personalized and intuitive.
## 🛠️ Technology Stack

| Component | Technology | Use Case |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core programming and logic |
| **Data Processing** | Pandas & NumPy | Large-scale dataset cleaning and filtering |
| **Machine Learning** | Scikit-Learn | TF-IDF Vectorization and Cosine Similarity |
| **Frontend UI** | Streamlit | Interactive web interface and data rendering |
| **Serialization** | Pickle | Model saving and loading for performance |
| **Data Source** | TMDB (Kaggle) | 1M movie metadata repository |

## 🚀 Key Features
- **Massive Data Handling:** Processes the TMDB 930k+ dataset efficiently using optimized data engineering and filtering.
- **NLP Vectorization:** Utilizes `TF-IDF Vectorization` to convert movie overviews and genres into high-dimensional mathematical vectors.
- **Similarity Engine:** Implements `Cosine Similarity` (Linear Kernel) to calculate the contextual distance between movies.
- **Dynamic UI:** A sleek, dark-themed Streamlit interface featuring high-quality posters, live star ratings, and expandable overviews.

## 🎬 Output Snapshots
<img width="500" height="300" alt="Screenshot 2026-04-12 005820" src="https://github.com/user-attachments/assets/9b811080-aa47-44a8-9f70-5e4969d5748a" />
<img width="500" height="300" alt="Screenshot 2026-04-12 005936" src="https://github.com/user-attachments/assets/f7860df1-8096-4db2-835e-1a75098add23" />
<img width="500" height="300" alt="Screenshot 2026-04-12 005955" src="https://github.com/user-attachments/assets/8882ad96-07b7-4ed8-aa79-8044f5ab8597" />
<img width="500" height="300" alt="Screenshot 2026-04-12 010352" src="https://github.com/user-attachments/assets/446b457f-b943-4f63-adcd-3ea7d4cf759f" />

## 🧠 Flow Diagram
The system follows a professional Data Science pipeline to turn raw text into insights:

```mermaid
   graph TD
    %% Define Clean Styles
    classDef blue fill:#e1f5fe,stroke:#01579b,color:#01579b
    classDef orange fill:#fff3e0,stroke:#e65100,color:#e65100
    classDef green fill:#f1f8e9,stroke:#33691e,color:#33691e
    classDef pink fill:#fce4ec,stroke:#880e4f,color:#880e4f

    subgraph Ingestion [Data Ingestion]
        A[Raw Kaggle Dataset]:::blue --> B[Load Pandas DataFrame]:::blue
    end

    subgraph Engineering [Data Engineering]
        B --> C{Vote Count > 500?}:::orange
        C -->|No| D[Drop Movie]:::orange
        C -->|Yes| E[Merge Metadata Tags]:::orange
        E --> F[Normalize Text]:::orange
        F --> G[Save processed_movies.csv]:::orange
    end

    subgraph AIML [ML Engine]
        G --> H[TF-IDF Vectorization]:::green
        H --> I[Cosine Similarity]:::green
        I --> J[Serialize with Pickle]:::green
    end

    subgraph UI [Frontend]
        J --> K[Streamlit Web App]:::pink
        L(User Selection) --> K
        K --> M[Fetch Similar Movies]:::pink
        M --> N[Map TMDB Posters]:::pink
        N --> O[Display Results]:::pink
    end

```
    
## 🛠️ Installation & Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/movie-recommender.git](https://github.com/YOUR_USERNAME/movie-recommender.git)
   ```

2. **Install Dependencies:**
   ```bash
   pip install pandas scikit-learn streamlit
   ```

3. **Data Preprocessing:**
  ```bash
  python preprocess.py
  ```

4. **Build the Engine:**
  ```bash
  python recommender.py
  ```
  
5. **Launch the App:**
  ```bash
  streamlit run app.py
  ```

  ---

<div align="center">
  <h3>✨ Let's Connect!</h3>
  <p>Exploring the intersection of Big Data, Natural Language Processing, and Software Engineering.</p>
  
  <a href="https://github.com/keshriaman231">
    <img src="https://img.shields.io/badge/GitHub-keshriaman231-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>

  <br/><br/>
  
  *"Transforming a million rows of data into a single perfect recommendation. One vector at a time."* 🚀 **[@aman-space](https://github.com/keshriaman231)**
</div>

  
