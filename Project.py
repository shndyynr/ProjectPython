# Program Python untuk menghitung rumus fisika dasar
# Dibuat oleh: Shandy Yanuar Nailul Falah

def hitung_kecepatan():
    try:
        jarak = float(input("Masukkan jarak (dalam meter): "))
        waktu = float(input("Masukkan waktu (dalam detik): "))
        if waktu != 0:  # Hindari pembagian oleh nol
            kecepatan = jarak / waktu
            print(f"Kecepatan = {kecepatan} m/s")
        else:
            print("Waktu tidak boleh nol!")
    except ValueError:
        print("Error: Masukkan angka yang valid.")

def hitung_percepatan():
    try:
        v_awal = float(input("Masukkan kecepatan awal (m/s): "))
        v_akhir = float(input("Masukkan kecepatan akhir (m/s): "))
        waktu = float(input("Masukkan waktu (dalam detik): "))
        if waktu != 0:
            percepatan = (v_akhir - v_awal) / waktu
            print(f"Percepatan = {percepatan} m/s²")
        else:
            print("Waktu tidak boleh nol!")
    except ValueError:
        print("Error: Masukkan angka yang valid.")

def hitung_gaya():
    try:
        massa = float(input("Masukkan massa (dalam kg): "))
        percepatan = float(input("Masukkan percepatan (m/s²): "))
        gaya = massa * percepatan
        print(f"Gaya = {gaya} Newton")
    except ValueError:
        print("Error: Masukkan angka yang valid.")

def hitung_berat():
    try:
        massa = float(input("Masukkan massa (dalam kg): "))
        g = 9.8  # Gravitasi bumi, dalam m/s²
        berat = massa * g
        print(f"Berat = {berat} Newton")
    except ValueError:
        print("Error: Masukkan angka yang valid.")

def hitung_energi_kinetik():
    try:
        massa = float(input("Masukkan massa (dalam kg): "))
        kecepatan = float(input("Masukkan kecepatan (m/s): "))
        energi = 0.5 * massa * (kecepatan ** 2)
        print(f"Energi kinetik = {energi} Joule")
    except ValueError:
        print("Error: Masukkan angka yang valid.")

# Menu utama program
while True:
    print("\n=== APLIKASI HITUNG FISIKA SEKOLAH ===")
    print("1. Hitung kecepatan (v = d / t)")
    print("2. Hitung percepatan (a = (v2 - v1) / t)")
    print("3. Hitung gaya (F = m * a)")
    print("4. Hitung berat (W = m * g)")
    print("5. Hitung energi kinetik (KE = 0.5 * m * v^2)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        hitung_kecepatan()
    elif pilihan == '2':
        hitung_percepatan()
    elif pilihan == '3':
        hitung_gaya()
    elif pilihan == '4':
        hitung_berat()
    elif pilihan == '5':
        hitung_energi_kinetik()
    elif pilihan == '6':
        print("Terima kasih! Program selesai.")
        break  # Keluar dari loop
    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")
