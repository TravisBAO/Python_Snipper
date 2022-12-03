from BrawlStars.Datas.ChartsDataPreparation import import_data_to_csv
from BrawlStars.Datas.ExportFromDatabase import fetch_data_from_database, bar_chart_trophies, sql_bar_trophies
from BrawlStars.MiscCharts.ChartsDash import charts_collection

if __name__ == "__main__":
    chart_data = fetch_data_from_database("brawlstars", sql_bar_trophies)
    import_data_to_csv(bar_chart_trophies, chart_data)
    charts_collection()
