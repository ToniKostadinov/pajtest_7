import pytest

# Funkcija koju testiramo
def je_paran(broj):
    return broj % 2 == 0

# Magija: Testiramo 4 različita slučaja odjednom!
@pytest.mark.parametrize("broj, ocekivani_rezultat", [
    (2, True),   # Paran broj
    (4, True),   # Paran broj
    (7, False),  # Neparan broj
    (0, True),   # Nula je parna
])
def test_je_paran_visestruko(broj, ocekivani_rezultat):
    assert je_paran(broj) == ocekivani_rezultat
