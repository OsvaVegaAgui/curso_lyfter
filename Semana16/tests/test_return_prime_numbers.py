from my_module.return_prime_numbers import get_prime_numbers

def test_return_prime_numbers_only_primes():
    
    #Arrange
    lista = lista = [101, 71, 97, 83, 67, 113, 79, 89, 107, 61]
    
    #Act
    result = get_prime_numbers(lista)
    
    #Assert
    assert result == [101, 71, 97, 83, 67, 113, 79, 89, 107, 61]
    
    
def test_return_prime_numbers_none_primes():
    
    #Arrange
    lista = [15, 4, 25, 9, 21, 6, 12, 10, 8, 14]
    
    #Act
    result = get_prime_numbers(lista)
    
    #Assert
    assert result == []


def test_return_prime_numbers_mix_list():
    
    #Arrange
    lista = [1009, 1024, 1013, 1050, 1021, 1081, 1019, 1025, 1003, 1031, 1007, 1040, 1033, 1065, 1011, 1039, 1051, 1005, 1001, 1049]
    
    #Act
    result = get_prime_numbers(lista)
    
    #Assert
    assert result == [1009, 1013, 1021, 1019, 1031, 1033, 1039, 1051, 1049]

