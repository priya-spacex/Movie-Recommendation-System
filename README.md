# 🎬 AI Movie Recommendation System
### TMDB Movies Dataset 2024 @kaggle

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📝 Brief Description
This project is a high-performance **Content-Based Recommendation Engine** designed to handle large-scale datasets (930k+ records). It transforms unstructured text data into a searchable mathematical space, allowing users to discover movies similar to their favorites based on plot complexity, genre relationships, and thematic elements. By utilizing advanced NLP techniques, the system mimics the recommendation logic used by industry leaders like Netflix and Amazon.

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


  

## 🧠 Flow Diagram
The system follows a professional Data Science pipeline to turn raw text into insights:

    graph TD
    %% Define styles for professional look
    classDef data fill:#e6f7ff,stroke:#1890ff,stroke-width:2px;
    classDef process fill:#fff7e6,stroke:#ffa940,stroke-width:1px;
    classDef core fill:#f6ffed,stroke:#52c41a,stroke-width:2px,stroke-dasharray: 5 5;
    classDef ui fill:#fff0f6,stroke:#eb2f96,stroke-width:2px;

    %% Data Ingestion
    subgraph Data_Ingestion [Data Ingestion]
        A[Raw Kaggle Dataset <br/> 930k+ TMDB Movies CSV]:::data --> B[Load into Pandas DataFrame]:::process
    end

    %% Preprocessing (preprocess.py)
    subgraph Preprocessing_Pipeline [Data Engineering Pipeline]
        B --> C{Quality Filter: <br/> vote_count > 500}:::process
        C -- No --> D(Drop Movie):::data
        C -- Yes --> E[Merge Metadata: <br/> Title + Genre + Overview = 'Tags']:::process
        E --> F[Normalize Text: <br/> Lowercase & Clean]:::process
        F --> G[Save processed_movies.csv <br/> 10k-15k Popular Movies]:::data
    end

    %% Recommender Engine (recommender.py)
    subgraph ML_Engine [AIML Core Engine]
        G --> H[TF-IDF Vectorization <br/> Convert tags to sparse matrix]:::core
        H --> I[Cosine Similarity Calculation <br/> Generate movie-to-movie scores]:::core
        I --> J[Serialize with Pickle <br/> Save similarity.pkl & movie_list.pkl]:::data
    end

    %% Frontend (app.py)
    subgraph Streamlit_UI [User Interface & Rendering]
        J --> K[Streamlit Web App]:::ui
        L(User Selects Movie) --> K
        K --> M[Fetch Pickle Files <br/> Instant Load Cached Model]:::process
        M --> N[Retrieve Top 5 Similar Indices]:::core
        N --> O[Map IDs to TMDB Public <br/> Image Server]:::process
        O --> P[Display Posters, Ratings, <br/> & Overviews in Grid]:::ui
    end

    
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

  
