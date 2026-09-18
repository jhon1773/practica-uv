def main() -> None:
    precio_original = float(input("Ingrese el precio del producto: "))
    descuento = precio_original * 0.10
    precio_final = precio_original - descuento
    print(f"Precio original: {precio_original}")
    print(f"Descuento: {descuento}")
    print(f"Precio final: {precio_final}")

main()
