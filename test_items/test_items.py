import time
from selenium.webdriver.common.by import By

map = {"ru": "Добавить в корзину", "es": "Añadir al carrito", "fr": "Ajouter au panier",
       "cs": "Vložit do košíku", "ar": "أضف الى سلة التسوق", "ca": "Afegeix a la cistella", "da": "Læg i kurv",
       "de": "In Warenkorb legen", "en-gb": "Add to basket", "el": "Προσθήκη στο καλάθι", "fi": "Lisää koriin",
       "it": "Aggiungi al carrello", "ko": "장바구니 담기", "nl": "Voeg aan winkelmand toe", "pl": "Dodaj do koszyka",
       "pt": "Adicionar ao carrinho", "pt-br": "Adicionar à cesta", "ro": "Adauga in cos", "sk": "Pridať do košíka",
       "uk": "Додати в кошик", "zh-cn": "Add to basket"}


def test_language(browser, request):
    browser_name = request.config.getoption("language")

    link = f"http://selenium1py.pythonanywhere.com/{browser_name}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button').text
    assert map.get(browser_name) == button

