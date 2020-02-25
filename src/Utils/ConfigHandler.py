"""
ConfigHandler
"""
# pylint: disable=R0903
import configparser
import os
from configparser import NoSectionError, NoOptionError
from typing import Union, Any

from src.Exception.ConfigurationException import NoSectionException, ValueTypeException
from src.Exception.DataException import NoConfigFile

_DEFAULT_CONFIG_FOLDER_NAME = "MLTemplate"


class ConfigHandler:
    """
    Set ups global config.
    """

    def __init__(self, config: Union[None, configparser.ConfigParser]) -> None:
        """
        Wrapper
        :param config: None or configparser. If None, default configparser
                       "config.ini" is read from parent directory.
        """

        if config is None:
            self.config = configparser.ConfigParser()
            par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
            par_par_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))

            if os.path.basename(par_dir) in ("src", "notebooks", "tests"):
                self.config.read(os.path.join(par_par_dir, "config.ini"))
            elif os.path.basename(os.getcwd()) in _DEFAULT_CONFIG_FOLDER_NAME:
                self.config.read(os.path.join(os.getcwd(), "config.ini"))
            else:
                raise NoConfigFile
        else:
            self.config = config

    def try_get_config_value(self, section: str, sub_section: str, type_of_value: type = str) \
            -> Any:
        """
        Returns value from config in right type. If problem, raise an exception.
        :param section: str. Name of config section.
        :param sub_section: str. Name of config subsection.
        :param type_of_value: Type of value for conversion. Default is str.
        :return: Value of subsection.
        """
        try:
            if type_of_value == bool:
                value = self.config.getboolean(section, sub_section)
            else:
                value = type_of_value(self.config.get(section, sub_section))
        except NoSectionError:
            raise NoSectionException(f"No section: {section}")
        except NoOptionError:
            raise NoSectionException(f"No subsection: {sub_section}")
        except ValueError:
            raise ValueTypeException(f"Value of {sub_section} in {section} cannot "
                                     f"be converted to {type_of_value}")

        return value


if __name__ == "__main__":
    CH = ConfigHandler(None)

    print(CH.config.get("config_test", "message"))
    print(CH.try_get_config_value("config_test", "message"))
