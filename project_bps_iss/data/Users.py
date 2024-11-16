import dataclasses


@dataclasses.dataclass
class User:
    name: str
    email: str
    phone: str
    company: str
    industry: str
    personal_count: str
    city: str
    job: str
    goal: str
    corp_email: str
    corp_site: str


test_person = User(
    name='Павел Викторович Суханов',
    email='pavel@mail.ru',
    phone='+790999999999',
    company='MyCompany',
    industry='Энергетика',
    personal_count='101-500',
    city='Санкт-Петербург',
    job='qa engineer',
    goal='Выполнить тестовое задание\nдля сдачи домашней работы в qa guru',
    corp_email='mycompany@mail.ru',
    corp_site='mycompany.ru'
)
