#!/bin/bash

# A script to run a matlab (plot) program on all data files of one folder.

# @author Sarah Lindner
# @date 27.08.2014

# Put path to directory which contains all the .txt files that should be plotted here. Make sure, that no other .txt files are in that folder.
directory='/mnt/Daten/measurements/SIQUTE/SIQ-BASD-SiV-M/SIQ-BASD-SiV-M5/spectra/try_plot_script'

cd $directory

for file in *.txt; do

	export file
	export directory

    echo plotting file: $file

	perl -pi -e 's/input_folder_name_here/$ENV{directory}/g' /mnt/Daten/my_programs/plot_spectrum/plot_spectrum.m
	perl -pi -e 's/input_file_name_here/$ENV{file}/g' /mnt/Daten/my_programs/plot_spectrum/plot_spectrum.m

	# Put path to the program which should be executed here.
	cd /mnt/Daten/my_programs/plot_spectrum

	# Put the program name without extension into the quotes.
	matlab -nodesktop -nosplash -r "plot_spectrum;quit;"

	cd $directory

	perl -pi -e 's/$ENV{directory}/input_folder_name_here/g' /mnt/Daten/my_programs/plot_spectrum/plot_spectrum.m
	perl -pi -e 's/$ENV{file}/input_file_name_here/g' /mnt/Daten/my_programs/plot_spectrum/plot_spectrum.m


done