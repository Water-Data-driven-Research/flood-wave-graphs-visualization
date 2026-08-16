import plotly.graph_objects as go

from fwg_visualization.plot.fwg_data_creator import FWGDataCreator


class FWGPlotter:
    """
    This class creates the plot of the received flood wave graph.
    """
    def __init__(self, fwg_data_creator: FWGDataCreator):
        """
        Constructor.
        :param FWGDataCreator fwg_data_creator: contains data for plotting
        """
        self.node_data_if = fwg_data_creator.node_data_if
        self.axis_data_if = fwg_data_creator.axis_data_if
        self.edge_data_if = fwg_data_creator.edge_data_if

    def get_graph_plot(self,
                       graph_name: str = 'Flood Wave Graph',
                       width: int = 1000,
                       height: int = 500) -> go.Figure:
        """
        Creates the plot of the graph.
        :param str graph_name: 'Flood Wave Graph' by default
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        :return go.Figure: the created plot
        """
        fig = go.Figure()

        node_trace = self.create_node_trace()
        fig.add_trace(trace=node_trace)

        edges = self.create_directed_edges()
        for edge in edges:
            fig.add_annotation(edge)

        self.create_layout(fig=fig,
                           graph_name=graph_name,
                           width=width,
                           height=height)

        return fig

    def create_node_trace(self) -> go.Scatter:
        """
        Creates the trace that includes the nodes of the graph.
        :return go.Scatter: the trace of the nodes
        """
        node_trace = go.Scatter(
            x=self.node_data_if.x_coordinates,
            y=self.node_data_if.y_coordinates,
            mode='markers',
            customdata=self.node_data_if.text_data,
            hovertemplate=
            '<b>%{customdata[0]}</b><br>'
            '%{customdata[1]} (%{customdata[2]})<br>'
            'Water level: %{customdata[3]}<br>'
            'Level group: %{customdata[4]}<extra></extra>',
            marker=dict(
                size=10,
                line_width=2,
                colorscale='YlOrRd',
                color=self.node_data_if.level_differences,
                colorbar=dict(
                    thickness=15,
                    title=dict(
                        text='Difference from level group',
                        side='right'
                    ),
                    xanchor='left',
                )
            )
        )

        return node_trace

    def create_directed_edges(self) -> list:
        """
        Creates the arrows that are the directed edges of the graph.
        :return list: a list of arrows (each represented as a dictionary)
        """
        directed_edges = []

        for edge_data_dict in self.edge_data_if.directed_edge_data:
            edge_dict = {
                'x': edge_data_dict['x_end'],
                'y': edge_data_dict['y_end'],
                'xref': 'x',
                'yref': 'y',
                'ax': edge_data_dict['x_start'],
                'ay': edge_data_dict['y_start'],
                'axref': 'x',
                'ayref': 'y',
                'showarrow': True,
                'arrowhead': 2,
                'arrowsize': 1.5,
                'arrowwidth': 1,
                'arrowcolor': '#337aa3'
            }
            directed_edges.append(edge_dict)

        return directed_edges

    def create_layout(self,
                      fig: go.Figure,
                      graph_name: str,
                      width: int,
                      height: int):
        """
        Creates the layout of the received figure.
        :param go.Figure fig: updates the layout of this figure
        :param str graph_name: the name of the graph ('Flood Wave Graph' by
               default)
        :param int width: the width of the image to be created (pixels)
        :param int height: the height of the image to be created (pixels)
        """
        fig.update_layout(
            title={
                'text': graph_name,
                'xanchor': 'center',
                'yanchor': 'top',
                'x': 0.5,
                'y': 0.98
            },
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=20, r=20, t=30),
            xaxis={
                'tickvals': self.axis_data_if.x_ticks,
                'ticktext': self.axis_data_if.x_tick_labels
            },
            yaxis={
                'tickvals': self.axis_data_if.y_ticks,
                'ticktext': self.axis_data_if.y_tick_labels
            },
            width=width,
            height=height
        )
