from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd

from tensorflow.python.framework.versions import VERSION
if VERSION >= "2.0.0a0":
    import tensorflow.compat.v1 as tf
else:
    import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

train_csv_input = "../data/train_labels.csv"
test_csv_input = "../data/test_labels.csv"
train_output_path = "../model/train.record"
test_output_path = "../model/test.record"
image_dir = "../data/images"

def class_text_to_int(row_label):
    if row_label == 'military tank':
        return 1
    elif row_label == 'military aircraft':
        return 2
    elif row_label == 'military truck':
        return 3
    elif row_label == 'civilian aircraft':
        return 4
    elif row_label == 'civilian car':
        return 5
    elif row_label == 'military helicopter':
        return 6
    else:
        return None

def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)

    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def create_tf_record(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()

    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    # Add all of the objects to the arrays.
    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_record = tf.train.Example(features=tf.train.Features(feature = {
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes)
    }))

    return tf_record

def create_record(csv_input, output_path):
    print(f"Creating record: {output_path}")

    global image_dir
    writer = tf.python_io.TFRecordWriter(output_path)
    path = os.path.join(os.getcwd(), image_dir)

    print("\tReading CSV label file...")
    examples = pd.read_csv(csv_input)
    grouped = split(examples, 'filename')

    print("\tBeginning compilation...")

    for group in grouped:
        tf_record = create_tf_record(group, path)
        writer.write(tf_record.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), output_path)
    print(f"Successfully created the TFRecords: {output_path}")

create_record(train_csv_input, train_output_path)
create_record(test_csv_input, test_output_path)
