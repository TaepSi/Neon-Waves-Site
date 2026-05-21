# Neon-Waves-Site
# 🌊 NEON WAVES — Music Producer Portfolio Site

**Полноценный fullstack-сайт** для музыкального продюсера с живой формой обратной связи, неоновым дизайном и потоковыми анимациями.

Демонстрация навыков: **frontend (HTML/CSS/JS)**, **backend (Flask + SQLite)**, **деплой (GitHub Pages + Render)**.

---

## ✨ Что внутри

### 🎨 Frontend (чистый HTML/CSS/JS, без библиотек)
- **Неоновый киберпанк-дизайн** с тёмной темой
- **Кастомный курсор** с неоновым свечением
- **Анимированные частицы** и плавающие блобы на фоне
- **Параллакс-эффект** при скролле
- **Стеклянные карточки** (glassmorphism) для треков, тура, статистики
- **Визуализатор** (анимированные бары, имитация эквалайзера)
- **Адаптивная вёрстка** под все устройства (включая iPhone SE)
- **Анимации появления** секций при скролле (reveal on scroll)

### ⚙️ Backend (Flask + SQLite)
- **Форма обратной связи** — сохраняет сообщения в базу данных
- **API-эндпоинты:**
  - `POST /send-message` — приём сообщений от формы
  - `GET /messages` — просмотр всех сообщений (JSON)
- **CORS** — разрешены запросы с GitHub Pages
- **Автоинициализация базы** при первом запуске

### ☁️ Деплой
- **Frontend:** GitHub Pages (из папки `/docs`)
- **Backend:** Render (Web Service, Python 3)

---

## 🗂 Структура проекта
Neon-Waves-Site/
├── docs/
│ └── index.html # весь фронтенд (стили, скрипты, вёрстка)
├── app.py # бекенд (Flask + SQLite + CORS)
├── requirements.txt # flask, flask-cors
└── .python-version # 3.13

text

> **Почему всё в одном файле?** Для демонстрации того, что сложный фронтенд можно собрать без фреймворков и сборщиков — чистый HTML/CSS/JS.

---

## 🚀 Как запустить

### Локально
```bash
pip install -r requirements.txt
python app.py
```
Открой docs/index.html в браузере.

Продакшен
GitHub Pages включён для папки /docs

Render подключён к репозиторию, деплоит app.py

📊 Live Demo
Ресурс	URL
Сайт	taepsi.github.io/Neon-Waves-Site/
API (статус)	neon-waves-site.onrender.com
Сообщения	neon-waves-site.onrender.com/messages
🛠 Технологии
https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white
https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white
https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black
https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white
https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white
https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white
https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white
https://img.shields.io/badge/GitHub_Pages-222222?style=flat&logo=github&logoColor=white

🔧 API Reference
POST /send-message
Принимает сообщение из формы обратной связи.

Request:

json
{
  "name": "Имя",
  "email": "email@example.com",
  "message": "Текст сообщения"
}
Response:

json
{
  "success": true
}
GET /messages
Возвращает все сохранённые сообщения.

Response:
```bash
json
[
  {
    "id": 1,
    "name": "Имя",
    "email": "email@example.com",
    "message": "Текст сообщения",
    "created_at": "2026-05-21 12:00"
  }
]
```

📱 Адаптивность
✅ Desktop (1440px+)

✅ Laptop (1024px)

✅ Tablet (768px)

✅ Mobile (375px)

✅ iPhone SE (320px)

Навигация сворачивается в гамбургер-меню на мобильных устройствах.

🎯 Для портфолио
Этот проект демонстрирует:

Умение создавать сложный дизайн без фреймворков

Понимание fullstack-архитектуры (фронтенд + бекенд + база данных)

Навыки деплоя на разные платформы (GitHub Pages + Render)

Работу с CORS и API

Адаптивную вёрстку под все устройства

📞 Контакты разработчика
Kwork: demurgas

© 2026 NEON WAVES. Built with passion, deployed with love.
