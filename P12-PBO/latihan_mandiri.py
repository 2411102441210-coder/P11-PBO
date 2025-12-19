import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(name)s %(message)s'
)
LOG_REG = logging.getLogger('RegistrationSystem')

class IValidationRule(ABC):
    @abstractmethod
    def validate(self, mhs_nama: str, data: dict) -> bool:
        pass

class SksLimitRule(IValidationRule):
    def validate(self, mhs_nama: str, data: dict) -> bool:
        sks = data.get('sks', 0)
        if sks > 24:
            LOG_REG.warning(f"Validasi Gagal: {mhs_nama} mengambil {sks} SKS. Maksimal 24!")
            return False
        return True

class RegistrationService:
    def __init__(self, rules: list[IValidationRule]):
        self.rules = rules

    def register(self, mhs_nama: str, data: dict):
        LOG_REG.info(f"Memulai registrasi mahasiswa: {mhs_nama}")
        
        valid = True
        for rule in self.rules:
            if not rule.validate(mhs_nama, data):
                valid = False
                break
        
        if valid:
            LOG_REG.info(f"Registrasi BERHASIL untuk {mhs_nama}.")
        else:
            LOG_REG.error(f"Registrasi DITOLAK untuk {mhs_nama} karena melanggar aturan.")

if __name__ == "__main__":
    validator_sks = SksLimitRule()
    service = RegistrationService(rules=[validator_sks])

    print("--- Skenario 1: Data Valid ---")
    service.register("Budi", {"sks": 20})

    print("\n--- Skenario 2: Pelanggaran SKS ---")
    service.register("Siti", {"sks": 26})