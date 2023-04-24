read y;
printf "%.3f" $(echo "scale = 4; $y" | bc);