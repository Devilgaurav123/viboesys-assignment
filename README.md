# ViboSys Project

ViboSys is a FastAPI-based project that integrates MySQL for database management. This project leverages SQLAlchemy for ORM and aims to build a robust and scalable backend.

## Project Status

🚧 **Work in Progress** 🚧

Hey there! Just a heads-up – this project isn't fully completed yet. We're actively working on enhancing features and ironing out some bugs. Stay tuned for updates!

## Technologies Used

- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/vibosys.git
   ```
2. Navigate to the project directory:
   ```bash
   cd vibosys
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Database Configuration

Ensure your MySQL server is running and update the `SQLALCHEMY_DATABASE_URL` in `db.py`:
```python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:<your_password>@localhost/vibeosys_db"
```

## Facing Issues?

If you encounter the `Access is denied` error when starting MySQL, try running your terminal as an administrator:
```bash
net start MySQL80
```

## Next Steps

- Complete the API endpoints
- Implement authentication
- Add frontend integration

Stay tuned for more updates! 😊
