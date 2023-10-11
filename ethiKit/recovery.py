import pytsk3

def recover_deleted_files(image_path):
    img = pytsk3.Img_Info(image_path)
    fs = pytsk3.FS_Info(img)

    # Iterate through all the directories and files in the file system
    for directory_entry in fs.recurse():
        if directory_entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DELETED:
            file_path = '/'.join(directory_entry.info.fs_file.info.meta.addr)
            print(f"Recovered file: {file_path}")

# Example usage
if __name__ == "__main__":
    disk_image_path = input("Enter the path to the disk image: ")
    recover_deleted_files(disk_image_path)
