from unittest.mock import patch
from prognoza import nabavi_temperaturu

# 'patch' presreće 'requests.get' unutar fajla 'prognoza'
@patch('prognoza.requests.get')
def test_nabavi_temperaturu(mock_get):
    # 1. Definišemo šta lažni 'get' treba da vrati
    mock_get.return_value.json.return_value = {"temp": 25}
    
    # 2. Pozivamo našu funkciju (ona misli da zove pravi internet)
    rezultat = nabavi_temperaturu("Beograd")
    
    # 3. Proveravamo rezultat
    assert rezultat == 25
    
    # 4. DODATNA MOĆ: Proveravamo da li je naš kod uopšte pozvao pravi URL
    mock_get.assert_called_once_with("https://vreme.com/Beograd")
