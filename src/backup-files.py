# This is a script to backup files using shutil

from pathlib import Path
import argparse
import logging
import shutil

# i configured logging
log_file = Path(__file__).with_name('backup.log')

logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s'
        )

# function to archive files and directories
def backup_file(path_to_backup: Path, destination_dir: Path):
    
    try:
        
        # in a case where no path_to_back provided
        if path_to_backup is None:
            print('No file provided')
            logging.error('No file provided')
            return

        # i check if the entered path for backup exists
        if not path_to_backup.exists():
            print(f'"{path_to_backup.name}" does not exist')
            logging.error(f'"{path_to_backup.resolve()}" does not exist')
            return

        # i check if the 'path_to_backup' is a file
        if path_to_backup.is_file():
            root_dir = path_to_backup.parent
            base_dir = path_to_backup.name
            
            # i alert the user that they can not backup empty files and immediately terminate the operation
            if path_to_backup.stat().st_size == 0:      # checking the file size
                print(f'Can not backup empty files')
                logging.error(f'Can not backup empty files')
                return

        # I check if the 'path_to_backup' is a directory
        elif path_to_backup.is_dir():
            root_dir = path_to_backup.parent
            base_dir = path_to_backup.name
            
            # i notify the user that they can not backup an empty directory and immediately terminate the operation
            if not any(path_to_backup.iterdir()):
                print(f'cannot back up empty directories')
                logging.error(f'cannot backup empty directories')
                return

        
        # I alert the user that the file path they entered is invalid
        else:
            print(f'{path_to_backup.name} is neither a file or directory')
            logging.error(f'{path_to_backup.resolve()} is neither a file or directory')
            return

        # incase it doesnt exist i will create the destination_dir
        destination_dir.mkdir(parents=True, exist_ok=True)

        # i create backup path with no suffix
        backup_name = destination_dir/path_to_backup.stem

        shutil.make_archive(str(backup_name), 'zip', root_dir = root_dir, base_dir = base_dir)

        print(f'Successfully backed up "{path_to_backup.name}" to "{backup_name.name}.zip"')
        logging.info(f'Successfully backed up "{path_to_backup.resolve()}" to "{backup_name.resolve()}.zip"')

    except Exception as e:
        print(f'Error during backup {e}')
        logging.error(f'Error during backup {e}')

def main():
    parser = argparse.ArgumentParser(description='a script to backup a file or directory')
    parser.add_argument('path_to_backup', nargs='?', default=None, help='path of file or directory to be backed up')
    parser.add_argument('destination', nargs='?', default='.', type=str, help='name of destination folder (default is current working directory)')
    args = parser.parse_args()

    path_to_backup = Path(args.path_to_backup).resolve() if args.path_to_backup else None
    destination_dir = Path(args.destination).resolve()
    backup_file(path_to_backup, destination_dir)

if __name__ == '__main__':
    main()
