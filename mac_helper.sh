#!/bin/bash
# Helper script for cleaning up stuff in the project.
# @author Walter Pach <wpach@email.sc.edu>

if [ "$1" == "install" ]; then
  echo "= Installing Dependencies"
  brew -v > /dev/null

  if [ $? -ne 0 ]; then
    echo "  - Installing Homebrew"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  else
    echo "  - Homebrew installed. Skipping."
  fi

  echo "  - Installing wget"
  brew install -q wget
  echo "  - Installing protobuf"
  brew install -q protobuf
  echo "  - Installing grpc"
  brew install -q grpc

  echo "= Done Installing Dependencies"

elif [ "$1" == "train" ]; then
  echo "= Beginning training..."
  cd src/model
  python3 models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path=content/mobilenet_v2.config \
    --model_dir=training/ \
    --alsologtostderr \
    --num_train_steps=55000\
    --sample_1_of_n_eval_examples=1 \
    --num_eval_steps=2000
  echo "= Done training"
elif [ "$1" == "eval" ]; then
  echo "= Beginning evaluation..."
  cd src/model
  python3 models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path=content/mobilenet_v2.config \
    --model_dir=training/ \
    --checkpoint_dir=training/
  echo "= Done evaluating"
else
  echo "Usage: helper.sh [clean, eval, install, train]"
  echo "  clean   - Cleans the temp/data files"
  echo "  eval    - Evaluated the models trained state"
  echo "  install - Install dependencies"
  echo "  train   - Trains the model from the last checkpoint"
fi
