"""
Visualizer
"""
from typing import Union
import numpy as np
import pandas as pd
import plotly.graph_objs as go

import src.Transformation.DFLogTransformator as L


class Visualizer:
    """
    To visualize the Data as a bar chart or a histogram.
    """

    def __init__(self) -> None:
        self.my_colors = ["#2E2300", "#DB9501", "#375E97", "#3F681C", "#C05805"]

    def set_colors(self) -> None:
        """
        Set bar chart colors
        :return:
        """
        # TODO - Jirka will think about it

    # pylint: disable=too-many-arguments
    def create_plotly_bar_chart(self, df: pd.DataFrame, name_category_attr: str, \
        name_value_attr: Union[str, None] = None, log_y_data: bool = False, \
        log_y_axis: bool = False, log_base: int = 10)\
    -> None:
        """
        Creates a bar chart. If only one column is provided,
        it will automatically add a count column.
        :param df: pd.DataFrame.
        :param name_category_attr: String.
        :param name_value_attr: String or None.
        :param log_y_axis: Bool. Apply logarithmic transformation on the y (name_value_attr) Data.
        :param log_y_data: Bool. To change the y axis to logarithmic.
        :param log_base: Int. Logarithm base.
        :rtype: None.
        """

        df = df.copy()  # TODO - Find a less expensive way to avoid adding count column

        if name_value_attr is None:
            name_value_attr = 'count'
            df[name_value_attr] = df.groupby(
                [name_category_attr])[name_category_attr].transform('count')
            df = df.drop_duplicates(subset='ID').reset_index(drop=True)
        else:
            df = df.groupby([name_category_attr])[name_value_attr].sum().reset_index()

        if log_y_data:
            df = L.DFLogTransformator().fit_predict(df, name_value_attr, log_base)

        fig = go.Figure(data=[
            go.Bar(
                x=df[name_category_attr],
                y=df[name_value_attr],
                marker_color=self.my_colors[2]
            )])

        fig.update_layout(
            title={'text': 'Bar Chart', 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
            barmode='group',
            xaxis_title=name_category_attr,
            yaxis_title=name_value_attr
        )
        if log_y_axis:
            fig.update_yaxes(type='log')
            fig.update_layout(yaxis_title=name_value_attr + ' (log ' + str(log_base) + ')')

        fig.update_traces(marker_color=self.my_colors[2], marker_line_color=self.my_colors[0],
                          marker_line_width=1.5, opacity=1)
        fig.update_yaxes(showgrid=True, zeroline=True)
        fig.update_xaxes(
            showgrid=False,
            zeroline=True,
            tickvals=df[name_category_attr]
        )

        fig.show()
        # pylint: enable=too-many-arguments

    # pylint: disable=too-many-arguments
    def create_plotly_histogram_chart(self, df: pd.DataFrame, name_category_attr: str, \
        bins: int = 0, log_x_data: bool = False, log_y_axis: bool = False, \
        log_base: int = 10) \
    -> None:
        """
        Creates an histogram.
        :param df: pd.DataFrame.
        :param name_category_attr: String.
        :param bins: Int. Number of bins. Default is 0,
        which automatically choose the number of bins.
        :param log_x_data: Bool. Apply a logarithmic transformation to the x Data.
        :param log_y_axis: Bool. To change the y axis to logarithmic.
        :param log_base: Int. Logarithm base.
        :rtype: None.
        """

        df = df.copy()  # TODO - Find a less expensive way to avoid adding count column

        x_axis_name = name_category_attr
        y_axis_name = 'count'

        if log_x_data:
            df = L.DFLogTransformator().fit_predict(df, name_category_attr, log_base)
            x_axis_name = name_category_attr + ' (log ' + str(log_base) + ')'

        start = np.round(min(df[name_category_attr].values)) - 1 \
            if min(df[name_category_attr].values) >= 0.5 else 0
        end = np.round(max(df[name_category_attr].values))
        size = abs(start - end) / bins

        fig = go.Figure(data=[go.Histogram(
            x=df[name_category_attr],
            marker_color=self.my_colors[2],
            xbins=dict(start=start, end=end, size=size),
        )])
        fig.update_layout(
            title={'text': 'Histogram', 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
            barmode='group',
            xaxis_title=x_axis_name,
            yaxis_title='count'
        )

        if log_y_axis:
            fig.update_yaxes(type='log')
            fig.update_layout(yaxis_title=y_axis_name + ' (log)')

        fig.update_traces(marker_color=self.my_colors[2], marker_line_color=self.my_colors[0],
                          marker_line_width=1.5, opacity=1)
        fig.update_xaxes(showgrid=False, zeroline=True)
        fig.update_yaxes(showgrid=True, zeroline=True)
        fig.show()
        # pylint: enable=too-many-arguments
