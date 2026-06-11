# Kali Linux Terminal & OS Fundamentals

## ⌨️ System & Terminal Shortcuts
* `setxkbmap tr` : Change keyboard layout to Turkish.
* `Tab` : Auto-complete file/directory names or commands.
* `Ctrl + L` (or `clear`) : Clear the terminal screen.
* `Ctrl + C` : Kill/Stop the currently running process.

## 📁 Directory & File Operations (Navigation & Management)
* `pwd` : Print working directory (Mevcut konumu gösterir).
* `ls -la` : List all files including hidden ones with details.
* `cd folder_name` : Change directory (Belirtilen klasöre geçer).
* `cd ..` : Move up one directory level (Bir üst dizine çıkar).
* `cd ~` : Navigate to the current user's home directory.
* `mkdir folder_name` : Create a new directory.
* `touch file.txt` : Create a new empty file.
* `cp source destination` : Copy files or directories.
* `mv source destination` : Move or rename files.
* `rm file_name` : Remove a specific file.
* `rm -rf folder_name` : Force remove a directory and its contents.

## 📝 Text Editors
* `nano file.txt` : Quick terminal text editor.
* `cat file.txt` : Read and output the content of a file.

## 📦 Package Management (APT)
* `sudo apt update` : Update the package list.
* `sudo apt install package_name` : Install a new package.
* `sudo apt remove package_name` : Remove an installed package.