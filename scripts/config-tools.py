#!/usr/bin/python

import os
from configparser import ConfigParser


def get_base_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    return parent_dir


def get_config(path):
    cfg = ConfigParser()
    cfg.read(path)
    return cfg


def update_cfg_file(src_cfg_path, dst_cfg_path):
    src_cfg = get_config(src_cfg_path)
    dst_cfg = get_config(dst_cfg_path)

    cfg_updated = False
    for section in src_cfg.sections():
        for option in src_cfg.options(section):
            if (
                dst_cfg.has_option(section, option)
                and option.endswith("pin")
                and src_cfg[section][option] != dst_cfg[section][option]
            ):
                cfg_updated = True
                print(
                    f"[{section}][{option}]: {src_cfg[section][option]} -> {dst_cfg[section][option]}"
                )
                dst_cfg.set(section, option, src_cfg.get(section, option))

    with open(dst_cfg_path, "w") as configfile:
        dst_cfg.write(configfile)

    if cfg_updated:
        print(f"updated: {dst_cfg_path}\n ")


def update_config(src_cfg_path, dst_cfg_path):
    """
    Updates destination configuration files recursively in the specified directory or a single file.

    Args:
        src_cfg_path (str): Path to the source configuration file.
        dst_cfg_path (str): Path to the destination configuration file or directory.

    Raises:
        FileNotFoundError: If the source or destination path is not found.

    Returns:
        None
    """
    if not os.path.exists(src_cfg_path):
        raise FileNotFoundError(f"Source path not found: {src_cfg_path}")

    if not os.path.exists(dst_cfg_path):
        raise FileNotFoundError(f"Destination path not found: {dst_cfg_path}")

    if os.path.isfile(dst_cfg_path):
        update_cfg_file(src_cfg_path, dst_cfg_path)
    elif os.path.isdir(dst_cfg_path):
        for root, dirs, files in os.walk(dst_cfg_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not os.path.islink(file_path) and file.endswith(".cfg"):
                    update_cfg_file(src_cfg_path, file_path)


# def compare_


def main():
    base_path = get_base_path()
    print(base_path)
    src_cfg_path = base_path + "/config/boards/m5p.cfg"
    dst_cfg_path = base_path + "/config/printers/vzbot"

    update_config(src_cfg_path, dst_cfg_path)


if __name__ == "__main__":
    main()
