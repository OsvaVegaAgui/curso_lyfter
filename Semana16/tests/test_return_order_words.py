from my_module.return_order_words import get_text

def test_return_order_words_with_one_word():
    #Arrange
    text = "python"
    
    #Act
    result = get_text(text)
    
    #Assert
    assert result == "python"
    
def test_return_order_words_with_same_first_letter():
    #Arrange
    text = "carro-casa-camino-comida"
    
    #Act
    result = get_text(text)
    
    #Assert
    assert result == "camino-carro-casa-comida"


def test_return_order_words_with_empty_word():
    #Arrange
    text = ""
    
    #Act
    result = get_text(text)
    
    #Assert
    assert result == ""