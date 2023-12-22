# Определитель спама

Базируется на [![Open in Streamlit](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg)](https://huggingface.co/mshenoda/roberta-spam)

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
