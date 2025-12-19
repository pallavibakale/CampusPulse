# CampusPulse

A Django-based web application designed to manage campus activities, events, and student information.

## 📋 Overview

CampusPulse is a comprehensive campus management system built with Django that helps track and manage various aspects of campus life including student information, events, and more.

## 🚀 Features

- **Student Management**: Track and manage student information
- **Event Management**:  Organize and manage campus events
- **User-friendly Interface**: Clean and intuitive web interface
- **Django Admin Integration**: Built-in admin panel for easy management

## 🛠️ Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML/CSS/JavaScript (Static files)
- **Database**: SQLite (default Django setup)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pallavibakale/CampusPulse.git
   cd CampusPulse
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   # Install other dependencies as needed
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Or on Windows, use the batch file:
   ```bash
   getting-to-graduation.bat
   ```

7. **Access the application**
   
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 📁 Project Structure

```
CampusPulse/
├── events/              # Events management app
├── students/            # Students management app
├── getting_to_graduation/  # Main Django project directory
│   ├── common/          # Common utilities
│   ├── templates/       # HTML templates
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL configurations
│   └── wsgi. py          # WSGI configuration
├── static/              # Static files (CSS, JS, images)
├── manage.py            # Django management script
└── test.py              # Test file
```

## 🧪 Running Tests

```bash
python test.py
```

Or use Django's test runner:
```bash
python manage.py test
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Pallavi Bakale**
- GitHub: [@pallavibakale](https://github.com/pallavibakale)

## 📧 Contact

For any questions or feedback, please open an issue on the GitHub repository. 

---

⭐ Star this repository if you find it helpful! 
```
