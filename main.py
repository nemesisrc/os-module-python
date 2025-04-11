# Complete Python `os` Module Tutorial

The `os` module in Python provides a way of using operating system dependent functionality. It allows you to interface with the underlying operating system that Python is running on, including Windows, Mac, and Linux.

## Table of Contents
1. [Importing the Module](#importing-the-module)
2. [File and Directory Operations](#file-and-directory-operations)
3. [Path Manipulation](#path-manipulation)
4. [Environment Variables](#environment-variables)
5. [Process Management](#process-management)
6. [System Information](#system-information)
7. [File Descriptors and Permissions](#file-descriptors-and-permissions)
8. [Walking Directory Trees](#walking-directory-trees)
9. [Miscellaneous Functions](#miscellaneous-functions)
10. [Best Practices](#best-practices)

## Importing the Module

```python
import os
```

## File and Directory Operations

### Creating and Removing Directories

```python
# Create a single directory
os.mkdir('new_directory')

# Create directories recursively (like mkdir -p)
os.makedirs('path/to/new/directory')

# Remove a file
os.remove('file.txt')

# Remove an empty directory
os.rmdir('empty_directory')

# Remove directories recursively
os.removedirs('path/to/directory')  # Removes all empty directories in path
```

### Listing Directory Contents

```python
# List files and directories in current directory
print(os.listdir('.'))

# List with full path (using list comprehension)
full_paths = [os.path.join('.', f) for f in os.listdir('.')]
```

### Checking Existence and Type

```python
# Check if path exists
print(os.path.exists('some_path'))

# Check if path is a file
print(os.path.isfile('file.txt'))

# Check if path is a directory
print(os.path.isdir('directory'))

# Check if path is a symbolic link
print(os.path.islink('symlink'))
```

## Path Manipulation

The `os.path` submodule is especially useful for path manipulations.

```python
# Join path components
path = os.path.join('dir', 'subdir', 'file.txt')

# Get absolute path
abs_path = os.path.abspath('relative/path')

# Get basename (filename) from path
filename = os.path.basename('/path/to/file.txt')  # 'file.txt'

# Get directory name from path
dirname = os.path.dirname('/path/to/file.txt')  # '/path/to'

# Split path into directory and filename
dir_name, file_name = os.path.split('/path/to/file.txt')

# Split filename into name and extension
name, ext = os.path.splitext('file.txt')  # ('file', '.txt')

# Get the size of a file
size = os.path.getsize('file.txt')

# Get modification time
mtime = os.path.getmtime('file.txt')  # returns timestamp
```

## Environment Variables

```python
# Get all environment variables
env_vars = os.environ

# Get a specific environment variable
home_dir = os.environ.get('HOME')  # or os.getenv('HOME')

# Set an environment variable (affects current process only)
os.environ['MY_VAR'] = 'value'

# Check if environment variable exists
if 'PATH' in os.environ:
    print("PATH exists")
```

## Process Management

```python
# Get current process ID
pid = os.getpid()

# Get parent process ID
ppid = os.getppid()

# Execute a system command (blocking)
return_code = os.system('ls -l')

# Spawn a new process
os.spawnl(os.P_NOWAIT, '/path/to/program', 'arg1', 'arg2')

# Exit the program with status code
os._exit(0)  # Use with caution - immediately terminates program
```

## System Information

```python
# Get current working directory
cwd = os.getcwd()

# Change working directory
os.chdir('/new/path')

# Get login name
username = os.getlogin()

# Get system name (e.g., 'Linux', 'Windows', 'Darwin' for Mac)
system_name = os.name  # Note: 'posix', 'nt', or 'java'

# More detailed platform info
import platform
print(platform.system())  # More detailed than os.name
```

## File Descriptors and Permissions

```python
# Open a file with low-level file descriptor
fd = os.open('file.txt', os.O_RDONLY)

# Read from file descriptor
data = os.read(fd, 100)

# Close file descriptor
os.close(fd)

# Change file permissions (Unix-like systems)
os.chmod('file.txt', 0o755)  # Octal notation for permissions

# Change owner and group (Unix-like systems, requires privileges)
os.chown('file.txt', uid, gid)

# Get file status
stat_info = os.stat('file.txt')
print(stat_info.st_size)  # File size
print(stat_info.st_mtime)  # Modification time
```

## Walking Directory Trees

```python
# Recursively walk through directory tree
for root, dirs, files in os.walk('/path/to/start'):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("---")
    
    # You can modify 'dirs' in-place to control traversal
    if 'skip_this_dir' in dirs:
        dirs.remove('skip_this_dir')
```

## Miscellaneous Functions

```python
# Rename a file or directory
os.rename('old.txt', 'new.txt')

# Create a symbolic link (Unix-like systems)
os.symlink('target', 'link_name')

# Create a hard link (Unix-like systems)
os.link('target', 'link_name')

# Get terminal size
rows, columns = os.get_terminal_size()

# Generate random bytes
random_bytes = os.urandom(16)

# Platform-specific path separator
print(os.sep)  # '/' on Unix, '\' on Windows

# Platform-specific path component separator
print(os.pathsep)  # ':' on Unix, ';' on Windows

# Platform-specific line separator
print(os.linesep)  # '\n' on Unix, '\r\n' on Windows
```

## Best Practices

1. **Use `os.path.join()`** instead of manual string concatenation for paths to ensure cross-platform compatibility.

2. **Check file/directory existence** before operations to avoid exceptions.

3. **Handle exceptions** - many os operations can raise OSError or its subclasses.

4. **Be careful with recursive operations** - double-check paths before deleting or modifying files recursively.

5. **Use context managers** for file operations when possible (though not directly part of os module).

6. **Consider pathlib** - in Python 3.4+, the pathlib module offers an object-oriented approach to filesystem paths that many find more intuitive.

7. **Be mindful of security** - especially when dealing with user-provided paths or executing system commands.

## Example: Practical Usage

Here's a practical example that combines several os module functions:

```python
import os

def clean_directory(directory, extensions_to_keep):
    """Remove files with extensions not in the keep list"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext.lower() not in extensions_to_keep:
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except OSError as e:
                    print(f"Error removing {file_path}: {e}")

# Usage
extensions = ['.txt', '.pdf', '.jpg']
clean_directory('/path/to/clean', extensions)
```

This tutorial covers most of the essential functionality of the os module. Remember that some functions may be platform-specific, so always check the documentation if you're writing cross-platform code.
