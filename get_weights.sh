#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if 'data' directory does not exist and then create it
if [[ ! -e $DIR/data ]]; then
    mkdir "$DIR/weights"
else
    echo "'weights' dir already exists."
fi

gdown -O "$DIR/weights/ft_yolov8m.pt" "https://drive.google.com/uc?export=Download&id=1ztQiLMM_Shsc-fmnYmr7kuAj6kJPzr5J" 

