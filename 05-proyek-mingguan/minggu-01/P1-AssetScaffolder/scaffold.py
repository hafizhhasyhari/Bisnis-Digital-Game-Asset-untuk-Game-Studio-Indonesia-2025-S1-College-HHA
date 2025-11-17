 # Hafizh Hilman Asyhari
 # Github : @hafizhhasyhari
 # Tahun : 2025
 # Proyek Program 1: Asset Project Scaffolder (Python)
 # Tujuan: Setiap kali kita memulai aset 3D baru (misal: PetiHartaKarun, PedangAjaib), kita butuh struktur folder yang konsisten. Program ini akan membuatnya secara otomatis.
import os
import sys

def create_asset_structure(asset_name):
    """
    Membuat struktur folder standar untuk aset baru.
    """
    # Daftar folder yang akan dibuat
    folders = [
        "01_Blender_Maya",  # File .blend atau .ma
        "02_CSP_Textures",  # File .csp dan source tekstur
        "03_Exports",       # File .fbx, .obj
        "04_Renders",       # Gambar hasil render / preview
        "05_References"     # Moodboard & referensi
    ]
    
    # Membuat folder utama aset
    if not os.path.exists(asset_name):
        os.makedirs(asset_name)
        print(f"Folder utama '{asset_name}' berhasil dibuat.")
    else:
        print(f"Folder '{asset_name}' sudah ada.")
        
    # Membuat sub-folder
    for folder in folders:
        folder_path = os.path.join(asset_name, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"  -> Sub-folder '{folder}' dibuat.")
        else:
            print(f"  -> Sub-folder '{folder}' sudah ada.")
            
    print(f"\nStruktur folder untuk '{asset_name}' selesai dibuat!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        asset_name = sys.argv[1]
    else:
        asset_name = input("Masukkan nama aset (misal: 'PetiHartaKarun'): ")
        
    create_asset_structure(asset_name)
