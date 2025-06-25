from locators.agents_locators import AgentsLocators
from pages.base_page import BasePage


class AgentsPage(BasePage):
    def open_agents_menu(self) -> None:
        self.page.click(AgentsLocators.AGENTS_MENU)

    def add_agent(self, human_name: str, agent_name: str, instruction: str) -> None:
        self.page.click(AgentsLocators.ADD_AGENT_BUTTON)
        self.page.wait_for_selector(AgentsLocators.HUMAN_NAME_INPUT)
        self.page.fill(AgentsLocators.HUMAN_NAME_INPUT, human_name)
        self.page.fill(AgentsLocators.AGENT_NAME_INPUT, agent_name)
        self.page.fill(AgentsLocators.INSTRUCTION_INPUT, instruction)
        self.page.click(AgentsLocators.SAVE_BUTTON)
        self.page.wait_for_selector(AgentsLocators.SUCCESS_TOAST)

    def is_agent_in_list(self, human_name: str) -> bool:
        self.page.wait_for_selector(AgentsLocators.AGENT_LIST_ITEM)
        return self.page.is_visible(f'text="{human_name}"')
