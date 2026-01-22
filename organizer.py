import shutil
import logging
from pathlib import Path

# ================= CONFIG =================   this are the key points for the program to understand files types
BASE_DIR = Path("test_folder")
SKIP_FOLDERS = ["Images", "Videos", "Documents", "Others"]

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Others": []
}
# =========================================

#this part is to save all the loggings for the security reasons
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

#this function determines which target folder a file should be moved to based on its extension
def get_target_folder(file):
    for folder, extensions in FILE_TYPES.items():
        if file.suffix.lower() in extensions:
            return folder
    return "Others"

#this function scans the base folder and simulates all file movements in the dry run phase
def scan_files():
    """Phase 1: Dry Run"""
    actions = []

    for item in BASE_DIR.iterdir():

        if item.is_dir() and item.name in SKIP_FOLDERS:
            continue

        if item.is_file():
            target = get_target_folder(item)
            actions.append((item, target))
            print(f"[DRY RUN] {item.name} → {target}")
            logging.info(f"[DRY RUN] {item.name} → {target}")

    return actions

#this function executes the actual file movements in the live run phase after user approval
def execute_actions(actions):
    """Phase 2: Live Run"""
    for file, target in actions:
        target_path = BASE_DIR / target
        target_path.mkdir(exist_ok=True)
        shutil.move(str(file), target_path / file.name)
        logging.info(f"MOVED {file.name} → {target}")

if __name__ == "__main__":

    print("🔍 PHASE 1: DRY RUN (Simulation Only)\n")
    planned_actions = scan_files()

    if not planned_actions:
        print("ℹ️ No files to organize.")
        exit()

    confirm = input("\n⚠️ Type Y to execute changes: ")
    if confirm != "Y":
        print("❌ Operation cancelled. No files were moved.")
        exit()

    print("\n🚀 PHASE 2: LIVE RUN (Executing Changes)\n")
    execute_actions(planned_actions)

    print("✅ Files organized successfully.")
