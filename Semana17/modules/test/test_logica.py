

from modules.logica.Categorias import Categorias
from modules.logica.Transactions import Transactions

def test_categorie_whit_empty_name():
    # Arrange
    category_name = ""
    categoria = Categorias(category_name)

    # Act
    result, messge = categoria.save_category()

    # Assert
    assert result == False
    assert messge == "Please enter a category name"


def test_categorie_already_exists():
    # Arrange
    category_name = "Otros"
    categoria = Categorias(category_name)

    # Act
    result, messge = categoria.save_category()

    # Assert
    assert result == False
    assert messge == "This category already exists"
    
def test_get_all_categories_returns_full_list():
    # Arrange & Act
    categories = Categorias.get_all_categories()

    # Act
    categories = Categorias.get_all_categories()

    # Assert
    assert len(categories) > 0

def test_transaction_with_empty_title():
    # Arrange
    transaction = Transactions(
        title="",
        idCategory="101",
        amount="45650",
        date="06/08/2023",
        type="1"
    )

    # Act
    result, message = transaction.save_transaction()

    # Assert
    assert result == False
    assert message == "Title cannot be empty"

def test_transaction_with_non_numeric_category_id():
    # Arrange
    transaction = Transactions(
        title="Comidita",
        idCategory="a",
        amount="45650",
        date="06/08/2023",
        type="1"
    )

    # Act
    result, message = transaction.save_transaction()

    # Assert
    assert result == False
    assert message == "Category ID must be a number"
    
def test_transaction_with_non_numeric_amount():
    # Arrange
    transaction = Transactions(
        title="Comidita",
        idCategory="101",
        amount="a",
        date="06/08/2023",
        type="1"
    )

    # Act
    result, message = transaction.save_transaction()

    # Assert
    assert result == False
    assert message == "Amount must be a number"


def test_transaction_with_invalid_date_format():
    # Arrange
    transaction = Transactions(
        title="Comidita",
        idCategory="101",
        amount="100000",
        date="2025-08-11",
        type="1"
    )

    # Act
    result, message = transaction.save_transaction()

    # Assert
    assert result == False
    assert message == "Date must be in format dd/mm/yyyy"

def test_transaction_with_invalid_type():
    # Arrange
    transaction = Transactions(
        title="Comidita",
        idCategory="101",
        amount="100000",
        date="06/08/2023",
        type="3"
    )

    # Act
    result, message = transaction.save_transaction()

    # Assert
    assert result == False
    assert message == "Type must be 1 (Expense) or 2 (Income)"
