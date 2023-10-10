from flask import Flask, request
from datetime import date
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
  
  # Повертаємо поточний час
  return f'<h>Current time: {time_str}</h>'

  
