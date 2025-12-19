import pdb

class DiskonCalculator:
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:

        #pdb.set_trace() 
        
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_akhir = harga_awal - jumlah_diskon
        return harga_akhir

if __name__ == '__main__':
    calc = DiskonCalculator()
    calc.hitung_diskon(1000, 10)