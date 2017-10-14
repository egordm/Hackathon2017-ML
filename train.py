import argparse
import pandas as pd

from tools.dataset import load_dataset
from tools.ml import pick_model


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data', type=str, default='data/dataset.csv', help='Path with all the data to train on.')
    parser.add_argument('--model', type=str, default='svm', help='Model to train with. [svm, naive_bayes, svm_grid_search]')
    parser.add_argument('--name', type=str, default='model_name', help='Name of the training session. Used to save the model.')
    run(parser.parse_args())

def run(settings):
    model = pick_model(settings.model)()
    X_train, X_valid, Y_train, Y_valid = load_dataset(settings.data)
    print('Training the model')
    model.train(X_train, Y_train)
    print('Prediction accuracy on training set: {}'.format(model.test(X_train, Y_train)))
    print('Prediction accuracy on validation set: {}'.format(model.test(X_valid, Y_valid)))





if __name__ == '__main__':
    main()
