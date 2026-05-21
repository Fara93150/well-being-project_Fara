class KNN :
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        distances = []  
    
        for neighbor_index, point in enumerate(self.X_train):
         distances.append((((X - point)**2)**0.5, neighbor_index))
        distances.sort()
        k_nearest = distances[:self.k]
        labels = []
        for _, neighbor_index in k_nearest:
            labels.append(self.y_train.iloc[neighbor_index])
        return max(labels, key=labels.count)
    def evaluate(self, X, Y):
        correct_predictions = []
        for row_index, row in enumerate(X):
          predicted_label = self.predict(row)
          if predicted_label == Y.iloc[row_index]:
            correct_predictions.append(1)
        prediction_accuracy = sum(correct_predictions) / len(X)
        return prediction_accuracy
        for k in k_values:
            knn = KNN(k)
            knn.fit(X, Y)
            accuracy = knn.evaluate(X_test, Y)
            print(f"K: {k}, Accuracy: {accuracy:.4f}")
            def grid_search(self, X, Y, k_values=[1, 3, 5, 7, 9]):
             best_score = 0
             best_k = None
        for k in k_values:
         knn = KNN(k)
         knn.fit(X, Y)
         score = knn.evaluate(X, Y)
        if score > best_score:
            best_score = score
            best_k = k
        return best_k