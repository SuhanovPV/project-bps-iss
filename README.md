<h1 align="center">Проект автоматизации <a href="https://bps-iss.ru">сайта</a> компании БПС</h1>

### Описание:
Было разработано несколько тест-кейсов:
- [x] Проверка перехода через меню к выбранному направлению
- [x] Проверка успешного поиска статей по ключевому слову  
- [x] Проверка поиска статей, поиск результатов не дал
- [x] Проверка заполнения формы регистрации на мероприятие
- [x] Проверка заполнения формы обратной связи

Кейсы реализованы основе шаблона PageObject

## Используемый стек технологий и инструментов

|                        Python                         |                        Pytest                         |                          Selen                          |                        Selenoid                         |                        Git                         |                        Jenkins                         |                        Allure                         |                        Allure TestOps                         |
|:-----------------------------------------------------:|:-----------------------------------------------------:|:-------------------------------------------------------:|:-------------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------------------:|:-----------------------------------------------------:|:-------------------------------------------------------------:|
| <img width="55" height="55" src="source/python.svg"/> | <img width="55" height="55" src="source/pytest.svg"/> | <img width="55" height="55" src="source/selenium.svg"/> | <img width="55" height="55" src="source/selenoid.svg"/> | <img width="55" height="55" src="source/git.svg"/> | <img width="55" height="55" src="source/jenkins.svg"/> | <img width="55" height="55" src="source/allure.svg"/> | <img width="40" height="40" src="source/allure-testops.png"/> |

## Запуск автотестов
### На Jenkins реализован параметризованный запуск тестов:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser_url=${BROWSER_URL} --browser_version=${BROWSER_VERSION}
```
<img width="1200" src="source/jenkins-biuid.png" />

### Тесты выполняются на удаленном браузере благодаря использованию Selenoid
Логин и пароль для доступа к Selenoid хранятся в переменных среды
### Добавлена генерация отчетов на allure а так же интеграция с Allure TestOpt
<img width="1200" src="source/jenkins-artefact.png">

### Allure TestOpt 
#### Suites: Помимо автотестов в добавлены ручные тест-кейс
<img width="1200" src="source/allure-test-ops.png">

#### Дашборд:
<img width="1200" src="source/allure-dashboard.png">

### При выполнении автотестов, для тестов линкуются логи, скриншоты, html-страница и видео прохождения кейса
<img width="1200" src="source/allure-test-case-result-artefacts.png">

##### Пример видео:
<img width="1200" src="source/video.gif">

### Добавлено уведомление о выполнении прохождении тест-кейсов через чат-бота в Telegrm
<img src="source/telegram.png">