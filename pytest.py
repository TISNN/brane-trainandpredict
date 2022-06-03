from train import train_predict

# set input variables
input = "py_decision_tree" #py_knn

# local testing
def test_train():
    print(f"Testing training pipeline using {input}...")
    output = train_predict(input)
    assert output[:8] == "Accuracy", "Not correct output"
    print(output)
    print('Testing is done, no problem')

    
if __name__ == "__main__":
    test_train()