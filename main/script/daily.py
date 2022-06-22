from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, Panel
from bokeh.layouts import column, row


def daily(df):
    def make_dataset(df):
        return ColumnDataSource(df)

    def style(plot):
        plot.title.align = "center"
        plot.title.text_font_size = "20pt"

        plot.xaxis.axis_label_text_font_size = "14pt"
        plot.xaxis.axis_label_text_font_style = "bold"
        plot.yaxis.axis_label_text_font_size = "14pt"
        plot.yaxis.axis_label_text_font_style = "bold"

        plot.xaxis.major_label_text_font_size = "12pt"
        plot.yaxis.major_label_text_font_size = "12pt"

        return plot

    def confirmed_plot(src):
        fig = figure(
            plot_width=1000,
            plot_height=400,
            title="Confirmed Cases",
            x_axis_label="Date",
            y_axis_label="Value",
            x_axis_type="datetime",
        )

        hover = HoverTool(
            tooltips=[
                ("As at", "@Date{%F}"),
                ("Confirmed Cases", "@Daily_Case"),
                ("Recovered Cases", "@Daily_Recovered"),
                ("Death Cases", "@Daily_Death"),
            ],
            formatters={"@Date": "datetime"},
            mode="vline",
        )

        fig.line("Date", "Daily_Case", source=src, color="gray")
        fig.diamond(
            "Date",
            "Daily_Case",
            source=src,
            fill_alpha=0.7,
            size=5,
            hover_fill_color="purple",
            hover_fill_alpha=1,
            color="cyan",
        )
        fig.add_tools(hover)

        fig = style(fig)

        return fig

    def recovered_plot(src):
        fig = figure(
            plot_width=800,
            plot_height=400,
            title="Recovered Cases",
            x_axis_label="Date",
            y_axis_label="Value",
            x_axis_type="datetime",
        )

        hover = HoverTool(
            tooltips=[
                ("As at", "@Date{%F}"),
                ("Confirmed Cases", "@Daily_Case"),
                ("Recovered Cases", "@Daily_Recovered"),
                ("Death Cases", "@Daily_Death"),
            ],
            formatters={"@Date": "datetime"},
            mode="vline",
        )

        fig.line("Date", "Daily_Recovered", source=src, color="gray")
        fig.diamond(
            "Date",
            "Daily_Recovered",
            source=src,
            fill_alpha=0.7,
            size=5,
            hover_fill_color="purple",
            hover_fill_alpha=1,
            color="lime",
        )
        fig.add_tools(hover)

        fig = style(fig)

        return fig

    def death_plot(src):
        fig = figure(
            plot_width=800,
            plot_height=400,
            title="Confirmed Death",
            x_axis_label="Date",
            y_axis_label="Value",
            x_axis_type="datetime",
        )

        hover = HoverTool(
            tooltips=[
                ("As at", "@Date{%F}"),
                ("Confirmed Cases", "@Daily_Case"),
                ("Recovered Cases", "@Daily_Recovered"),
                ("Death Cases", "@Daily_Death"),
            ],
            formatters={"@Date": "datetime"},
            mode="vline",
        )

        fig.line("Date", "Daily_Death", source=src, color="gray")
        fig.diamond(
            "Date",
            "Daily_Death",
            source=src,
            fill_alpha=0.7,
            size=5,
            hover_fill_color="purple",
            hover_fill_alpha=1,
            color="red",
        )
        fig.add_tools(hover)

        fig = style(fig)

        return fig

    def update(attr, old, new):
        province = menu.value

        df1 = df[df["Province"] == province]
        new_src = make_dataset(df1)

        src.data.update(new_src.data)

        return province

    option = list(df["Province"].value_counts().index)
    option.sort()

    menu = Select(options=option, value="DKI JAKARTA", title="Province")

    menu.on_change("value", update)

    controls = column(menu)

    province = menu.value

    df1 = df[df["Province"] == province]
    src = make_dataset(df1)

    c_plot = confirmed_plot(src)
    r_plot = recovered_plot(src)
    d_plot = death_plot(src)

    controls = row([controls]) 
    layout1 = row([c_plot])
    layout2 = row([r_plot], sizing_mode="scale_both")
    layout3 = row([d_plot], sizing_mode="scale_both")
    layout = column(controls, layout1, layout2, layout3)

    tab = Panel(child=layout, title="Daily Progression")

    return tab
