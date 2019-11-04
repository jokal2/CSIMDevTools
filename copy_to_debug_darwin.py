import pathlib
import shutil
import os


REPO_ROOT = pathlib.Path("/Users/lanza", "Projects", "ClassicSim")
DEBUG_DIR = pathlib.Path(
    "/Users/lanza",
    "Projects",
    "build-ClassicSim-Desktop_Qt_5_12_5_clang_64bit-Debug",
    "ClassicSim.app", "Contents", "MacOS"
)


def main():
    copy_rotations()
    copy_items()
    create_saves()


def copy_rotations():
    src_path = REPO_ROOT / "Rotation" / "Rotations"
    class_directories = {
        "Hunter",
        "Rogue",
        "Warrior",
        "Paladin",
        "Shaman",
        "Mage",
        "Druid",
        "Priest",
        "Warlock",
    }
    if (DEBUG_DIR / "Rotations").exists():
        shutil.rmtree(str(DEBUG_DIR / "Rotations"))
    for directory in class_directories:
        if not (src_path / directory).exists():
            print("Skipping " + directory + " because source does not exist")
            continue

        shutil.copytree(
            src=str(src_path / directory), dst=str(DEBUG_DIR / "Rotations" / directory)
        )
    shutil.copy2(
        src=str(src_path / "rotation_paths.xml"),
        dst=str(DEBUG_DIR / "rotation_paths.xml"),
    )


def copy_items():
    source = REPO_ROOT / "Equipment" / "EquipmentDb"
    item_directories = {
        "Belts",
        "Boots",
        "Chests",
        "Gloves",
        "Helms",
        "Legs",
        "Misc",
        "Shoulders",
        "Weapons",
        "Wrists",
    }
    for directory in item_directories:
        if (DEBUG_DIR / directory).exists():
            shutil.rmtree(str(DEBUG_DIR / directory))
        shutil.copytree(src=str(source / directory), dst=str(DEBUG_DIR / directory))

    shutil.copy2(
        src=str(source / "equipment_paths.xml"),
        dst=str(DEBUG_DIR / "equipment_paths.xml"),
    )
    shutil.copy2(
        src=str(source / "set_bonuses.xml"), dst=str(DEBUG_DIR / "set_bonuses.xml")
    )


def create_saves():
    if not (DEBUG_DIR / "Saves").exists():
        os.mkdir((DEBUG_DIR / "Saves"))


if __name__ == "__main__":
    main()
