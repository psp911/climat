# climat
weather monitoring and managment

Подготовка погодной станции на Raspberry Pi 3
Используются DHT_22 две штуки
/Скоро - датчик давления/

1. Установить Python3 на Raspberry Pi 3 (подготовить систему для использования датчиков)
2. Подключить датчики
3. Подготовить базу данных для подключения: завести пользователя и дать ему права
4. Добавить climat_to_db.py в Cron: Crontab -e 
В базу данных будут заливаться данные новые данные с периодом, указанным в Cron

Далее готовится сайт с данными из таблицы
