"""
folderStruct.py
Developer: Tim Weiser
Project: Messin
Date: 11/16/2018
References:
https://docs.python.org/2/library/os.html
https://www.tutorialspoint.com/python/string_lower.htm
https://stackoverflow.com/questions/13819496/what-is-different-between-makedirs-and-mkdir-of-os
https://stackabuse.com/creating-and-deleting-directories-with-python/
"""

import os


def make_work_directory(file_path, project_name):
    """
    Creates a bunch of folders into my structure of choice for animation projects
    :param str file_path: file path where the directory will be placed
    :param str project_name: name of the project
    """
    project_name_words = project_name.split()
    if len(project_name_words) == 1:
        final_project_name = project_name_words[0]
    else:
        final_project_name_words = []
        for i in range(len(project_name_words)):
            if i == 0:
                lower_word = project_name_words[0].lower()
                final_project_name_words.append(lower_word)
            else:
                final_project_name_words.append(project_name_words[i])
        final_project_name = ''.join(final_project_name_words)

    project_root = file_path + '\\' + final_project_name
    os.mkdir(project_root)

    root_folders = ['production', '_output']
    for folder in root_folders:
        os.mkdir(project_root + '\\' + folder)

    os.mkdir(project_root + '\\' + '_output' + '\\' + 'preview')
    os.mkdir(project_root + '\\' + '_output' + '\\' + 'final')

    prod_folder = project_root + '\\' + 'production'
    prod_folders = ['_other', 'PSD', '3D', 'AI', 'AE']
    for folder in prod_folders:
        os.mkdir(prod_folder + '\\' + folder)

    ae_folder = prod_folder + '\\' + 'AE'
    ae_assets_folders = ['ai', 'audio', 'footage', 'img', 'pre', 'projects', 'psd', 'ref']
    for folder in ae_assets_folders:
        os.makedirs(ae_folder + '\\' + 'assets' + '\\' + folder)


def main():
    """
    Sets variables for the file path where the directory will be created as well as the project's name
    """
    file_path = 'C:\Users\HomieSlice\Desktop'
    project_name = 'Dummy Project Name'
    make_work_directory(file_path, project_name)


if __name__ == '__main__':
    """
    Standard boilerplate to call the main() function.
    """
    main()
