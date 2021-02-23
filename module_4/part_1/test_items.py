from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_language_verification(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    btn = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")))
    string = browser.current_url
    lang = string.split('/')[3]

    if lang == 'ru':
        assert btn.text == 'Добавить в корзину', "Invalid name of button!"
    elif lang == 'fr':
        assert btn.text == 'Ajouter au panier', "Invalid name of button!"
    elif lang == 'en-GB':
        assert btn.text == 'Add to basket', "Invalid name of button!"
    elif lang == 'es':
        assert btn.text == 'Añadir al carrito', "Invalid name of button!"
    else:
        print('invalid language')


