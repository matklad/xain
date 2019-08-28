import os

import tensorflow as tf

from xain.generator import data

local_generator_datasets_dir = os.path.expanduser("~/.xain/generator/datasets")

cifar10 = tf.keras.datasets.cifar10
fashion_mnist = tf.keras.datasets.fashion_mnist

datasets = {
    "cifar10_random_splits_10": {
        "keras_dataset": cifar10,
        "transformers": [data.random_shuffle],
        "transformers_kwargs": [{}],
        "num_splits": 10,
        "validation_set_size": 5000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_01cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 1}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_02cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 2}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_03cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 3}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_04cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 4}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_05cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 5}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_06cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 6}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_07cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.remove_balanced, data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [
            # we need to remove 100 elements from the full xy_train so the
            # 540 examples per partition are reduced to 539 and therefore
            # divisible by 7
            {"num_remove": 100},
            {"num_partitions": 100, "cpp": 7},
        ],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": False,
    },
    "fashion_mnist_100p_08cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.remove_balanced, data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [
            # we need to remove 400 elements from the full xy_train so the
            # 540 examples per partition are reduced to 536 and therefore
            # divisible by 8
            {"num_remove": 400},
            {"num_partitions": 100, "cpp": 8},
        ],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": False,
    },
    "fashion_mnist_100p_09cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 9}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_10cpp": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.sorted_labels_sections_shuffle],
        "transformers_kwargs": [{"num_partitions": 100, "cpp": 10}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
    "fashion_mnist_100p_IID_balanced": {
        "keras_dataset": fashion_mnist,
        "transformers": [data.balanced_labels_shuffle],
        "transformers_kwargs": [{"num_partitions": 100}],
        "num_splits": 100,
        "validation_set_size": 6000,
        "assert_dataset_origin": True,
    },
}
