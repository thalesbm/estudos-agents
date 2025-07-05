from view.main_view import MainPage
from controller.main_controller import MainController

import logging

logger = logging.getLogger(__name__)

def init():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    logger.info("Bem vindo ao melhor mini agente do mundo")

    question = MainPage.get_user_input()
    
    if question:
        MainController.run(question)


if __name__ == "__main__":
    init()
