import datetime
import os
from pathlib import Path
from docxtpl import DocxTemplate


def bill(achternaam, tabel):
    base_dir = Path(__file__).parent
    word_template_path = base_dir / 'factuur.docx'
    output_dir = base_dir / "Rekeningen"

    output_dir.mkdir(exist_ok=True)
    file_count = 1
    for path in os.listdir(output_dir):
        if os.path.isfile(os.path.join(output_dir, path)):
            file_count += 1

    today = datetime.datetime.today()
    factuur_nummer = str(2023) + str(file_count)
    factuur_naam = achternaam + '_' + factuur_nummer + '.docx'
    doc = DocxTemplate(word_template_path)
    context = {
        "TODAY": today.strftime("%Y-%m-%d"),
        "FACTUURNUMMER": factuur_nummer,
        "ACHTERNAAM": achternaam,
        "TABEL": tabel
    }


    doc.render(context)

    doc.save(output_dir / factuur_naam)
