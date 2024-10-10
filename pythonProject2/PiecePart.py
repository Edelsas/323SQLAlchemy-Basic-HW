from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from orm_base import Base

class PiecePart(Base):
    __tablename__ = 'PiecePart'

    partID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pieceName: Mapped[str] = mapped_column(String(16), nullable=False)
    partDesc: Mapped[str] = mapped_column(String(80), nullable=False)
    vendor_id: Mapped[int] = mapped_column(ForeignKey('Vendor.id'), nullable=False)

    # Define the relationship with Vendor
    vendor = relationship("Vendor", back_populates="pieceparts")

    def __init__(self, pieceName: str, partDesc: str, vendor_id: int):
        super().__init__()
        self.pieceName = pieceName
        self.partDesc = partDesc
        self.vendor_id = vendor_id

    def __str__(self):
        return f"Piece name: {self.pieceName}, part description: {self.partDesc}, vendor ID: {self.vendor_id}"
