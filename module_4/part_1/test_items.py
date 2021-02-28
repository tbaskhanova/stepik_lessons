from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Data
add_to_basket_locator = "button.btn.btn-lg.btn-primary.btn-add-to-basket"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
dict_of_languages = {
    "ru": "Добавить в корзину",
    "fr": "Ajouter au panier",
    "en-GB": "Add to basket",
    "es": "Añadir al carrito"
}


def test_language_verification(browser,language):
    # Arrange
    browser.get(link)

    # Act
    add_to_basket_btn = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, add_to_basket_locator)))

    # Assert
    assert add_to_basket_btn.text == dict_of_languages[language], "Invalid name of button!"




