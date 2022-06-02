from train import train_predict

# set input variables
input = "knn"

# local testing
def test_features():
    print(f"Testing training using {input}...")
    assert train_predict(input) == "knn", "Not correct output"

    
if __name__ == "__main__":
    test_features()