# Backup Files
This a Python tool to backup files and directories by compressing and archiving them.
Backup is important for keeping records for future use, regulatory compliance(e.g GDPR, PCI DSS) and date safety.
I have dockerised the tool and integrated it into a CI/CD pipeline so that it can be easily deployed and used.

## Purpose
This tool assist users e.g analysts, developers, and others to:
- backup files and directories for future use.
- Comply with regulations (e.g. GDPR, ISO) regarding safe keeping of data.

## Requirements
- Python3 must be installed to run the tool.
- The tool currently runs via the command-line interface (CLI).

## Usage
From the command line, the tool can be run like this:

```bash
python3 backup-files.py <path_to_backup> <destination_path>
   ```
Or if you want to use the current working directory as the default destination 

```bash
python3 backup-files.py <path_to_backup> 
   ``` 
## Docker
I dockerised the tool for easy deployment and integration into CI/CD pipeline

## Logging
The tool produces logs files that are an essential part of tracking when backups were made and if any errors occurred.
