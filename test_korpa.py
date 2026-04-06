import pytest

# Ovo je "fixture" - on pravi svežu korpu pre svakog testa
@pytest.fixture
def prazna_korpa():
    return []

# Test 1: Proveravamo da li je korpa stvarno prazna na početku
def test_prazna_korpa(prazna_korpa):
    assert len(prazna_korpa) == 0

# Test 2: Dodajemo predmet i proveravamo broj elemenata
def test_dodavanje_u_korpu(prazna_korpa):
    prazna_korpa.append("Laptop")
    assert len(prazna_korpa) == 1
    assert "Laptop" in prazna_korpa
