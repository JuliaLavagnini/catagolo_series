# 🎬 Series Catalogue API & Web App

Lightweight Full-Stack application built in Python with **FastAPI**, **SQLite** and **HTML/CSS/JavaScript**, allowing you to register, list, search and remove series through a RESTful API or directly through the integrated web interface.

![Series Catalogue demo](demo/demo.gif)

## 🚀 Project Evolution by Stages

1. **Registration and Validation (`POST /series`)**: Modular structuring of the API and creation of models with **Pydantic** to validate business rules (release year > 1900 and seasons > 0).
2. **Catalogue Listing (`GET /series`)**: Implementation of the full query of all registered series in JSON format.
3. **SQLite Database and Specific Search (`GET /series/{title}`)**: Migration of persistence to **SQLite (`sqlite3`)**, adding *case-insensitive* search by title and HTTP status handling (`201`, `400`, `404`).
4. **Removal and Web Interface (`DELETE /series/{title}` & Front-end)**: Creation of the delete route and development of a pure HTML/JS interface served directly by FastAPI (`FileResponse`) via the `fetch` API.

## 📁 Project Structure

```text
catalogue_series/
├── app/
│   ├── __init__.py       # Python package initialization
│   ├── main.py           # FastAPI configuration, CORS and Front-end route
│   ├── schemas.py        # Pydantic validation models
│   ├── database.py       # SQLite connection and CRUD operations
│   └── routes.py         # API endpoints (/series)
├── frontend/
│   └── index.html        # Web interface (HTML, CSS and JavaScript)
├── .gitignore            # Files ignored by Git (venv, __pycache__, .db)
├── requirements.txt      # Project dependencies
└── README.md             # Repository documentation
```

## 🛠️ Technologies Used

* **Back-end:** Python 3, FastAPI, Pydantic, Uvicorn
* **Database:** SQLite (`sqlite3`)
* **Front-end:** HTML5, CSS3, JavaScript (Fetch API)

## 🧩 System Design

```mermaid
flowchart LR
    U[User] -->|Accesses the page| B[Browser]
    B -->|HTML/CSS/JavaScript| F[frontend/index.html]
    B -->|GET / and Fetch API| A[FastAPI - app/main.py]

    subgraph Back-end
        A --> R[Routes - app/routes.py]
        R --> S[Pydantic Validation - app/schemas.py]
        R --> D[CRUD Operations - app/database.py]
    end

    D -->|SQL| DB[(SQLite - series.db)]
    DB -->|Records| D
    D -->|JSON Data| R
    R -->|HTTP Response| B
```

## 🔄 Workflow

```mermaid
sequenceDiagram
    actor User
    participant Interface as Front-end
    participant API as FastAPI
    participant Validation as Pydantic
    participant Database as SQLite

    User->>Interface: Registers, searches, lists or deletes
    Interface->>API: HTTP Request (GET, POST or DELETE)

    alt POST /series
        API->>Validation: Validates the series data
        Validation-->>API: Valid data
        API->>Database: INSERT
        Database-->>API: Confirmation
        API-->>Interface: 201 + message
    else GET /series
        API->>Database: SELECT all series
        Database-->>API: List of series
        API-->>Interface: 200 + JSON
    else GET /series/{title}
        API->>Database: Search by title
        Database-->>API: Series or empty
        alt Series found
            API-->>Interface: 200 + series
        else Series not found
            API-->>Interface: 404
        end
    else DELETE /series/{title}
        API->>Database: DELETE by title
        Database-->>API: Removed or not found
        alt Series removed
            API-->>Interface: 200 + message
        else Series not found
            API-->>Interface: 404
        end
    end

    Interface->>Interface: Updates the screen
    Interface-->>User: Displays result
```

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JuliaLavagnini/catagolo_series
   cd catalogue-series
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the application:**
   * **Web Interface:** `http://127.0.0.1:8000`
   * **API Documentation (Swagger UI):** `http://localhost:8000/docs`
