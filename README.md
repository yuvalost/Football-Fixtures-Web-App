# 🏆 Football Fixtures App

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Docker](https://img.shields.io/badge/docker-ready-blue)

A modern football fixtures web application that displays upcoming matches from major leagues (Premier League, La Liga, Serie A), with live status, league filters, team search, and real-time news ticker.

> Built with **Flask**, **HTML/JS**, and **Bootstrap 5** — containerized with **Docker**, and fetches data from football APIs.

---

## 🌍 Features

- 🔍 Search bar by team name
- 🎯 Filter fixtures by league
- 🔄 Load more fixtures (pagination)
- 🟢 "LIVE" badge for active matches
- 📅 Tooltip with matchday and stadium
- 📰 Real-time football news ticker (Guardian RSS)
- 🎨 Responsive & modern UI with light gradient background
- 🐳 Full Docker support for local or cloud deployment

---

## 📸 Preview

![App Screenshot](./static/preview.png) <!-- You can upload a screenshot to static/preview.png -->

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yuvalost/football-fixtures-app.git
cd football-fixtures-app

Language	Python 3, JavaScript
Framework	Flask (Backend)
Frontend	HTML5, Bootstrap 5, Vanilla JS
API Source	Football-Data.org (fixtures)
The Guardian RSS (news)
Proxy	AllOrigins (to bypass CORS for RSS)
Web Server	gunicorn (in Docker)
Container	Docker, Docker Hub
Development	VS Code, Git
Deployment	Docker CLI / optional Render, Railway, etc.