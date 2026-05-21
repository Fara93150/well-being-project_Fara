import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, GridSearchCV

def load_data(csv_path, target_col="target"):
	df = pandas.read_csv(csv_path)
@@ -27,18 +27,14 @@ def evaluate(X_normalized, Y, n_neighbors=5, n_splits=10, scoring="f1_weighted")
	return scores


def find_optimal_kvalue(X_normalized, Y, n_splits=10, scoring="f1_weighted", n_neighbors_range=range(1, 100,2)):
	"""Grid Search CV"""

	dict_of_k_scores = {}
	
	for n_neighbors in n_neighbors_range:
		scores = evaluate(X_normalized, Y, n_neighbors=n_neighbors, n_splits=n_splits, scoring=scoring)
		current_mean_score = scores.mean()
def find_optimal_kvalue(X_normalized, Y, n_splits=10, scoring="f1_weighted", n_neighbors_range=range(1, 100, 2)):
	cross_validation_object = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
	param_grid = {'n_neighbors': list(n_neighbors_range)}

		dict_of_k_scores[n_neighbors] = current_mean_score
	grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=cross_validation_object, scoring=scoring)
	grid_search.fit(X_normalized, Y)

	optimal_n_neighbors = max(dict_of_k_scores, key=dict_of_k_scores.get)
	optimal_n_neighbors = grid_search.best_params_['n_neighbors']
	print("-"*100)
	print(f"The optimal N neighbors value is {optimal_n_neighbors}")
	print("-"*100)