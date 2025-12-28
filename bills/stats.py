from enum import Enum
from .entity import *
from .item import *


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):

        contador: dict[Product, int] = {}
        
        for bill in self.bills:
            for product in bill.products:
                if product in contador:
                    contador[product] = contador[product] + 1
                else:
                    contador[product] = 1
        
        producto_max = max(contador, key=contador.get)
        apariciones_max = contador[producto_max]

        return (producto_max, apariciones_max)

    def find_top_two_sellers(self) -> list:
        
        # Acumula total de ventas por vendedor
        total_por_vendedor: dict[Seller, float] = {}
        for bill in self.bills:
            seller = bill.seller
            total_por_vendedor[seller] = total_por_vendedor.get(seller, 0.0) + bill.calculate_total()

        # Ordena por total descendente y toma hasta 2
        vendedores_ordenados = sorted(total_por_vendedor.keys(),
                                      key=lambda s: total_por_vendedor[s],
                                      reverse=True)
        return vendedores_ordenados[:2]



    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        
        # Acumula total de compras por comprador
        total_por_comprador: dict[Buyer, float] = {}
        for bill in self.bills:
            buyer = bill.buyer
            total_por_comprador[buyer] = total_por_comprador.get(buyer, 0.0) + bill.calculate_total()

        # Si no hay compras, devuelve (None, 0.0)
        if not total_por_comprador:
            return (None, 0.0)

        # Encuentra el comprador con el menor total
        buyer_min = min(total_por_comprador, key=total_por_comprador.get)
        return (buyer_min, total_por_comprador[buyer_min])



    def order_products_by_tax(self, order_type: OrderType) -> tuple:

        # 1) Acumular impuestos por producto (clave: Product -> suma)
        impuestos_por_producto: dict[Product, float] = {}
        representante: dict[Product, Product] = {}  # primera instancia vista

        for bill in self.bills:
            for product in bill.products:
                total_impuestos_aparicion = product.calculate_total_taxes()
                impuestos_por_producto[product] = impuestos_por_producto.get(product, 0.0) + total_impuestos_aparicion
                if product not in representante:
                    representante[product] = product  # guarda la primera instancia como representante

        # 2) Construir lista de pares únicos (Product, suma_impuestos_acumulada)
        pares: list[tuple[Product, float]] = [
            (representante[p], impuestos_por_producto[p]) for p in impuestos_por_producto
        ]

        # 3) Ordenar según order_type
        if order_type == OrderType.ASC:
            pares.sort(key=lambda t: t[1])
        elif order_type == OrderType.DES:
            pares.sort(key=lambda t: t[1], reverse=True)

        return pares


    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
