from pathlib import Path

import plotly.graph_objects as go


class PlotSaver:
    """
    This static class saves a created plot as a static image (by default PDF).
    """
    @staticmethod
    def save_plot(fig: go.Figure,
                  folder_path: Path,
                  file_name: str = 'plot.pdf'):
        """
        Saves a created plot (as a PDF file by default).
        :param go.Figure fig: the plot to be saved
        :param Path folder_path: where the file will be saved
        :param str file_name: the name of the saved file
        """
        folder_path.mkdir(parents=True, exist_ok=True)

        fig.write_image(folder_path / file_name)
