# Otus-Python-QA-Final-Project-Ticketland.ru

Финальный проект курса Otus Python QA Engineer

**1. Подготовка к запуску:**

- Установить chromedriver (https://chromedriver.chromium.org)
- Установить необходимые библиотеки (pip3 install -r requirements.txt)

**2. Запуск тестов (pytest)**

- Все тесты (pytest -v tests/)
- Один тест или файл с тестами (pytest -v tests/ -k test_file_name.py)

**3. Запуск тестов (robot)**

- Команда в терминале (robot robottest/)

**4. Сбор и просмотр отчета allure:**

- При запуске тестов передать параметр --alluredir=logs/allure-report
- После прогона тестов выполнить команду (allure serve allure-report)

**5. Прогон pipeline в Jenkins:**

- Создаем в любой директории (не в проекте) JenkinsDockerfile:
```buildoutcfg
FROM jenkins/jenkins:lts
USER root
RUN apt-get update -qq
RUN apt-get install -qqy apt-transport-https ca-certificates \
    curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg \
    | apt-key add -
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable"
RUN apt-get update -qq \
    && apt-get install docker-ce=17.12.1~ce-0~debian -y
```
- В папке с файлом создаем image c jenkins (docker build -t my_jenkins -f JenkinsDockerfile .)
- Запускаем контейнер с image c jenkins (docker run -p 8080:8080 -p 50000:50000 -v 
                                         /var/run/docker.sock:/var/run/docker.sock my_jenkins)
- Открываем jenkins (http://localhost:8080)
- Создаем pipeline, передаем Jenkinsfile

**5. Запуск тестов в docker:**

-  В папке с файлом Dockerfile создаем image c тестами (docker build -t  ticketland_tests -f .)
-  Запускаем тесты в docker (docker run -it ticketland_tests)

**6. Как запустить тесты в разных браузерах:**

Chrome:
pytest -v --browser_name=chrome tests

FireFox:
pytest -v --browser_name=firefox tests

**7. Настройки логгирования:**
pytest -v --log_file=logs/filename, где "filename" - наименование файла, куда запишутся логи
pytest -v ---log_level=INFO, где "INFO" - тип логов, которые будут собраны
