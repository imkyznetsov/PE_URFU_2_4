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
- `$ git clone git@github.com:imkyznetsov/PE_URFU_2_4.git` *(создайте клон проекта)*
- `$ pip install streamlit` *(установите Streamlit)*
- `$ streamlit run image_classification.py` *(запустите приложение)*
- Перейдите по адресу: http://10.0.2.15:8501/ в браузере *(если этого не произошло автоматически)*
