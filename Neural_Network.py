from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

class NeuralNetwork:
    def __init__(self, activation_function, number_of_neurons, optimizer):
        self.act = activation_function
        self.neurons = number_of_neurons
        self.opt = optimizer

        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(self.neurons, activation=self.act),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10)
        ])

        predictions = model(x_train[:1]).numpy()

        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        loss_fn(y_train[:1], predictions).numpy()

        model.compile(optimizer=self.opt,
                      loss=loss_fn,
                      metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=5)


nn = NeuralNetwork("relu", 128, "adam")