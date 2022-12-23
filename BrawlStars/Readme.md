# Guide for the Brawl Stars Scripts
Describe how to use the inbuilt functions to calculate and summarize the trophies and why the functions are there.

## CalcPowerPoints.py
### up_to_level(level=20)
To calculate the trophies when all stars reach the dedicated level.  
@param level: the dedicated level; the default value is 20.

### up_to_trophies(trophy=500)
To calculate the trophies when all stars reach the dedicated trophy  
@param trophy: default= 500, and value would be the level line 524, 549, 574, 599

### required_power_points()
This is to calculate that if reaching the highest level, how many power points are required for each hero.

### season_end_decrement()
This is to calculate the trophies when the current season ends.

## CalcTrophies.py
### to_reach_current_rank()
This is to calculate the trophies that if the stars reach their current ranks. 
This function is needed when the hero loses some trophies, but I want to know the maximal trophies.

## BrawlStarData.py
All the stars data are in this file.

## ChartsDataPreparation.py
### import_data_to_csv(csv_head, csv_data)
To collect data to format csv, which is required for package plotly  
@param csv_head: first lane of csv file  
@param csv_data: test data

## ExportFromDatabase.py
### fetch_data_from_database(database, sql_query)
collect data form database  
@param database: target database  
@param sql_query: dedicated sql query: all the queries are included in ExportFromDatabase.py  

## ImportToDatabase.py
This file is to operate the database.
- connect_to_database(database)
- insert_data_to_database(database, table)
- update_data_to_database(database, table)

## folder MiscCharts
All the used charts from plotly
- BarCharts.py
- ChartsDash.py (dashboard of multiple charts)
- HistogramCharts.py
- LineCharts.py
- ScatterCharts.py

## folder VariableSorts
All the used sorts from plotly
- BubbleSort.py