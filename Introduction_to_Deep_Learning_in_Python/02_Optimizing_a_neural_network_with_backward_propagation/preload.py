def predict_with_network(input_data_row, weights):
    # TODO: implement this
    pass


def get_slope(input_data, target, weights):
    preds = (input_data * weights).sum()
    error = preds - target
    return 2 * input_data * error


def get_mse(input_data, target, weights):
    # TODO: implement this
    pass
