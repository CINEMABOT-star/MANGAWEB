import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
CATALOG_PATH = ROOT / "catalogo.json"
SUPPORTED_FILES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".pdf", ".epub"}
DEFAULT_ART = {
    "style": "linear-gradient(145deg,#253945,#bd654a 58%,#e4b36a)",
    "orb": "#edc38c",
    "shape": "#252834",
}


def sort_key(value):
    return [
        int(part) if part.isdigit() else part.casefold()
        for part in re.split(r"(\d+)", value)
    ]


def asset_path(path):
    return "/".join(quote(part) for part in path.relative_to(ROOT).parts)


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")


def discover_titles():
    titles = []
    for section, content_type in (("manga", "manga"), ("libri", "libro")):
        section_path = ROOT / section
        if not section_path.is_dir():
            continue

        for title_path in sorted(section_path.iterdir(), key=lambda path: sort_key(path.name)):
            if not title_path.is_dir() or title_path.name.startswith("_"):
                continue
            metadata_path = title_path / "info.json"
            if not metadata_path.is_file():
                raise ValueError(f"Manca il file obbligatorio: {metadata_path.relative_to(ROOT)}")
            with metadata_path.open(encoding="utf-8") as metadata_file:
                metadata = json.load(metadata_file)
            if not isinstance(metadata, dict):
                raise ValueError(f"{metadata_path.relative_to(ROOT)} deve contenere un oggetto JSON.")

            title_id = metadata.get("id", slugify(title_path.name))
            for field in ("title", "author", "genre", "description"):
                if not isinstance(metadata.get(field), str) or not metadata[field].strip():
                    raise ValueError(f"{metadata_path.relative_to(ROOT)}: il campo {field!r} è obbligatorio.")
            if not re.fullmatch(r"[a-z0-9-]+", title_id):
                raise ValueError(f"{metadata_path.relative_to(ROOT)}: id non valido {title_id!r}.")

            chapters = []
            chapters_path = title_path / "capitoli"
            if chapters_path.is_dir():
                for chapter_path in sorted(chapters_path.iterdir(), key=lambda path: sort_key(path.name)):
                    if not chapter_path.is_dir():
                        continue
                    files = sorted(
                        (path for path in chapter_path.rglob("*")
                         if path.is_file() and path.suffix.lower() in SUPPORTED_FILES),
                        key=lambda path: sort_key(path.relative_to(chapter_path).as_posix()),
                    )
                    if not files:
                        continue
                    documents = [path for path in files if path.suffix.lower() in {".pdf", ".epub"}]
                    images = [path for path in files if path not in documents]
                    if documents and images:
                        raise ValueError(
                            f"{chapter_path.relative_to(ROOT)}: separa i PDF/EPUB dalle pagine immagine."
                        )
                    if documents:
                        for document in documents:
                            chapters.append({
                                "title": document.stem if len(documents) > 1 else chapter_path.name,
                                "url": asset_path(document),
                            })
                    else:
                        chapters.append({
                            "title": chapter_path.name,
                            "pages": [asset_path(path) for path in images],
                        })

            entry = {
                **DEFAULT_ART,
                **metadata,
                "id": title_id,
                "type": content_type,
                "volumes": metadata.get("volumes", "In corso"),
                "rating": metadata.get("rating", ""),
                "chapters": chapters,
            }
            cover = metadata.get("cover")
            if isinstance(cover, str) and cover and not cover.startswith(("https://", "http://")):
                entry["cover"] = asset_path(title_path / cover)
            titles.append(entry)
    return titles


def main():
    with CATALOG_PATH.open(encoding="utf-8") as catalog_file:
        catalog = json.load(catalog_file)
    if not isinstance(catalog, list):
        raise ValueError("catalogo.json deve contenere una lista di titoli.")

    ids = {item["id"] for item in catalog}
    additions = discover_titles()
    for item in additions:
        if item["id"] in ids:
            raise ValueError(f"Id duplicato nel catalogo: {item['id']!r}.")
        ids.add(item["id"])
    catalog.extend(additions)
    with CATALOG_PATH.open("w", encoding="utf-8", newline="\n") as catalog_file:
        json.dump(catalog, catalog_file, ensure_ascii=False, indent=2)
        catalog_file.write("\n")
    print(f"Catalogo pronto: {len(catalog)} titoli totali, {len(additions)} aggiunti dalle cartelle.")


if __name__ == "__main__":
    main()
