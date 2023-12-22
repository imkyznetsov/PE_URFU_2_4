# Определитель спама
![Logotype](./docs/credit-data-quality-campaign.png)

Базируется на ![Logo](https://cdn-lfs.huggingface.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/42378b786aa85e6103abbd2ee24e56672467d562ecf884eb51cefe3a68971087?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo-with-title.png%3B+filename%3D%22hf-logo-with-title.png%22%3B&response-content-type=image%2Fpng&Expires=1703543062&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcwMzU0MzA2Mn19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5odWdnaW5nZmFjZS5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzQyMzc4Yjc4NmFhODVlNjEwM2FiYmQyZWUyNGU1NjY3MjQ2N2Q1NjJlY2Y4ODRlYjUxY2VmZTNhNjg5NzEwODc%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=neOVekNqTrg5V42vPwDzcYSWSfjBFXwEiGiI2IEzK5J7mX2IT3Fcbw6vKYm69mmWCFb8ZhljDDsFw0YUeiC2SiLl99N5lNgM9344I1JV0ALA8IiKsdHIuHmW%7E-4TPP369EVC1Gq9DV2XPRCWLb8u1QaPNpq694-KiJ4qnHKiScqVua6Ukg0T0TX-QtLKhLk%7ET6HPFI2du3%7EMuYN%7E4OjLQiOwMSZrFt0hfc45Y66obMmDlayWPe1A-l5uNynB49HKfiKBYdgvXzMf-85w2Ol%7EQQN2ZoI8-TgLRbYWSr8XVlAECmNwXecqn9BoSnm1ZRlEm-Z2yvPzwgxzZbc7lCS-oQ__&Key-Pair-Id=KVTP0A1DKRTAX)(https://huggingface.co/mshenoda/roberta-spam)

## Начало работы

1. Настройки для локального запуска проекта:
> [!IMPORTANT]
> *Перед началом работы создайте папку на вашем компьютере под управлением ОС Linux, которая будет содержать проект. Для этого выполните следующие команды в Вашем терминале:*
- `$ mkdir folder_name`  *создайте папку в которую вы поместите проект*
- `$ cd folder_name` *перейдите в нее*
- `$ sudo apt-get update` *проверьте наличие обновлений*
- `$ sudo apt install python3-venv` *установите пакет для работы с виртуальным окружением*
- `$ python3 -m venv venv_name` *создайте новое окружение*
- `$ source venv_name/bin/activate` *активируйте новое окружение*
  
2. Загрузка и запуск проекта:
> [!NOTE]
> *Для успешного запуска приложения, пожалуйста, проделайте следующие шаги:*
- `$ git clone git@github.com:ChristopherMcCandless/group_six_project.git` *(создайте клон проекта)*
- `$ pip install -r requirements.txt` *(установите все необходимые библиотеки из файла)*
- `$ streamlit run streamlit_startup.py` *(запустите приложение)*
- Перейдите по адресу: http://10.0.2.15:8501/ в браузере *(если этого не произошло автоматически)*

## Использование

1. Перейдите на главную страницу приложения;
  ![Startupscreen](./docs/startup_screen.png)
2. В поле с надписью "Введите текст" введите соответствующий текст (для примера, можете использовать [готовые тексты](https://read-analytic.ru/textes/))
3. Нажмите "Сформировать конспект"
  > В поле ниже появится сформированный конспект.

## Команда

```
Менеджер проекта, аналитик данных – Кузнецов Иван
Инженер по машинному обучению, Full Stack-разработчик – Казанцев Александр
Тестировщик – Спивак Дмитрий
Документалист/технический писатель – Граб Яков
```

## Лицензия

_Python Software Foundation License_
