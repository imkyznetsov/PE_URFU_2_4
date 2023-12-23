# Определитель спама

Базируется на модели **mshenoda/roberta-spam**: [![Open model](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg)](https://huggingface.co/mshenoda/roberta-spam)

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
- `$ git clone git@github.com:imkyznetsov/PE_URFU_2_4` *(создайте клон проекта)*
- `$ pip install -r requirements.txt` *(установите все необходимые библиотеки из файла)*
- `$ uvicorn main:app` *(запустите приложение)*
 ```
На новой вкладке введите последовательно:
  curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Only this evening, and only now you can hear this bell"
}'
 ```

> В поле ниже появится результат отработки модели определения спама, где LABEL_0 - спама нет, LABEL_1 - спам есть.

## Тесты
В репозитории настроены средства Continious Integration (**CI**) с помощью Github Actions:
![image](https://github.com/imkyznetsov/PE_URFU_2_4/assets/149815971/30e5cb36-b7cf-436d-9ff6-d7f75ea2082d)

## Выполнил

```
Менеджер проекта, Full Stack-разработчик, аналитик данных, тестировщик и документалист – Кузнецов Иван

```

## Лицензия

_Python Software Foundation License_
