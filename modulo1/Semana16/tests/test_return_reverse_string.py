from my_module.return_reverse_string import get_text

def test_return_reverse_string_with_special_characters():
    #Arrange
    text = "¡Año de celebración!"
    
    #Act
    result = get_text(text)
    
    #Assert
    assert result == "!nóicarbelec ed oñA¡"

def test_return_reverse_string_with_one_word():
    #Arrange
    text = "Pizza"
    
    #Act
    result = get_text(text)
    
    #Assert
    assert result == "azziP"
    
def test_return_reverse_string_with_long_text():
    #Arrange
    text = "San Carlos un canton situado en la vibrante Zona Norte de Costa Rica es un paraiso de riqueza natural y prosperidad agricola"
    
    #Act
    result = get_text(text)
    
    #Assert
    assert result == "alocirga dadirepsorp y larutan azeuqir ed osiarap nu se aciR atsoC ed etroN anoZ etnarbiv al ne odautis notnac nu solraC naS"

