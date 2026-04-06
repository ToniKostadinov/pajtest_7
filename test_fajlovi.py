def zapisi_poruku(putanja, poruka):
    with open(putanja, "w") as f:
        f.write(poruka)

def test_pisanje_u_fajl(tmp_path):
    # 1. Pytest pravi privremeni folder samo za ovaj test
    d = tmp_path / "podaci"
    d.mkdir()
    fajl_putanja = d / "poruka.txt"
    
    # 2. Pozivamo našu funkciju
    zapisi_poruku(fajl_putanja, "Zdravo iz testa!")
    
    # 3. Proveravamo da li fajl postoji i šta piše u njemu
    assert fajl_putanja.exists()
    assert fajl_putanja.read_text() == "Zdravo iz testa!"
