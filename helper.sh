# Helper script for cleaning up stuff in the project.
# @author Walter Pach <wpach@email.sc.edu>
#!/bin/bash

if [ "$1" == "train" ]; then
  echo "Beginning training..."
  cd src/model
  python3 models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path=content/mobilenet_v2.config \
    --model_dir=training/ \
    --alsologtostderr \
    --num_train_steps=8000 \
    --sample_1_of_n_eval_examples=1 \
    --num_eval_steps=1000
  echo "Done training"
elif [ "$1" == "eval" ]; then
  echo "Beginning evaluation..."
  cd src/model
  python3 models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path=content/mobilenet_v2.config \
    --model_dir=training/ \
    --checkpoint_dir=training/
  echo "Done evaluating"
else
  echo "Usage: helper.sh [clean, eval, train]"
  echo "  clean - Cleans the temp/data files"
  echo "  eval  - Evaluated the models trained state"
  echo "  train - Trains the model from the last checkpoint"
fi
