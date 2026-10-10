# o-----------------------o
# |   PodSync by Niamh    |
# |        10/9/26        |
# o-----------------------o

# Copyright (C) 2026 Niamh-LabbRatt

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Libraries
import os
import sys
import glob
import shutil
import contextlib
from pathlib import Path

# Set the location of your music folders
# syncfs = local pc sync folder
# ipodfs = ipod root folder
syncfs = sys.argv[1]
ipodfs = sys.argv[2]

# This function clears the terminal when called
def clearTerm():
    # os.name is 'nt' for Windows, 'posix' for macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# Check if the diven directories exist and are readable/writable
def checkDir():
    # Checking if the sync folder exists
    if not Path(syncfs).is_dir():
        print("Error:", syncfs, "is not a directory or does not exist.")
        sys.exit(1)
    # Checking if the ipod folder exists
    if not Path(ipodfs).is_dir():
        print("Error:", ipodfs, "is not a directory or does not exist.")
        sys.exit(1)
    # Checking if the sync folder is readable/writable
    if not os.access(syncfs, os.R_OK | os.W_OK):
        print("Error:", syncfs, "is not readable and/or writable.")
        sys.exit(1)
    # Checking if the ipod folder is readable/writable
    if not os.access(syncfs, os.R_OK | os.W_OK):
        print("Error:", ipodfs, "is not readable and/or writable.")
        sys.exit(1)

# Custom copy function, spits out a log when copying file
def copyLog(src, dst):
    print(f"Copying: {src}")
    return shutil.copy2(src, dst)

# Initialization
clearTerm()

print("PodSync\nCopyright (C) 2026 Niamh\n")

print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions. Refer to "+"LICENSE.txt"+" for details.\n")

checkDir()

print("Local Folder: " + syncfs)
print("Device Folder: " + ipodfs + "\n")

start = input("Are you sure you would like to sync these folders? Every synced file on your rockbox device will be deleted and replaced.\n(Y/N): ")

if start == "y":
    try:
        with contextlib.suppress(FileNotFoundError):
            # Deletes all files in the specified folders
            shutil.rmtree(ipodfs+"Music")
            shutil.rmtree(ipodfs+"Pictures")
            shutil.rmtree(ipodfs+"Videos")

        print("Starting to copy files.")

        # Copies all files from the sync folder to the ipod.
        shutil.copytree(
            syncfs+"Music",
            ipodfs+"Music",
            copy_function=copyLog
        )

        shutil.copytree(
            syncfs+"Pictures",
            ipodfs+"Pictures",
            copy_function=copyLog
        )

        shutil.copytree(
            syncfs+"Videos",
            ipodfs+"Videos",
            copy_function=copyLog
        )

        # Prompts to delete all database files.
        dbrprompt = input("\nDelete old database files? (Y/N): ")
        print("")
        if dbrprompt == "y":
            dbfolder = ipodfs+".rockbox/database_**.tcd"
            dbfiles = glob.glob(dbfolder)

            for file_path in dbfiles:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as de:
                    print(f"Error deleting {file_path}: {de}")

    except OSError as e:
        print(f"Error syncing: {e}")

print("\nSyncing complete, have fun!")
