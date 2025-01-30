class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret-key'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jgadgaambrosio@gmail.com'
    MAIL_PASSWORD = 'qghu hciv bxbe ynkk'  # Substitua por uma senha real ou App Password
