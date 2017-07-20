CLASS=Coast

python gamma.py ${CLASS}*.bmp
./fisheye2pano -v 90,0 -h 180 -f angle ${CLASS}*.png pano.png