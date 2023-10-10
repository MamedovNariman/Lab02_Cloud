import json
from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')

def curent_time():
  # Отримуємо поточний час
  current_time = datetime.now()
  
  # Отримуємо години та хвилини з поточного часу
  current_hour = current_time.hour
  current_minute = current_time.minute
  
  # Створюємо рядок з годинами та хвилинами у форматі "гг:хх"
  time_str = f"{current_hour:02d}:{current_minute:02d}"
  
  # Створюємо словник для JSON
  time_data = {
    'statusCode': 200,
    'body': f'Поточний час: {time_str}'
  }

  # Повертаємо JSON-рядок
  return time_data
