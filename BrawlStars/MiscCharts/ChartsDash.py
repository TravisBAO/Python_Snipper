from BrawlStars.MiscCharts.BarCharts import bar_chart_by_trophies, bar_chart_by_hero_parity


def charts_collection():
    with open('graph.html', 'a') as charts:
        # include_plotlyjs='cdn' only in the first figure and include_plotlyjs=False in subsequent.
        # No need to load javascript multiple times
        charts.write(bar_chart_by_trophies().to_html(full_html=False, include_plotlyjs='cdn'))
        charts.write(bar_chart_by_hero_parity().to_html(full_html=False, include_plotlyjs='cdn'))
