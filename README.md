# 🏆 Football Fixtures Web App

A full-stack web application built with Flask and vanilla JavaScript that displays live and upcoming football fixtures for the Premier League, La Liga, and Serie A. Includes a news ticker, league filters, and modern UI styling.

![Docker Pulls](https://img.shields.io/docker/pulls/yuvalost/football-fixtures-app?style=for-the-badge)

---

## 🧰 Tech Stack

- ⚙️ **Backend**: Python + Flask  
- 🎨 **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (vanilla)  
- 📦 **Containerization**: Docker  
- 🔁 **Automation**: GitHub Actions CI/CD  
- 🔐 **Secrets**: GitHub Actions Encrypted Secrets  
- 📡 **Data Source**: [football-data.org](https://www.football-data.org/)

---

## 📸 Preview

![App Screenshot](preview.png)

---

## 🚀 Features

- Live and upcoming match fixtures
- Search by team name
- Filter by league (Premier League, La Liga, Serie A)
- Pagination / Load more
- Live match indicator (🔴 LIVE)
- News ticker from The Guardian (RSS)
- Responsive design with Bootstrap

---

## 🧪 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yuvalost/Football-Fixtures-Web-App.git
cd Football-Fixtures-Web-App

Create a .env file with your football-data.org API key:
FOOTBALL_API_KEY=your_real_api_key_here

Build the Docker image:
docker build -t yuvalost/football-fixtures-app .
Run the container:
docker run -p 5000:5000 --env-file .env yuvalost/football-fixtures-app

Open http://localhost:5000 in your browser.

📦 Docker Hub
Pull the image:
docker pull yuvalost/football-fixtures-app:latest