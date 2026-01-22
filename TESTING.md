# 🧪 Testing Guide - File Organizer Bot

## Prerequisites

1. Python 3.6+ installed
2. A test folder with sample files

## 🎯 Test Scenarios

### Test 1: Basic File Organization

**Setup:**
1. Create `test_folder` in the project root
2. Add sample files:
   - `photo1.jpg`
   - `photo2.png`
   - `video1.mp4`
   - `document1.pdf`
   - `random.txt`
   - `unknown.xyz`

**Expected Behavior:**
- Dry run shows all files and their target folders
- After typing "YES", files are moved to appropriate folders
- Log file contains all actions

**Verification:**
```bash
# Check folder structure
ls test_folder/
ls test_folder/Images/
ls test_folder/Videos/
ls test_folder/Documents/
ls test_folder/Others/
```

### Test 2: Empty Folder

**Setup:**
- Empty `test_folder` (or folder with only subfolders)

**Expected Behavior:**
- Program exits with "No files to organize" message
- No folders created
- No log entries for moves

### Test 3: Already Organized Files

**Setup:**
1. Create `test_folder` with:
   - `Images/photo1.jpg` (already in Images folder)
   - `random.pdf` (in root)

**Expected Behavior:**
- Only `random.pdf` is shown in dry run
- `Images` folder is skipped (as configured)
- `random.pdf` moves to `Documents` folder

### Test 4: Cancellation Test

**Setup:**
- Any test folder with files

**Steps:**
1. Run the program
2. Review dry run output
3. Type anything other than "YES" (e.g., "no", "cancel", "n")

**Expected Behavior:**
- Program exits with cancellation message
- No files are moved
- Dry run actions are still logged

### Test 5: Case Sensitivity

**Setup:**
- Files with mixed case extensions:
  - `photo.JPG`
  - `document.PDF`
  - `video.MP4`

**Expected Behavior:**
- All files are correctly categorized (case-insensitive matching)
- Files moved to appropriate folders

### Test 6: Log File Verification

**Steps:**
1. Run a complete test (dry run + execution)
2. Check `organizer.log`

**Expected Content:**
- Timestamp for each action
- `[DRY RUN]` entries for simulation
- `MOVED` entries for actual execution
- Clear audit trail

## 🧹 Test Cleanup Script

Create a simple cleanup script to reset test environment:

```python
# cleanup_test.py
import shutil
from pathlib import Path

test_folder = Path("test_folder")
if test_folder.exists():
    shutil.rmtree(test_folder)
    test_folder.mkdir()
    print("Test folder cleaned!")
```

## 📊 Test Checklist

- [ ] Basic file organization works
- [ ] Empty folder handled gracefully
- [ ] Already organized folders are skipped
- [ ] Cancellation prevents file movement
- [ ] Case-insensitive extension matching
- [ ] Log file contains all actions
- [ ] "Others" category works for unknown extensions
- [ ] Multiple files of same type organized correctly
- [ ] Folders are created if they don't exist
- [ ] No errors when running twice on same folder

## 🐛 Common Issues & Solutions

### Issue: "No such file or directory"
**Solution:** Ensure `test_folder` exists before running

### Issue: Files not moving
**Solution:** Check file permissions and ensure files aren't open in another program

### Issue: Log file not created
**Solution:** Check write permissions in the current directory

## 🎬 Demo Test Run

For a complete demo, use this test setup:

```bash
# Create test structure
mkdir test_folder
cd test_folder

# Create sample files (Windows PowerShell)
New-Item -ItemType File -Name "vacation.jpg"
New-Item -ItemType File -Name "screenshot.png"
New-Item -ItemType File -Name "movie.mp4"
New-Item -ItemType File -Name "report.pdf"
New-Item -ItemType File -Name "notes.txt"
New-Item -ItemType File -Name "mystery.xyz"

cd ..
python organizer.py
```

This creates a realistic test scenario perfect for demonstrations.
