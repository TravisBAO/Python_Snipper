from BrawlStars.Datas.ChartsDataPreparation import import_data_to_csv
from BrawlStars.Datas.ExportFromDatabase import fetch_data_from_database, bar_chart_trophies, sql_bar_trophies, \
    sql_line_name, line_chart_name
from BrawlStars.MiscCharts.ChartsDash import charts_collection
import BrawlStars.MiscCharts.HistogramCharts
from BrawlStars.MiscCharts.LineCharts import line_chart_by_name

if __name__ == "__main__":
    # bar chart, trophies
    chart_data = fetch_data_from_database("brawlstars", sql_bar_trophies)
    import_data_to_csv(bar_chart_trophies, chart_data)
    # charts_collection()
    BrawlStars.MiscCharts.HistogramCharts.histogram_chart_by_hero_trophy()

    # line chart, name
    # chart_data = fetch_data_from_database("brawlstars", sql_line_name)
    # import_data_to_csv(line_chart_name, chart_data)
    # line_chart_by_name()


