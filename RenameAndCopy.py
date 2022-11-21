import glob
import os
import shutil
import sys

sys.path.append("..")


def copyOriginFile(src_path, dst_path):
    # file_src = '..\\..\\source\\Sandbox\\engdata\\'
    # file_dst = 'FirmwareUpdate\\DFU\\'
    # path_r = os.getcwd()
    # os.chdir(src_path)
    # files = glob.glob('AX100PB*.bin')
    # print("files is %s" % files)
    # bin_name = files[0]
    # # copy file
    # os.chdir(path_r)
    # try:
    #     shutil.copyfile(os.path.join(src_path, bin_name), os.path.join(dst_path, bin_name))
    # except Exception as e:
    #     print(e)
    # finally:
    #     if os.path.exists(os.path.join(dst_path, bin_name)):
    #         print('Copy {} from {} to {} done!'.format(bin_name, src_path, dst_path))
    #     else:
    #         print('Failed to copy file:', bin_name)
    print(src_path)
    print(dst_path)


def copyAndRename_Binary():
    print(os.getcwd())
    # list files
    path_r = os.getcwd()
    os.chdir(file_src)
    files = glob.glob('AX100PB*.bin')
    print("files is %s" % files)
    file1 = files[0]

    # copy file
    os.chdir(str(path_r))

    print(os.getcwd())
    shutil.copyfile(os.path.join(file_src, file1), os.path.join(file_dst, file1))

    # delete file if file exists
    for item in os.listdir(file_dst):
        if item == new_name:
            os.remove(file_dst + item)
    new_file_name = new_name
    # rename\
    try:
        os.rename(file_dst + file1, file_dst + new_file_name)
    except Exception as e:
        print(e)


def copyAndRename_BinaryToH1Firmware():
    shutil.copyfile(os.path.join(file_src, file_name), os.path.join(file_dst, file_name))
    # delete file if file exists
    for item in os.listdir(file_dst):
        if item == "H1Firmware":
            os.remove(file_dst + item)
    new_file_name = "H1Firmware"
    # rename
    os.rename(file_dst + file_name, file_dst + new_file_name)


def copyEngdata(src_path, dst_path):
    dst_abspath = os.path.abspath(dst_path)
    src_abspath = os.path.abspath(src_path)
    file_list = []
    # delete files
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
        print("delete the default folder: ", dst_abspath)
    os.mkdir(dst_abspath)
    print("create a new empty folder: ", dst_path)
    batch_copy_file(src_abspath, dst_abspath)


def del_file(file_path):
    os.chdir(file_path)
    cur_path = os.getcwd()
    # os.chdir(file_path)
    print("currently path: ", cur_path)
    for item in os.listdir(cur_path):
        path_file = os.path.join(cur_path, item)
        if os.path.isfile(path_file):
            os.remove(path_file)
            print("delete default file: ", item)
        else:
            del_file(path_file)
    print("All files are deleted !")


def batch_copy_file(src_path, dst_path):
    for item in os.listdir(src_path):
        filepath = os.path.join(src_path, item)
        if os.path.isfile(filepath):
            shutil.copyfile(filepath, dst_path + "\\" + item)
            print("copy file: ", item)
        elif os.path.isdir(filepath):
            folderpath = os.path.join(dst_path, item)
            os.mkdir(folderpath)
            print("create folder: ", item)
            sub_src_path = filepath + "\\"
            sub_dst_path = folderpath + "\\"
            batch_copy_file(sub_src_path, sub_dst_path)
        else:
            print("error!!!")
    print("*" * 50)
    print("All files in {} are copied to {}.".format(src_path, dst_path))
    print("*" * 50)


def copy_specified_file():
    # src_path = "..\\"
    # dst_path = "..\\..\\source\\Sandbox\\"
    # filename = "compile_engdata.bat"
    for item in os.listdir(dst_path):
        if item == filename:
            os.remove(dst_path + item)
            print("delete the default file: ", filename)

    shutil.copyfile(src_path + filename, dst_path + filename)
    print("copy {} from {} to {}".format(filename, os.path.abspath(src_path), os.path.abspath(dst_path)))


if __name__ == '__main__':
    if sys.argv[1] == "copyBinary":
        file_src = sys.argv[2]
        file_dst = sys.argv[3]
        new_name = sys.argv[4]
        copyAndRename_Binary()
    elif sys.argv[1] == "copyBinaryToH1Firmware":
        file_src = sys.argv[2]
        file_name = sys.argv[3]
        file_dst = sys.argv[4]
        copyAndRename_BinaryToH1Firmware()
    elif sys.argv[1] == "copyEngdata":
        src_path = sys.argv[2]
        dst_path = sys.argv[3]
        copyEngdata(src_path, dst_path)
    elif sys.argv[1] == "copyOneFile":
        src_path = sys.argv[2]
        dst_path = sys.argv[3]
        filename = sys.argv[4]
        copy_specified_file()
    elif sys.argv[1] == "copyOriginFile":
        src_path = sys.argv[2]
        dst_path = sys.argv[3]
        copyOriginFile(src_path, dst_path)
    else:
        print("Error input!")
else:
    print("this is just to verify of invoking functions directly")