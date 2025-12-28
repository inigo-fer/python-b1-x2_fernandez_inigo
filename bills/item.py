from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id: str, tax_type: TaxType,percentage: float):
        self.tax_id=tax_id
        self.tax_type=tax_type
        self.percentage=percentage
        pass


class Product:
     # Write the parameters in the next line
    def __init__(self, product_id: str, name: str, expiration_date: datetime, bar_code: str, quantity: int, price: float, taxes: list[Tax]):
        self.product_id=product_id
        self.name=name
        self.expiration_date=expiration_date
        self.bar_code=bar_code
        self.quantity=quantity
        self.price=price
        self.taxes=taxes
        pass        

    def calculate_tax(self, tax: Tax) -> float:
        tax_base= self.quantity*self.price
        tax_type=tax.tax_type
        calculated_tax=0

        for single_tax in self.taxes:
            if single_tax.tax_type==tax_type:
                if tax_type == TaxType.IVA:
                    tax_amount=tax_base*single_tax.percentage
                elif tax_type == TaxType.ISD:
                    tax_amount=tax_base*single_tax.percentage*ISD_FACTOR
            
                calculated_tax=calculated_tax+tax_amount
        
        return calculated_tax

    def calculate_total_taxes(self) -> float:
        
        # Calculate IVA for this product
        total_iva = self.calculate_tax(
            Tax(tax_id="IND-IVA", tax_type=TaxType.IVA, percentage=0.0)
        )
        # Calculate ISD for this product
        total_isd = self.calculate_tax(
            Tax(tax_id="IND-ISD", tax_type=TaxType.ISD, percentage=0.0)
        )
        # Sum both
        return float(total_iva + total_isd)


    def calculate_total(self) -> float:
        base = self.quantity * self.price
        taxes_total = self.calculate_total_taxes()
        return float(base + taxes_total)


    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        self.bill_id=bill_id
        self.sale_date=sale_date
        self.seller=seller
        self.buyer=buyer
        self.products=products
        pass
       

    def calculate_total(self) -> float:
        total = 0.0
        for product in self.products:
            total += product.calculate_total()
        return float(total)


    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()