import logging
from menu_definitions import (
    menu_main, add_select, delete_select, list_select,
    select_select, update_select, yes_no
)
from db_connection import engine, Session
from orm_base import metadata
from Vendor import Vendor
from PiecePart import PiecePart
from Address import Address

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main loop for the menu-driven application."""
    metadata.drop_all(engine)
    metadata.create_all(engine)
    session = Session()

    while True:
        choice = menu_main.menu_prompt()
        if choice == "Add PiecePart":
            add_piece_part(session)
        elif choice == "Add Vendor":
            add_vendor(session)
        elif choice == "Add Address":  # Add this line
            add_address(session)
        elif choice == "List PieceParts":
            list_piece_parts(session)
        elif choice == "List Vendors":
            list_vendors(session)
        elif choice == "Update Vendor":
            update_vendor(session)
        elif choice == "Delete PiecePart":
            delete_piece_part(session)
        elif choice == "Delete Vendor":
            delete_vendor(session)
        elif choice == "Quit":
            break

    session.close()


def add_piece_part(session):
    """Prompt for adding a new piece part."""
    part_name = input("Enter part name: ")
    part_desc = input("Enter part description: ")
    vendor_id = int(input("Enter vendor ID: "))

    # Check if the vendor exists
    vendor = session.get(Vendor, vendor_id)
    if not vendor:
        print(f"Error: Vendor with ID {vendor_id} does not exist.")
        return

    piece_part = PiecePart(pieceName=part_name, partDesc=part_desc, vendor_id=vendor_id)

    session.add(piece_part)
    session.commit()
    print("Piece part added successfully!")

def add_address(session):
    """Prompt for adding a new address."""
    zip_code = input("Enter zip code: ")
    city = input("Enter city: ")
    state = input("Enter state: ")

    address = Address(zip_code=zip_code, city=city, state=state)

    session.add(address)
    session.commit()
    print(f"Address added successfully with ID: {address.id}")


def add_vendor(session):
    """Prompt for adding a new vendor."""
    vendor_name = input("Enter vendor name: ")
    address_id = int(input("Enter address ID: "))

    # Check if the address exists
    address = session.get(Address, address_id)
    if not address:
        print(f"Error: Address with ID {address_id} does not exist.")
        return

    vendor = Vendor(vendor_name=vendor_name, address_id=address_id)

    session.add(vendor)
    session.commit()
    print("Vendor added successfully!")


def list_piece_parts(session):
    """List all piece parts."""
    piece_parts = session.query(PiecePart).all()
    for part in piece_parts:
        print(part)


def list_vendors(session):
    """List all vendors."""
    vendors = session.query(Vendor).all()
    for vendor in vendors:
        print(vendor)


def update_vendor(session):
    """Prompt for updating a vendor's information."""
    vendor_id = int(input("Enter vendor ID: "))
    new_vendor_name = input("Enter new vendor name: ")

    vendor = session.get(Vendor, vendor_id)
    if vendor:
        vendor.vendor_name = new_vendor_name
        session.commit()
        print("Vendor updated successfully!")
    else:
        print("Vendor not found.")

def delete_piece_part(session):
    """Prompt for deleting a piece part."""
    part_id = int(input("Enter part ID: "))

    piece_part = session.get(PiecePart, part_id)
    if piece_part:
        session.delete(piece_part)
        session.commit()
        print("Piece part deleted successfully!")
    else:
        print("Piece part not found.")


def delete_vendor(session):
    """Prompt for deleting a vendor."""
    vendor_id = int(input("Enter vendor ID: "))

    vendor = session.get(Vendor, vendor_id)
    if vendor:
        session.delete(vendor)
        session.commit()
        print("Vendor deleted successfully!")
    else:
        print("Vendor not found.")


if __name__ == "__main__":
    main()
