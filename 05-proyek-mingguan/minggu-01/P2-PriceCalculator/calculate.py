   # Proyek Program 2: Simple Asset Price Calculator (Python)
   # Tujuan: Program konsol sederhana untuk menghitung harga jual aset berdasarkan jam kerja dan rate yang diinginkan. Ini adalah inti dari "Bisnis Digital".
   # Nama : Hafizh Hilman Asyhari
   # Github : @hafizhhasyhari
   # Instagram : @hafizhhasyhari
   # Youtube : @hafizhhasyhari

def calculate_price():
    """
    Kalkulator sederhana untuk menentukan harga jual aset digital.
    """
    try:
        # Input dari kreator
        hourly_rate = float(input("Masukkan target rate per jam Anda (misal: 150000): Rp "))
        total_hours = float(input("Masukkan total jam kerja untuk aset ini: "))
        
        # Biaya platform (misal: Unity Asset Store 30%)
        platform_cut = 0.30 
        
        # Biaya dasar (Waktu Anda)
        base_cost = hourly_rate * total_hours
        
        # Harga yang harus Anda tetapkan agar 
        # setelah dipotong platform, Anda tetap dapat biaya dasar.
        price_to_charge = base_cost / (1 - platform_cut)
        
        # Keuntungan Anda setelah dipotong
        your_profit = price_to_charge * (1 - platform_cut)
        
        print("\n--- Kalkulasi Harga Aset ---")
        print(f"Rate per Jam Anda:   Rp {hourly_rate:,.0f}")
        print(f"Total Jam Kerja:     {total_hours} jam")
        print(f"Biaya Produksi:      Rp {base_cost:,.0f}")
        print(f"Potongan Platform:   {platform_cut * 100}%")
        print("\n==============================================")
        print(f"Rekomendasi Harga Jual di Store:")
        print(f" >> Rp {price_to_charge:,.0f} <<")
        print("==============================================")
        print(f"Estimasi pendapatan Anda (setelah dipotong): Rp {your_profit:,.0f}")
        
    except ValueError:
        print("\nError: Masukkan hanya angka.")
    except ZeroDivisionError:
        print("\nError: Sesuatu yang aneh terjadi.")

if __name__ == "__main__":
    calculate_price()
