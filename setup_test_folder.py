"""
Helper script to create a test folder with sample files for testing the organizer.
Run this before testing the organizer.py script.
"""

from pathlib import Path
import os

def create_test_environment():
    """Create a test folder with sample files of different types."""
    
    test_folder = Path("test_folder")
    
    # Create test folder if it doesn't exist
    test_folder.mkdir(exist_ok=True)
    
    # Sample files to create
    test_files = [
        "vacation.jpg",
        "screenshot.png",
        "family_photo.jpeg",
        "movie.mp4",
        "video_clip.mkv",
        "report.pdf",
        "notes.txt",
        "document.docx",
        "unknown_file.xyz",
        "random_data.dat"
    ]
    
    print("Creating test files...")
    for filename in test_files:
        file_path = test_folder / filename
        if not file_path.exists():
            file_path.touch()
            print(f"  ✓ Created: {filename}")
        else:
            print(f"  ⊙ Already exists: {filename}")
    
    print(f"\n✅ Test environment ready in '{test_folder}'")
    print(f"   Total files: {len(list(test_folder.glob('*')))}")
    print("\nYou can now run: python organizer.py")

if __name__ == "__main__":
    create_test_environment()
