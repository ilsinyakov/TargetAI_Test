import os

import allure
from faker import Faker
from playwright.sync_api import Page

from config import LOGIN_URL
from pages.agents_page import AgentsPage
from pages.login_page import LoginPage


def test_add_agent(page: Page) -> None:
    fake = Faker("ru_RU")
    human_name = fake.name()
    agent_name = Faker().user_name()
    instruction = "Автоматизированный агент для тестирования функционала добавления."

    with allure.step("Открыть страницу логина"):
        page.goto(LOGIN_URL)
    login_page = LoginPage(page)
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    assert login is not None and password is not None, "LOGIN and PASSWORD must be set"
    with allure.step("Выполнить логин"):
        login_page.login(login, password)
        allure.attach(page.screenshot(), name="login", attachment_type=allure.attachment_type.PNG)

    agents_page = AgentsPage(page)
    with allure.step("Открыть меню 'Агенты'"):
        agents_page.open_agents_menu()
    with allure.step("Добавить нового агента"):
        agents_page.add_agent(human_name, agent_name, instruction)
        allure.attach(page.screenshot(), name="add_agent", attachment_type=allure.attachment_type.PNG)
    with allure.step("Проверить, что агент появился в списке"):
        agents_page.open_agents_menu()
        assert agents_page.is_agent_in_list(human_name)
        allure.attach(page.screenshot(), name="agent_in_list", attachment_type=allure.attachment_type.PNG)
