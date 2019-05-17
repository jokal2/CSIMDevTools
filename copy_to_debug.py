import pathlib
import shutil


REPO_ROOT = pathlib.Path("C:/", "C++", "ClassicSim")
DEBUG_DIR = pathlib.Path("C:/", "C++", "build-ClassicSim-Desktop_Qt_5_11_3_MinGW_32bit-Debug")


def main():
    copy_rotations()
    copy_items()


def copy_rotations():
    src_path = (REPO_ROOT / "Rotation" / "Rotations")
    class_directories = {
        "Hunter",
        "Rogue",
        "Warrior",
        "Paladin",
    }
    shutil.rmtree(str(DEBUG_DIR / "Rotations"))
    for directory in class_directories:
        shutil.copytree(src=str(src_path / directory), dst=str(DEBUG_DIR / "Rotations" / directory))
    shutil.copy2(src=str(src_path / "rotation_paths.xml"), dst=str(DEBUG_DIR / "rotation_paths.xml"))


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
        shutil.rmtree(str(DEBUG_DIR / directory))
        shutil.copytree(src=str(source / directory), dst=str(DEBUG_DIR / directory))

    shutil.copy2(src=str(source / "equipment_paths.xml"),
                 dst=str(DEBUG_DIR / "equipment_paths.xml"))
    shutil.copy2(src=str(source / "set_bonuses.xml"),
                 dst=str(DEBUG_DIR / "set_bonuses.xml"))



if __name__ == "__main__":
    main()
