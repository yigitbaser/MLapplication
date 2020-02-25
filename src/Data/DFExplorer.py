"""
Explorer
"""

from pandas import DataFrame

import src.Visualization.Visualization as V


class DFExplorer:
    """
    It prints and plots basic information about a DataFrame.
    """

    def __init__(self) -> None:
        self.visu = V.Visualizer()

    def print_attr_stats(self, df: DataFrame, min_unique: int = 20) -> None:
        """
        Prints df columns stats.
        :param df: DataFrame. Data to have its column stats printed.
        :param min_unique: Integer. Used to set the maximum allowed unique values for individual
        columns to be printed and plotted.
        """
        for attr in df.columns:
            self.print_single_attr_stats(df, attr, min_unique)

    @staticmethod
    def print_info_about_data_frame(df: DataFrame) -> None:
        """
        Print overall df stats.
        :param df: DataFrame. Data to have its stats printed.
        """
        print("\n")
        print("#############################################")
        print("\n")
        print(f"DataFrame type:")
        print(f"{str(type(df))}")
        print("DataFrame shape:")
        print(f"{str(df.shape)}")
        print(f"DataFrame head:")
        print(f"{df.head()}")
        print(f"DataFrame description:")
        print(f"{df.describe()}")
        print("\n")

    def print_single_attr_stats(self, df: DataFrame, attr_name: str, min_unique: int = 20) \
            -> None:
        """
        Print and plot individual stats of the df attributes.
        :param df: DataFrame. Data to have its attribute stats printed.
        :param attr_name: String. Name of the attribute to be analyzed.
        :param min_unique: Integer. Used to set the maximum allowed unique values for individual
        columns to be printed and plotted.
        """
        print("#############################################")
        print("\n")
        print(f"Attribute Name: {attr_name}")
        print(f" Attribute type: {df[attr_name].dtype}")
        print(f" Number of Null values: {df[[attr_name]].isnull().sum()[0]}")
        print(f" Number of unique values is:{len(df[attr_name].value_counts())}")
        print(f" Percentage of unique values is: "
              f"{len(df[attr_name].value_counts()) / df.shape[0]}"
              )
        if len(df[attr_name].value_counts()) < min_unique:
            pom = df[attr_name].value_counts()
            print("\n")
            print("Summation of unique values per ID:")
            print(pom)
            self.visu.create_plotly_bar_chart(df=df, name_category_attr=attr_name)
        if (df[attr_name].dtype == "float64" or df[attr_name].dtype == "int64") and \
                df[[attr_name]].isnull().sum()[0] == 0:
            self.visu.create_plotly_histogram_chart(df=df, name_category_attr=attr_name)
        print("\n")
