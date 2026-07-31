# 🎬 Movie Search Web Scraper

A modern Flask-based web application that scrapes movie information from a website and provides a fast, searchable interface for users. The application collects movie titles and URLs, stores them in a JSON file, and displays them through a responsive web interface with real-time search functionality.

---

## 📌 Features

* 🔍 Real-time movie search
* 🎥 Automatically scrapes movie titles and links
* 🌐 Flask-powered web interface
* 📱 Responsive UI for desktop and mobile
* ⚡ Lightweight and fast
* 📂 JSON-based data storage
* 🎨 Clean and modern design

---

## 📁 Project Structure

```text
movie-search-web-scraper/
│
├── app.py                  # Flask application
├── scraper.py              # Web scraper script
├── urls.json               # Scraped movie data
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment configuration
├── runtime.txt             # Python version (optional)
│
├── templates/
│   └── index.html          # Web page template
│
├── static/
│   ├── style.css           # Styling
│   └── script.js           # Search functionality
│
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3.11+
* Flask
* Requests
* BeautifulSoup4
* HTML5
* CSS3
* JavaScript

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-search-web-scraper.git
cd movie-search-web-scraper
```

### 2. Create a Virtual Environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Scrape Movie Data

Run the scraper to collect movie titles and URLs.

```bash
python scraper.py
```

This generates the `urls.json` file.

### Step 2: Start the Flask Server

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔍 How It Works

1. The scraper sends an HTTP request to the target website.
2. BeautifulSoup parses the HTML content.
3. Movie titles and links are extracted.
4. The extracted data is stored in `urls.json`.
5. Flask reads the JSON data and displays it.
6. JavaScript enables instant search filtering.

---

## 📦 Requirements

```text
Flask
gunicorn
requests
beautifulsoup4
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## 🌍 Deployment

This project can be deployed for free on:

* Render (Recommended)
* Railway
* PythonAnywhere

For Render:

* Build Command

```bash
pip install -r requirements.txt
```

* Start Command

```bash
gunicorn app:app
```

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```text
screenshots/
├── home-page.png
├── search.png
└── mobile-view.png
```

---

## 🔮 Future Enhancements

* Movie posters
* Pagination
* Genre filters
* Year-wise filtering
* Dark/Light mode
* Favorites list
* Auto-refresh scraper
* Database integration (SQLite/MySQL)
* REST API
* User authentication

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## ⚠️ Disclaimer

This project is created for **educational and learning purposes only**. Ensure that your scraping activities comply with the target website's Terms of Service, robots.txt, and applicable laws.

---

## 👨‍💻 Author

**Sathish Danaveni**

* GitHub: https://github.com/Sathish-911
* LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star this repository
* 🍴 Fork the project
* 🛠️ Contribute improvements
* 📢 Share it with others

Happy Coding! 🚀

