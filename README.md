<img width="1363" height="761" alt="Screenshot 2026-04-12 005955" src="https://github.com/user-attachments/assets/60b2607f-3c66-460b-9fde-c94f66eaeb8f" /># 🎬 AI Movie Recommendation System
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
<img width="1365" height="727" alt="Screenshot 2026-04-12 005820" src="https://github.com/user-attachments/assets/9b811080-aa47-44a8-9f70-5e4969d5748a" />
<img width="1364" height="755" alt="Screenshot 2026-04-12 005936" src="https://github.com/user-attachments/assets/f7860df1-8096-4db2-835e-1a75098add23" />
<img width="1363" height="761" alt="Screenshot 2026-04-12 005955" src="https://github.com/user-attachments/assets/8882ad96-07b7-4ed8-aa79-8044f5ab8597" />
<img width="1365" height="750" alt="Screenshot 2026-04-12 010352" src="https://github.com/user-attachments/assets/446b457f-b943-4f63-adcd-3ea7d4cf759f" />

## 🧠 Flow Diagram
The system follows a professional Data Science pipeline to turn raw text into insights:

```mermaid
   graph TD
    %% Define NEW STYLES for high visibility in Light Mode
    %% Colors use darker stroke and explicitly black text where possible
    classDef ingestion fill:#e6f7ff,stroke:#105a99,stroke-width:2px,color:black,font-weight:bold;
    classDef engineering fill:#fff7e6,stroke:#b26a0a,stroke-width:1px,color:black;
    classDef coreEngine fill:#f6ffed,stroke:#2d6614,stroke-width:2px,stroke-dasharray: 5 5,color:black,font-weight:bold;
    classDef interface fill:#fff0f6,stroke:#9c125d,stroke-width:2px,color:black;

    subgraph Data_Ingestion [Data Ingestion Pipeline]
        A[Raw Kaggle Dataset 930k TMDB Movies]:::ingestion --> B[Load into Pandas DataFrame]:::ingestion
    end

    subgraph Preprocessing_Pipeline [Data Engineering Pipeline]
        B --> C{Quality Filter: vote_count > 500}:::engineering
        C -- No --> D(Drop Movie):::engineering
        C -- Yes --> E[Merge Metadata: Title + Genre + Overview]:::engineering
        E --> F[Normalize Text: Lowercase & Clean]:::engineering
        F --> G[Save processed_movies.csv]:::engineering
    end

    subgraph ML_Engine [AIML Core Engine]
        G --> H[TF-IDF Vectorization]:::coreEngine
        H --> I[Cosine Similarity Calculation]:::coreEngine
        I --> J[Serialize with Pickle]:::coreEngine
    end

    subgraph Streamlit_UI [User Interface]
        J --> K[Streamlit Web App]:::interface
        L(User Selects Movie) --> K
        K --> M[Load Pickle Files]:::engineering
        M --> N[Retrieve Top 5 Similar Indices]:::coreEngine
        N --> O[Map IDs to TMDB Image Server]:::engineering
        O --> P[Display Posters & Ratings]:::interface
    end<img width="1365" height="727" alt="Screenshot 2026-04-12 005820" src="https://github.com/user-attachments/assets/f2cce9dc-726c-452b-85f0-9a6b8fc59769" />

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

  
