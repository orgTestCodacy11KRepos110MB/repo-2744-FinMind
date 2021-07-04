from IPython.display import HTML, display
from pyecharts import options as opts
from pyecharts.charts import Pie

from FinMind.schema import PiePlotSchema


def pie(
    pie_plot_data: PiePlotSchema,
    title: str = "title",
    series_name: str = "",
    width: str = "800px",
    height: str = "600px",
    radius: typing.List[str] = ["30%", "50%"],
    pos_left: str = "legft",
    pos_top: str = "10%",
    filename: str = "pie.html",
):
    """plot bar
    :param: bar_plot_data (:obj:FinMind.PiePlotSchema)
    PiePlotSchema(labels=labels, series=series)
    :param: title (str) default "title"
    :param: series_name (str) default ''
    :param: width (str) default "800px"
    :param: height (str) default "600px"
    :param: radius (List[str]) default ["30%", "50%"]
    :param: pos_left (str) default "legft"
    :param: pos_top (str) default "10%"
    :param: filename (str) default "pie.html", output filename
    :return: display pie
    :rtype pyecharts.charts.Pie
    """
    pie_plot = (
        Pie()
        .add(
            series_name=series_name,
            data_pair=[
                list(z) for z in zip(pie_plot_data.labels, pie_plot_data.series)
            ],
            radius=radius,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(
                pos_left=pos_left, orient="vertical", pos_top="10%"
            ),
        )
    )
    pie_plot.render(filename)
    display(HTML(filename=filename))
    return pie_plot
