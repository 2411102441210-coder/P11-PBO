import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
LOGGER = logging.getLogger('Checkout')

@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: Order) -> bool:
        """Interface untuk prosesor pembayaran."""
        pass

class INotificationService(ABC):
    @abstractmethod
    def send(self, order: Order):
        """Interface untuk layanan notifikasi."""
        pass

class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        logging.info(f"Payment: Memproses Kartu Kredit untuk {order.customer_name}.")
        return True

class EmailNotifier(INotificationService):
    def send(self, order: Order):
        logging.info(f"Notif: Mengirim email konfirmasi ke {order.customer_name}.")

# --- KELAS KOORDINATOR DENGAN DOCSTRING ---
class CheckoutService:
    """
    Kelas high-level untuk mengkoordinasi proses transaksi pembayaran.
    
    Kelas ini memisahkan logika pembayaran dan notifikasi (memenuhi SRP).
    """

    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        """
        Menginisialisasi CheckoutService dengan dependensi yang diperlukan.
        
        Args:
            payment_processor (IPaymentProcessor): Implementasi interface pembayaran.
            notifier (INotificationService): Implementasi interface notifikasi.
        """
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order) -> bool:
        """
        Menjalankan proses checkout dan memvalidasi pembayaran.
        
        Args:
            order (Order): Objek pesanan yang akan diproses.
            
        Returns:
            bool: True jika checkout sukses, False jika gagal.
        """
        # Logging alih-alih print() [cite: 277]
        LOGGER.info(f"Memulai checkout untuk {order.customer_name}. Total: {order.total_price}")
        
        payment_success = self.payment_processor.process(order)
        
        if payment_success:
            order.status = "paid"
            self.notifier.send(order)
            LOGGER.info("Checkout Sukses. Status pesanan: PAID.")
            return True
        else:
            LOGGER.error("Pembayaran gagal. Transaksi dibatalkan.")
            return False

if __name__ == "__main__":
    andi_order = Order("Andi", 500000)
    service = CheckoutService(CreditCardProcessor(), EmailNotifier())
    service.run_checkout(andi_order)