import re

num_classes = 6
batch_size = 4
num_steps = 50000
num_eval_steps = 1000

train_record_path = "./train.record"
test_record_path = "./test.record"
model_dir = "./training"
labelmap_path = "labelmap.pbtxt"
pipeline_config_path = "content/mobilenet_v2.config"
fine_tune_checkpoint = "content/mobilenet_v2/mobilenet_v2.ckpt-1"

with open(pipeline_config_path) as f:
    config = f.read()

with open(pipeline_config_path, 'w') as f:
    config = re.sub('label_map_path: ".*?"', 'label_map_path: "{}"'.format(labelmap_path), config)

    config = re.sub(
        'fine_tune_checkpoint: ".*?"',
        'fine_tune_checkpoint: "{}"'.format(fine_tune_checkpoint),
        config
    )

    config = re.sub(
        '(input_path: ".*?)(PATH_TO_BE_CONFIGURED/train)(.*?")',
        'input_path: "{}"'.format(test_record_path), config
    )

    config = re.sub(
        '(input_path: ".*?)(PATH_TO_BE_CONFIGURED/val)(.*?")',
        'input_path: "{}"'.format(test_record_path), config
    )

    config = re.sub(
        'num_classes: [0-9]+',
        'num_classes: {}'.format(6), config
    )

    config = re.sub(
        'batch_size: [0-9]+',
        'batch_size: {}'.format(batch_size), config
    )

    config = re.sub(
        'num_steps: [0-9]+',
        'num_steps: {}'.format(num_steps), config
    )

    f.write(config)
    f.close()
    print('Finished writing configuration')
