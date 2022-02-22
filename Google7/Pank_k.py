from Google7.Pank import Konto

paul_konto = Konto("Paul", 100.00)
jakob_konto = Konto("Jakob", 500.00)

print("Algne saldo")
print("Pauli konto arve: " + paul_konto.naita_saldo())  # 100.0
print("Jakobi konto arve: " + jakob_konto.naita_saldo())  # 500.0

jakob_konto.ylekanne(250.00)
print(jakob_konto.naita_saldo())  # Jakobi saldo nüüd on 250.0
paul_konto.deposiit(250.00)
print("Pauli saldos nüüd on {0}".format(paul_konto.naita_saldo()))  # Pauli saldo nüüd on 350.0

print("Lõplik seisund")
print(paul_konto.naita_saldo())  # 350.0
print(jakob_konto.naita_saldo())  # 250.0
