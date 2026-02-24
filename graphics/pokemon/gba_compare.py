import os
from PIL import Image

base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Dossier analysé : {base_dir}")

subfolders = sorted([
    f for f in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, f))
])

if not subfolders:
    print("Aucun sous-dossier trouvé.")
    exit()

rows = []
total_height = 0
max_width = 0

for folder in subfolders:
    folder_path = os.path.join(base_dir, folder)
    print(f"\nAnalyse du dossier : {folder}")

    all_files = os.listdir(folder_path)
    lower_files = [f.lower() for f in all_files]

    # Condition obligatoire : au moins un "front_gba"
    has_front_gba = any(
        f.endswith(".png") and "front_gba" in f
        for f in lower_files
    )

    if not has_front_gba:
        print("  -> Ignoré (pas de front_gba)")
        continue

    # Sépare anim_front et back
    front_files = sorted([
        f for f in all_files
        if f.lower().endswith(".png") and "anim_front" in f.lower()
    ])

    back_files = sorted([
        f for f in all_files
        if f.lower().endswith(".png") and "back" in f.lower()
    ])

    image_files = front_files + back_files

    if not image_files:
        print("  -> Aucun anim_front/back trouvé.")
        continue

    print(f"  -> {len(image_files)} images retenues")

    images = []
    for file in image_files:
        img_path = os.path.join(folder_path, file)
        try:
            img = Image.open(img_path).convert("RGBA")
            images.append(img)
        except Exception as e:
            print(f"Erreur avec {file} : {e}")

    if not images:
        continue

    row_width = sum(img.width for img in images)
    row_height = max(img.height for img in images)

    row_image = Image.new("RGBA", (row_width, row_height), (0, 0, 0, 0))

    x_offset = 0
    for img in images:
        row_image.paste(img, (x_offset, 0))
        x_offset += img.width

    rows.append(row_image)
    total_height += row_height
    max_width = max(max_width, row_width)

if not rows:
    print("\nAucune image valide trouvée au total.")
    exit()

final_image = Image.new("RGBA", (max_width, total_height), (0, 0, 0, 0))

y_offset = 0
for row in rows:
    final_image.paste(row, (0, y_offset))
    y_offset += row.height

output_path = os.path.join(base_dir, "assemblage.png")
final_image.save(output_path)

print(f"\nImage créée : {output_path}")

input("Press Enter to continue...")