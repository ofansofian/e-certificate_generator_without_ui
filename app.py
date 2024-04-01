from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load template sertifikat
#sesuaikan dengan image tamplate sertifkat Anda
template_path = "template.jpg"
template = Image.open(template_path)

# Load font untuk teks
font_path = "AnandaBlackPersonalUseRegular-rg9Rx.ttf"
font = ImageFont.truetype(font_path, size=30)

# Load data peserta dari file Excel atau CSV
data = pd.read_excel("data_peserta.xlsx")

# Loop melalui setiap baris data
for index, row in data.iterrows():
    # Copy template
    sertifikat = template.copy()

    # Inisialisasi ImageDraw
    draw = ImageDraw.Draw(sertifikat)

    # Tulis informasi peserta ke sertifikat
    nama = row['Nama']
    judul = row['Judul']    
    posisi_nama = (50, 100)
    posisi_judul = (50, 150)
    

    draw.text(posisi_nama, nama, fill="black", font=font)
    draw.text(posisi_judul, judul, fill="black", font=font)
    

    # Simpan sertifikat
    sertifikat.save(f"sertifikat_{nama}.png")

print("Sertifikat berhasil dibuat!")
