from Bio.PDB import PDBParser
import os

def calculate_gridbox_center(structure):
    model = structure[0]  # Mengambil model pertama dari struktur PDB
    atoms = model.get_atoms()  # Mendapatkan daftar atom dalam model
    
    x_sum = y_sum = z_sum = 0.0
    num_atoms = 0
    
    for atom in atoms:
        x, y, z = atom.get_coord()
        x_sum += x
        y_sum += y
        z_sum += z
        num_atoms += 1
    
    x_center = round(x_sum / num_atoms, 3)
    y_center = round(y_sum / num_atoms, 3)
    z_center = round(z_sum / num_atoms, 3)
    
    return x_center, y_center, z_center


# Direktori input (file PDB) dan output (file config.txt)
input_directory = os.getcwd()  # Direktori kerja
output_directory = os.getcwd()  # Direktori kerja

# Ukuran grid box
size_x = 60.0
size_y = 60.0
size_z = 60.0

# Loop melalui setiap file PDB dalam direktori input
for filename in os.listdir(input_directory):
    if filename.endswith(".pdb"):
        pdb_file = os.path.join(input_directory, filename)
        
        # Buat direktori output sesuai dengan nama file PDB
        pdb_name = os.path.splitext(filename)[0]
        output_subdirectory = os.path.join(output_directory, pdb_name)
        os.makedirs(output_subdirectory, exist_ok=True)
        
        # Membaca struktur PDB
        parser = PDBParser()
        structure = parser.get_structure("ligand", pdb_file)
        
        # Menghitung koordinat titik pusat grid box
        gridbox_center = calculate_gridbox_center(structure)
        
        # Menulis koordinat titik pusat, ukuran grid box, dan parameter tambahan dalam file "config.txt"
        config_filename = "config.txt"
        config_filepath = os.path.join(output_subdirectory, config_filename)
        with open(config_filepath, "w") as file:
            file.write(f"center_x = {gridbox_center[0]:.3f}\n")
            file.write(f"center_y = {gridbox_center[1]:.3f}\n")
            file.write(f"center_z = {gridbox_center[2]:.3f}\n")
            file.write(f"size_x = {size_x:.3f}\n")
            file.write(f"size_y = {size_y:.3f}\n")
            file.write(f"size_z = {size_z:.3f}\n")
            file.write("num_modes = 10\n")
            file.write("exhaustiveness = 8\n")
            file.write("cpu = 4\n")
            file.write("\n")
            file.write("# Script ini ditulis oleh La Ode Aman\n")
            file.write("# Email: laodeaman.ai@gmail.com\n")
            file.write("# laode_aman@ung.ac.id\n")
            file.write("# Universitas Negeri Gorontalo, Indonesia\n")
        
        print(f"Koordinat titik pusat, ukuran grid box, dan parameter tambahan untuk file {filename} telah ditulis dalam file {config_filepath}.")
        print("Script ini ditulis oleh La Ode Aman")
        print("Email: laodeaman.ai@gmail.com")
        print("laode_aman@ung.ac.id")
        print("Universitas Negeri Gorontalo, Indonesia")
