"""
SaverAndLoader
"""

import os
import pickle

from typing import Optional, List, Any
from pandas import DataFrame

from src.Utils.ConfigHandler import ConfigHandler
from src.Utils.Timerer import Timerer


class SaverAndLoader(ConfigHandler): # type:ignore
    """
    To save and load Triplet and Timeseries DataFrames.
    """

    def __init__(self, config: Optional[ConfigHandler]) -> None:
        super(SaverAndLoader, self).__init__(config)
        self.t = Timerer()
        self.t.set_initial_timestamp(False)

    def save_triplet(self, df: DataFrame, file_name: str, attr_names: List[str],
                     where_to_store: str = "raw") -> None:
        """
        Saves a Data frame into Raw or Final folder.
        :param df: DataFrame. DF to save.
        :param file_name: String. File name without .pkl.
        :param attr_names: List of strings. List of attribute names of the index, time and value
        attributes.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        """
        self.t.set_meantime(print_results=False)

        attr_id = df[attr_names[0]].to_list()
        attr_time = df[attr_names[1]].to_list()
        attr_value = df[attr_names[2]].to_list()
        for_save = [attr_id, attr_value, attr_time]

        self._save_pkl(for_save, file_name, where_to_store)

        self.t.set_meantime(label="Saving Triplet Duration: ", print_results=True)

    def load_triplet(self, file_name: str, attr_names: List[str], where_to_store: str = "raw") \
            -> DataFrame:
        """
        Loads a pickle Data frame from Raw or Final folder.
        :param file_name: String. File  name without .pkl.
        :param attr_names: List of strings. List of attribute names of the index, time and value
        attributes.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        :return: DataFrame.
        """
        self.t.set_meantime(print_results=False)

        loaded = self._load_pkl(file_name, where_to_store)

        df = DataFrame()
        df[attr_names[0]] = loaded[0]  # Index attribute
        df[attr_names[1]] = loaded[1]  # Time attribute
        df[attr_names[2]] = loaded[2]  # Value attribute

        self.t.set_meantime(label="Loading Triplet Duration: ", print_results=True)

        return df

    def save_timeseries(self, df: DataFrame, file_name: str, attr_names: List[str],
                        where_to_store: str = "raw") -> None:
        """
        Saves a Data frame into Raw or Final folder.
        :param df: DataFrame. DF to save.
        :param file_name: String. File name without .pkl.
        :param attr_names: List of strings. List of attribute names of the index and value
        attributes.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        """
        self.t.set_meantime(print_results=False)

        attr_id = df[attr_names[0]].to_list()
        attr_timeseries = df[attr_names[1]].to_list()
        for_save = [attr_id, attr_timeseries]

        self._save_pkl(for_save, file_name, where_to_store)

        self.t.set_meantime(label="Saving Timeseries Duration: ", print_results=True)

    def load_timeseries(self, file_name: str, attr_names: List[str], where_to_store: str = "raw") \
            -> DataFrame:
        """
        Loads a pickle Data frame from Raw or Final folder.
        :param file_name: String. File  name without .pkl.
        :param attr_names: List of strings. List of attribute names of the index and value
        attributes.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        :return: DataFrame.
        """
        self.t.set_meantime(print_results=False)

        loaded = self._load_pkl(file_name, where_to_store)

        df = DataFrame()
        df[attr_names[0]] = loaded[0]  # Index attribute
        df[attr_names[1]] = loaded[1]  # Value attribute

        self.t.set_meantime(label="Loading Timeseries Duration: ", print_results=True)

        return df

    def delete_pkl(self, file_name: str, where_to_store: str) -> None:
        """
        To delete a file.
        :param file_name: String. File name without .pkl.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        """
        path = self._get_path(file_name, where_to_store)
        if os.path.exists(path):
            os.remove(path)

    def _save_pkl(self, for_save: List[Any], file_name: str, where_to_store: str) -> None:
        """
        Saves DataFrame as pkl file.
        :param for_save: List of list. Different parts of the divided DataFrame.
        :param file_name: String. File name without .pkl.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        """
        path = self._get_path(file_name, where_to_store)

        with open(path, 'wb') as handle:
            pickle.dump(for_save, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def _load_pkl(self, file_name: str, where_to_store: str) -> Any:
        """
        Loads a .pkl file.
        :param file_name: String. File name without .pkl.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        :return: Pickle file. Loaded Data from a .pkl file.
        """
        path = self._get_path(file_name, where_to_store)
        with open(path, 'rb') as handle:
            loaded = pickle.load(handle)

        return loaded

    def _get_path(self, file_name: str, where_to_store: str = "raw") -> str:
        """
        Returns path of a file for Raw or Final Data folder.
        :param file_name: String. File name without .pkl.
        :param where_to_store: String. Within a folder structure "raw" or "final".
        :return: String. Path.
        """
        if where_to_store == "raw":
            dir_path = self.try_get_config_value("path", "raw_data")
        elif where_to_store == "final":
            dir_path = self.try_get_config_value("path", "final_data")

        return os.path.abspath(os.path.join(
            dir_path, file_name + ".pkl"
        ))
