import os

MAGIC_NUMBERS = {
    "PNG": bytes.fromhex("89 50 4E 47 0D 0A 1A 0A"),
    "JPG": bytes.fromhex("FF D8 FF"),
    "GIF": b"GIF89a",
    "PDF": b"%PDF",
    "ZIP": bytes.fromhex("50 4B 03 04")
}

def main():
    input_file = input("[+] Archivo de entrada: ").strip()

    if not os.path.isfile(input_file):
        print("[-] El archivo no existe.")
        return

    print("[*] Tipos disponibles:")
    for t in MAGIC_NUMBERS:
        print(f" - {t}")

    target_type = input("[*] ¿A qué tipo quieres que sea?: ").strip().upper()

    if target_type not in MAGIC_NUMBERS:
        print("[-] Tipo no soportado.")
        return

    output_file = input("[+] Nombre del archivo de salida: ").strip()

    with open(input_file, "rb") as f:
        original_data = f.read()

    new_data = MAGIC_NUMBERS[target_type] + original_data

    with open(output_file, "wb") as f:
        f.write(new_data)

    print(f"[+] Archivo creado: {output_file}")
    print(f"[*] Magic number usado: {MAGIC_NUMBERS[target_type].hex(' ')}")

if __name__ == "__main__":
    main()
