class AgentsLocators:
    AGENTS_MENU = "text=Агенты"
    ADD_AGENT_BUTTON = 'button:has-text("Создать агента")'
    ADD_AGENT_MENU = "text=Добавить агенты"
    HUMAN_NAME_INPUT = 'input[value="Новый агент"]'
    AGENT_NAME_INPUT = 'input[value="new_agent"]'
    INSTRUCTION_INPUT = 'p[data-placeholder="Введите текст"]'
    SAVE_BUTTON = 'button[data-testid="save-button"]'
    AGENT_LIST = "div.agent-list"
    AGENT_LIST_ITEM = 'div[data-testid^="agent-table-row"]'
    SUCCESS_TOAST = 'text="Агент успешно создан"'
