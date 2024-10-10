from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from orm_base import Base

class Address(Base):
    __tablename__ = 'Address'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    zip_code: Mapped[str] = mapped_column(String(60), nullable=False)
    city: Mapped[str] = mapped_column(String(60), nullable=False)
    state: Mapped[str] = mapped_column(String(60), nullable=False)

    # Define the relationship with Vendor
    vendors = relationship("Vendor", back_populates="address")

    def __init__(self, zip_code: str, city: str, state: str):
        super().__init__()  # Call to the parent class constructor
        self.zip_code = zip_code
        self.city = city
        self.state = state

    def __str__(self):
        return f"Address: {self.zip_code}, {self.city}, {self.state}"
