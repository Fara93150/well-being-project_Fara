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