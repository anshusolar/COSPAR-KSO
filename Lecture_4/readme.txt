Lecture 4

- 4.1 Read and plot images of different graphic format and save it in another format -> Folder 2Dimages, script imgplot.py
      Play with different image-files in lines 13...17 by commenting on/off (#)
      Play with x- and y-labels, save result as jpg
      
- 4.2 Plot a bar chart out of a table -> Folder BarChart, script barchart.py
      Play with performance and transparency alfa
      Change color of the bars and increase fontsize of labels
      Add another language to the bar

- 4.3 Plot a pie chart out of a table -> Folder PieChart, script piechart.py
      Play with labels and sizes, figure size, shadow and startangle
      Check parameters of pie using ctrl+i
      Add anther piece of pie with another animal and explode it by 20%

- 4.4 Plot histograms out of self generated random number -> Folder Histogram, script histogram.py
      Play with histogram type, color, transparency (alfa)
      Add a grid to the plot

- 4.5 download event-list from FTP-server at SWPC (NOAA) -> Folder eventlinst, script ftpdownload.py
      if internet is not working, then copy 20??_events.tar.gz from distribution disc and perform script 4.6
      Try to download missing files from 2019 and 2020, if available

- 4.6 Load script /../Lectures/Lecture_4/event_reader.py  <- new
      Read zipped event-list for 2010-2019 and select type II. If internet is not working
      comment (# or """) lines 24-28
      If internet is working download NOAA-eventlist by un-commenting lines 24-28
      Select year and burst type in lines 15 and 16
      After successfully generating list for type II, do the same for type I, III, IV and V
      Check generated lists with your texteditor, e.g. notepad
      During lecture 7, we will generate histograms for velocity of CME out of type II
