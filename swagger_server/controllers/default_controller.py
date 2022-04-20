import os
import zipfile

from werkzeug.utils import secure_filename

from statistics.constants.constants import CACHE_UPLOADS_PATH
from statistics.files_size_statistics import ProcessData


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


def average_post(zfile):  # noqa: E501
    """Returns the average file size

    Returns the average file size # noqa: E501

    :param zfile: zip file that is a directory
    :type zfile: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    uploads_dir = create_cache_uploads_path()

    zipfile_name = zfile.filename
    path_to_zip_file = uploads_dir + '/' + zipfile_name
    zfile.save(os.path.join(uploads_dir, secure_filename(zipfile_name)))
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(uploads_dir)
    process_data = ProcessData()
    return process_data.get_average(os.path.abspath(remove_suffix(path_to_zip_file, '.zip')))


def create_cache_uploads_path():
    uploads_dir = CACHE_UPLOADS_PATH
    os.makedirs(uploads_dir, mode=0o777, exist_ok=True)
    os.chmod(uploads_dir, 0o777)
    return uploads_dir


def biggest_post(zfile=None):  # noqa: E501
    """Returns the biggest file

    Returns the biggest file # noqa: E501

    :param zfile: zip file that is a directory
    :type zfile: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    uploads_dir = create_cache_uploads_path()

    zipfile_name = zfile.filename
    path_to_zip_file = uploads_dir + '/' + zipfile_name
    zfile.save(os.path.join(uploads_dir, secure_filename(zipfile_name)))
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(uploads_dir)
    process_data = ProcessData()
    return process_data.get_biggest(os.path.abspath(remove_suffix(path_to_zip_file, '.zip')))


def histogram_post(zfile=None):  # noqa: E501
    """Returns the histogram of file sizes

    Returns the histogram of file sizes # noqa: E501

    :param zfile: zip file that is a directory
    :type zfile: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    uploads_dir = create_cache_uploads_path()

    zipfile_name = zfile.filename
    path_to_zip_file = uploads_dir + '/' + zipfile_name
    zfile.save(os.path.join(uploads_dir, secure_filename(zipfile_name)))
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(uploads_dir)
    process_data = ProcessData()
    return process_data.get_histogramBase64(os.path.abspath(remove_suffix(path_to_zip_file, '.zip')))


def smallest_post(zfile=None):  # noqa: E501
    """Returns the smallest file

    Returns the smallest file # noqa: E501

    :param zfile: zip file that is a directory
    :type zfile: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    uploads_dir = create_cache_uploads_path()

    zipfile_name = zfile.filename
    path_to_zip_file = uploads_dir + '/' + zipfile_name
    zfile.save(os.path.join(uploads_dir, secure_filename(zipfile_name)))
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(uploads_dir)
    process_data = ProcessData()
    return process_data.get_smallest(os.path.abspath(remove_suffix(path_to_zip_file, '.zip')))
