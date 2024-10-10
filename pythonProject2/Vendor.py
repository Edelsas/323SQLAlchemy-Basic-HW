from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from orm_base import Base

class Vendor(Base):
    __tablename__ = 'Vendor'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vendor_name: Mapped[str] = mapped_column(String(80), nullable=False)
    address_id: Mapped[int] = mapped_column(ForeignKey('Address.id'), nullable=False)

    # Define the relationship with Address
    address = relationship("Address", back_populates="vendors")

    # Define the relationship with PiecePart (this is important for the reverse relation)
    pieceparts = relationship("PiecePart", back_populates="vendor")

    def __init__(self, vendor_name: str, address_id: int):
        super().__init__()
        self.vendor_name = vendor_name
        self.address_id = address_id

    def __str__(self):
        return f"Vendor name: {self.vendor_name}, address ID: {self.address_id}"
