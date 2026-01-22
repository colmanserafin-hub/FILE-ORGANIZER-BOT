  Secure File Organizer Bot - MVP

A safe, two-phase file organization tool that simulates actions before execution.

Key Talking Points:
1. Safety First: "The program first runs in a dry-run phase where it simulates all actions and logs them. Only after explicit user approval does it execute the file movements."

2. Clean Architecture: "The two-phase design ensures clear separation of concerns - observation and action never mix."

3. User Experience: "Users can review exactly what will happen before committing to any changes."

4. Extensibility: "The configuration-based design makes it easy to add new file types or modify behavior."


Design Philosophy

Phase 1 = Observe (Dry Run)
Phase 2 = Act (Live Run)

The program never mixes both phases in the same execution, ensuring safety and predictability.

##  Execution Flow

```
Start Program
   ↓
Phase 1: Dry Run (Simulation)
   ↓
Show + Log Planned Actions
   ↓
Ask User Permission
   ↓
Phase 2: Live Run (Execution)
   ↓
End Program
```

##  Features

- ✅ **Safe Execution**: Dry run phase shows all planned actions before any files are moved
- ✅ **Clear Separation**: No mixing of simulation and execution logic
- ✅ **Comprehensive Logging**: All actions logged to `organizer.log`
- ✅ **User Confirmation**: Requires explicit "YES" confirmation before execution
- ✅ **Smart Categorization**: Automatically categorizes files by extension
- ✅ **Folder Protection**: Skips already organized folders

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Quick Start

1. **Create a test folder structure:**
   ```bash
   mkdir test_folder
   # Add some test files with different extensions
   ```

2. **Run the organizer:**
   ```bash
   python organizer.py
   ```

3. **Review the dry run output** and type `YES` to execute, or anything else to cancel.

## Configuration

Edit the configuration section in `organizer.py`:

```python
BASE_DIR = Path("test_folder")  # Change to your target folder
SKIP_FOLDERS = ["Images", "Videos", "Documents", "Others"]

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Others": []
}
```

## File Categories

- **Images**: `.jpg`, `.png`, `.jpeg`
- **Videos**: `.mp4`, `.mkv`
- **Documents**: `.pdf`, `.txt`, `.docx`
- **Others**: Any file that doesn't match the above categories

## Logging

All actions are logged to `organizer.log` with timestamps:
- Dry run simulations
- Actual file movements
- Timestamps for audit trail

## Testing

See [TESTING.md](TESTING.md) for detailed testing instructions.

### Demo Script:
1. Show the test folder with mixed files
2. Run the program and show the dry run output
3. Explain what would happen
4. Type "YES" to execute
5. Show the organized result
6. Show the log file

## Future Enhancements (Post-MVP)

- [ ] Configuration file (JSON/YAML) instead of hardcoded values
- [ ] Recursive folder scanning option
- [ ] Custom rules engine (date-based, size-based, etc.)
- [ ] GUI interface
- [ ] Undo functionality
- [ ] Duplicate file detection
- [ ] Progress bar for large operations
- [ ] Multi-threading for faster processing
- [ ] File metadata extraction (EXIF for images, etc.)

## 📄 License

This is an MVP project for demonstration purposes.

## 👤 Author

Colman Serafin Riwa
