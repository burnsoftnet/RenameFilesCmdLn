import os
import pathlib


class RenameFunctions:

    @staticmethod
    def rename_files_keep_extension(folder_path: str, prefix: str,
                                    keep_org_name: bool = False):
        """
        Renames all files in a given folder, adding a prefix and keeping the extension.
        Args:
            folder_path (str): The path to the directory containing the files.
            prefix (str): The new prefix to add to the file names.
            keep_org_name (bool): Keep the original name and append the new name in the front.
        """
        print(f"Renaming files in: {folder_path}")

        # Use pathlib for a modern and clean approach
        p = pathlib.Path(folder_path)

        if not p.is_dir():
            print(f"Error: The specified folder path '{folder_path}' is not a valid directory.")
            return
        i: int = 1
        for file_path in p.iterdir():
            # Check if it's a file and not a directory
            if file_path.is_file():
                # Get the current file name without the extension (stem) and the extension
                old_name = file_path.stem
                extension = file_path.suffix

                # Create the new file name
                if keep_org_name:
                    new_name = f"{prefix}_{old_name}{extension}"
                else:
                    new_name = f"{prefix}_{i:05d}{extension}"

                new_file_path = file_path.with_name(new_name)
                # Rename the file
                try:
                    file_path.rename(new_file_path)
                    print(f"Renamed '{file_path.name}' to '{new_file_path.name}'")
                    i = i + 1
                except OSError as e:
                    print(f"Error renaming file {file_path.name}: {e}")

        print("\nAll files have been processed.")
