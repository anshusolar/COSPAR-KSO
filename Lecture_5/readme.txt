Lecture 5

5.1 Read FIT-file from GOES and plot light curve(s), study and print header information -> Folder GOESlightcurve, script goes.py
    discuss hdu.info()
    Change x-axis from hours into seconds

5. Fit the leading edge of a light curve from GOES with different methods
5.2 Gauss' approximation (add labels and title)  -> CurevFitting->fitgoes2.py add a title to the 2nd plot
    amp/(np.sqrt(2*np.pi)*wid)) * np.exp(-(x-cen)**2 /(2*wid**2)

5.3 Non linear fit of a table -> CurevFitting->nonlinearfit.py add x-axis label, y-axis label and a title
    a * x / (b + x)
    Add x-axis label, y-axis label and a title. Add a grid in x and y


5.4 Image manipulation
    Resize an image -> Folder ImageManipulation, script imgresize.py
    Play with basewidth and copyre file size in explorer