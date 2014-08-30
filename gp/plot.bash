#!/bin/bash
python gp.py
p=`date '+%d.%m.%H.%M.%S'`
echo $p
p+=".png"
echo $p
gnuplot <<- EOF
        plot "grossPitaevskii.dat" u 1:2 w d title "GP free particle solution"
	set xlabel "position"
        set ylabel "particle density (GP)"
        set term png
        set out "$p"
	rep
EOF
