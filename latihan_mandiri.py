from abc import ABC, abstractmethod

class Mahasiswa:
    def __init__(self, nama, sks_diambil, lulus_prasyarat):
        self.nama = nama
        self.sks_diambil = sks_diambil
        self.lulus_prasyarat = lulus_prasyarat

class IValidationRule(ABC):
    @abstractmethod
    def validate(self, mhs: Mahasiswa) -> bool:
        pass

class SksValidator(IValidationRule):
    def validate(self, mhs: Mahasiswa) -> bool:
        if mhs.sks_diambil > 24:
            print(f"[Gagal] {mhs.nama}: SKS melebihi batas maksimal (24).")
            return False
        return True

class PrasyaratValidator(IValidationRule):
    def validate(self, mhs: Mahasiswa) -> bool:
        if not mhs.lulus_prasyarat:
            print(f"[Gagal] {mhs.nama}: Belum lulus mata kuliah prasyarat.")
            return False
        return True

class RegistrationManager:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: IValidationRule):
        self.rules.append(rule)

    def process_registration(self, mhs: Mahasiswa):
        print(f"\n--- Memproses Registrasi: {mhs.nama} ---")
        for rule in self.rules:
            if not rule.validate(mhs):
                return False
        print(f"[Sukses] {mhs.nama} berhasil registrasi!")
        return True

if __name__ == "__main__":
    # Setup Manager dan Aturan
    manager = RegistrationManager()
    manager.add_rule(SksValidator())
    manager.add_rule(PrasyaratValidator())

    # Data Mahasiswa
    mhs1 = Mahasiswa("Budi", 20, True)
    mhs2 = Mahasiswa("Siti", 26, True)  
    mhs3 = Mahasiswa("Agus", 18, False) 

    manager.process_registration(mhs1)
    manager.process_registration(mhs2)
    manager.process_registration(mhs3)