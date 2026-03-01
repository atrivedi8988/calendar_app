import math


class LogisticRegressionScratch:
    def __init__(self, lr: float = 0.08, epochs: int = 220):
        self.lr = lr
        self.epochs = epochs
        self.weights: list[float] = []
        self.bias = 0.0

    @staticmethod
    def _sigmoid(x: float) -> float:
        x = max(-35.0, min(35.0, x))
        return 1.0 / (1.0 + math.exp(-x))

    def fit(self, x: list[list[float]], y: list[int]) -> None:
        n_samples = len(x)
        n_features = len(x[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            dw = [0.0] * n_features
            db = 0.0
            for xi, yi in zip(x, y):
                linear = sum(wj * xij for wj, xij in zip(self.weights, xi)) + self.bias
                pred = self._sigmoid(linear)
                error = pred - yi
                for j in range(n_features):
                    dw[j] += error * xi[j]
                db += error

            for j in range(n_features):
                self.weights[j] -= self.lr * (dw[j] / n_samples)
            self.bias -= self.lr * (db / n_samples)

    def predict_proba(self, x: list[list[float]]) -> list[float]:
        probs = []
        for xi in x:
            linear = sum(wj * xij for wj, xij in zip(self.weights, xi)) + self.bias
            probs.append(self._sigmoid(linear))
        return probs


def row_to_features(row: dict) -> list[float]:
    tod = row["time_of_day"]
    return [
        float(row["preference_match"]),
        float(row["popularity"]),
        float(row["margin_pct"]),
        float(row["inventory_priority"]),
        float(row["prep_time_min"]) / 45.0,
        float(row["cart_total"]) / 500.0,
        float(row["is_weekend"]),
        1.0 if tod == "breakfast" else 0.0,
        1.0 if tod == "lunch" else 0.0,
        1.0 if tod == "snacks" else 0.0,
        1.0 if tod == "dinner" else 0.0,
    ]
