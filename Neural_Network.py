from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

class NeuralNetwork:
    def __init__(self, activation_function, number_of_neurons, optimizer, dropout, epoch_size, learning_rate, batch_size):
        self.act = activation_function
        self.neurons = number_of_neurons
        self.opt = optimizer
        self.drop = dropout
        self.epoch_size = epoch_size
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        
    def build(self):
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(self.neurons, activation=self.act),
            tf.keras.layers.Dropout(self.drop),
            tf.keras.layers.Dense(10)                                      # units: dimension of output space (10)
        ])

        predictions = model(x_train[:1]).numpy()

        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        loss_fn(y_train[:1], predictions).numpy()

        opt = self.opt(learning_rate=self.learning_rate)

        model.compile(optimizer=opt,
                      loss=loss_fn,
                      metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=self.epoch_size, batch_size=self.batch_size)
    
        return(model.evaluate(x_test, y_test, verbose=2)[1])                # return the accuracy of the evaluation of the NN to use it for the get_fitness function in the MainProgramm


if __name__ == "__main__":
    nn = NeuralNetwork("relu", 128, "adam", 0.2)
    nn.build()
