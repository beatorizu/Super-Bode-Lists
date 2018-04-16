from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e acidentalmente tenta submeter
        # um item vazio na lista. Ela tecla Enter na caixa de entrada vazia

        # A página inicial é atualizada e há uma mensagem de erro informando
        # que itens da lista não podem estar em branco

        # Eis que ela tenta novamente com um texto para o item, e isso functional_tests

        # De formar pervesa, ela decide submeter um segundo item em
        # branco na listas

        # Ela recebe um aviso semelhante na página da listas

        # Ela pode corrigir isso preenchendo o item com um texto
        self.fail('write me plz!')
