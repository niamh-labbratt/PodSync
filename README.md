# PodSync
This is mostly just a little tool I made for myself to sync my rockbox ipod with a folder on my pc, but I hope it can help you too.

## About

PodSync is a CLI tool for syncing a folder to your rockbox device.

**Current Features:**

1. Copies all files from a sync folder to a rockbox device.
2. (Optional) Removes rockbox database files to refresh the list.

**Planned Features:**
This program is unfinished, I plan to add these eventually.

1. Optional subfolders
2. File-based configuration
3. Automatically run when device is connected

## Usage
**BEFORE YOU USE**: This has only been tested on my 4th gen IPod. I have no guarantee your device will work.

First, you need a folder to sync from with the subfolders: "Music", "Pictures", and "Videos".

(You don't have to put any files into them, they just have to exist.)

And now, simply run the python script in a terminal, with the first argument being the folder to sync, and the second being the rockbox root directory.

Example:

`podsync.py /path/to/sync/dir/ /path/to/rockbox/`

---
