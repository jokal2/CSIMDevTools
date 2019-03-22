import datetime
import os
import pathlib
import shutil
import subprocess
import sys
import tarfile


QT_ROOT = pathlib.Path("G:/", "Qt", "5.11.0", "mingw53_32", "bin")
REPO_ROOT = pathlib.Path("C:/", "C++", "ClassicSim")
QML_DIR = REPO_ROOT / "QML"
ARCHIVE_PATH = pathlib.Path("C:/", "C++", "build-ClassicSim-Desktop_Qt_5_11_0_MinGW_32bit-Release")
RELEASE_DIR = ARCHIVE_PATH / "release"


def main():
    run_windeployqt()
    copy_rotations()
    copy_items()
    copy_license_files()
    clear_saves()
    tar_application()


def run_windeployqt():
    os.chdir(str(QT_ROOT))
    command = ["windeployqt.exe", "--qmldir", str(QML_DIR), str(RELEASE_DIR)]
    subprocess.run(command)


def copy_rotations():
    src_path = (REPO_ROOT / "Rotation" / "Rotations")
    class_directories = {
        "Hunter",
        "Rogue",
        "Warrior",
    }
    shutil.rmtree(str(RELEASE_DIR / "Rotations"))
    for directory in class_directories:
        shutil.copytree(src=str(src_path / directory), dst=str(RELEASE_DIR / "Rotations" / directory))
    shutil.copy2(src=str(src_path / "rotation_paths.xml"), dst=str(RELEASE_DIR / "rotation_paths.xml"))


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
        shutil.rmtree(str(RELEASE_DIR / directory))
        shutil.copytree(src=str(source / directory), dst=str(RELEASE_DIR / directory))

    shutil.copy2(src=str(source / "equipment_paths.xml"),
                 dst=str(RELEASE_DIR / "equipment_paths.xml"))
    shutil.copy2(src=str(source / "set_bonuses.xml"),
                 dst=str(RELEASE_DIR / "set_bonuses.xml"))


def copy_license_files():
    shutil.copy2(src=str(REPO_ROOT / "LICENSE"),
                 dst=str(RELEASE_DIR / "LICENSE"))
    shutil.copy2(src=str(REPO_ROOT / "LICENSE.LGPL"),
                 dst=str(RELEASE_DIR / "LICENSE.LGPL"))


def clear_saves():
    shutil.rmtree(str(RELEASE_DIR / "Saves"))
    os.mkdir(str(RELEASE_DIR / "Saves"))


def tar_application():
    def _get_tar_name():
        date_string = datetime.date.today().strftime("%y%m%d")

        for i in range(10):
            revision = i + 1
            tar_name = "classicsim-{date_string}-{revision}-win32".format(date_string=date_string,
                                                                          revision=revision)
            tar_path = ARCHIVE_PATH / tar_name
            if tar_path.exists():
                continue

            return tar_path

        print("Failed to tar application. All possible filenames existed already.")
        sys.exit(1)

    def _get_files_to_archive():
        files_to_archive = []
        all_files = list(RELEASE_DIR.glob("**/*"))

        for path in all_files:
            if path.suffix in [".o", ".cpp", ".opt", ".h"]:
                continue
            if path.is_dir():
                continue
            files_to_archive.append(path)

        for path in files_to_archive:
            print("Archiving", path.relative_to(RELEASE_DIR))

        return files_to_archive

    files_to_archive = _get_files_to_archive()

    tar_name = _get_tar_name()
    with tarfile.open("{tar_name}.tar.gz".format(tar_name=tar_name), "x:gz") as tar:
        for path in files_to_archive:
            tar.add(str(path), arcname=str(tar_name.name / path.relative_to(RELEASE_DIR)), recursive=False)


if __name__ == "__main__":
    main()
