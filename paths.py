import errno
import os


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as ex:
        import errno
        if ex.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def replace_ext(path, new_ext):
    root, ext = os.path.splitext(path)
    return root + new_ext

