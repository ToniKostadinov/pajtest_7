import psutil
import time
import os
import pytest
import logging

# 1. Funkcija koju testiramo
def teska_operacija():
    # Simuliramo rad: milion kvadriranja (troši CPU i RAM)
    lista = [i ** 2 for i in range(10**6)]
    time.sleep(0.5)  # Mala pauza radi stabilnosti benchmark-a
    return sum(lista)

# 2. Test funkcija sa fixture-ima:
# 'caplog' za logovanje u izveštaj
# 'benchmark' za automatsko merenje i grafikone
def test_meri_performanse(caplog, benchmark):
    # Postavljamo nivo logovanja da bi se INFO poruke videle u HTML-u
    caplog.set_level(logging.INFO)
    
    # Uzimamo referencu na trenutni proces za merenje RAM-a
    proces = psutil.Process(os.getpid())
    
    # --- DEO ZA BENCHMARK (VREME I HISTOGRAM) ---
    # Benchmark će pokrenuti 'teska_operacija' više puta i izvući prosek
    start_vreme = time.perf_counter()
    rezultat = benchmark(teska_operacija)
    kraj_vreme = time.perf_counter()
    
    trajanje = kraj_vreme - start_vreme
    
    # --- DEO ZA RESURSE (MEMORIJA I CPU) ---
    memorija = proces.memory_info().rss / (1024 * 1024)  # MB
    cpu_procenat = proces.cpu_percent(interval=0.1)
    
    # Logovanje rezultata koji će biti vidljivi u "Captured log call"
    logging.info(f"--- DETALJI PERFORMANSI ---")
    logging.info(f"Izmereno trajanje (zadnji krug): {trajanje:.4f} s")
    logging.info(f"Potrošnja memorije: {memorija:.2f} MB")
    logging.info(f"CPU opterećenje: {cpu_procenat}%")
    logging.info(f"Suma rezultata: {rezultat}")

    # --- PROVERE (ASSERTIONS) ---
    # Test pada ako memorija pređe 200 MB
    assert memorija < 200.0, f"Prevelika potrošnja RAM-a: {memorija:.2f}MB"
    
    # Test pada ako je pojedinačno izvršavanje predugo (npr. > 2s)
    assert trajanje < 12.0, f"Aplikacija prespora: {trajanje:.2f}s"

# Main blok za direktno pokretanje (bez benchmark fixture-a)
if __name__ == "__main__":
    print("Pokretanje skripte direktno... (Benchmark grafikon se generiše samo preko pytest-a)")
    # Za direktno pokretanje moramo proslediti None za fixture-e
    # Ali preporuka je isključivo: pytest test_monitor.py
    try:
        test_meri_performanse(None, lambda f: f())
    except Exception as e:
        print(f"Za puni izveštaj koristi komandu: pytest {os.path.basename(__file__)}")

