import os

MAGIC_FILE = "magic_numbers.txt"

def load_magic_numbers():
    magic_numbers = {}

    if not os.path.isfile(MAGIC_FILE):
        print(f"[-] No se encuentra {MAGIC_FILE}")
        return magic_numbers

    with open(MAGIC_FILE, "r") as f:
        for line in f:
            line = line.strip()

            if not line or "=" not in line:
                continue

            file_type, hex_value = line.split("=", 1)
            file_type = file_type.strip().upper()
            hex_value = hex_value.strip()

            try:
                magic_numbers[file_type] = bytes.fromhex(hex_value)
            except ValueError:
                print(f"[-] Hex inválido en {file_type}")

    return magic_numbers

def main():
    MAGIC_NUMBERS = load_magic_numbers()

    if not MAGIC_NUMBERS:
        print("[-] No hay magic numbers disponibles.")
        return

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
