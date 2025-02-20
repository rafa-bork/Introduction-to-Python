from dataclasses import dataclass

@dataclass
class Plant:
    species: str

@dataclass
class Tray:
    tray_id: int
    species: str
    number_of_plants: int

    def remove_plants(self, number: int, nursery: 'Nursery'):
        number = min(number, self.number_of_plants)  # Garante que não remova mais do que o disponível
        self.number_of_plants -= number
        nursery.transfer_to_pots(number, self.species)  # Chama o método na instância de Nursery
        return self

    def __repr__(self):
        return f"Tray(tray_id={self.tray_id}, species={self.species}, count={self.number_of_plants})"

@dataclass
class Pot:
    pot_id: int
    species: str

class Nursery:
    def __init__(self):
        self.trays = []
        self.pots = []

    @property
    def number_trays(self):
        return len(self.trays)

    @property
    def number_pots(self):
        return len(self.pots)

    def add_tray(self, tray: Tray):
        self.trays.append(tray)

    def remove_plants(self, tray_id, number):
        # Localiza a bandeja correspondente pelo tray_id
        tray = next((t for t in self.trays if t.tray_id == tray_id), None)
        if not tray:
            raise ValueError(f"Tray with ID {tray_id} not found.")
        tray.remove_plants(number, self)

    def transfer_to_pots(self, number, species):
        for _ in range(number):
            pot_id = self.number_pots + 1  # Gera um ID único para cada pote
            self.pots.append(Pot(pot_id=pot_id, species=species))

    def __str__(self):
        trays_info = "\n".join(str(tray) for tray in self.trays)
        pots_info = "\n".join(str(pot) for pot in self.pots)
        return f"Nursery:\nTrays:\n{trays_info}\n\nPots:\n{pots_info}"

# Exemplo de uso
nursery = Nursery()

# Adiciona bandejas ao berçário
nursery.add_tray(Tray(1, "Lily", 28))
nursery.add_tray(Tray(2, "Rose", 13))

# Remove plantas das bandejas
nursery.remove_plants(1, 10)  # Remove 10 plantas da bandeja com ID 1
nursery.remove_plants(2, 5)   # Remove 5 plantas da bandeja com ID 2

# Imprime o estado do berçário
print(nursery)
