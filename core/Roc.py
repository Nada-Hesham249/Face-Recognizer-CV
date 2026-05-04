
import numpy as np
import matplotlib.pyplot as plt


class ROC_Curve:
    def __init__(self, model):
        self.model = model

    def get_scores(self, X):
        # Note: if your model returns distances, negate decision_function(X)
        # so the values are treated like confidence scores.
        return self.model.decision_function(X)

    def compute_binary_roc(self, y_true, y_scores):
        # Sort scores from highest to lowest.
        sorted_idx = np.argsort(y_scores)[::-1]
        y_true_sorted = y_true[sorted_idx]
        y_scores_sorted = y_scores[sorted_idx]

        # Use thresholds from highest to lowest so the curve starts at (0, 0).
        thresholds = np.unique(y_scores_sorted)[::-1]

        # Start the curve at (0, 0).
        tpr_list = [0.0]
        fpr_list = [0.0]

        total_positive = np.sum(y_true == 1)
        total_negative = np.sum(y_true == 0)

        for thresh in thresholds:
            preds = (y_scores_sorted >= thresh).astype(int)

            tp = np.sum((preds == 1) & (y_true_sorted == 1))
            fp = np.sum((preds == 1) & (y_true_sorted == 0))

            tpr = tp / total_positive if total_positive else 0
            fpr = fp / total_negative if total_negative else 0

            tpr_list.append(tpr)
            fpr_list.append(fpr)

        return np.array(fpr_list), np.array(tpr_list)

    def compute_macro_roc(self, X, y):
        """
        Build ONE ROC curve (macro-average)
        """
        y_scores = self.get_scores(X)
        n_classes = y_scores.shape[1]

        all_fpr = []
        all_tpr = []

        # Compute a one-vs-rest ROC curve for each class.
        for i in range(n_classes):
            y_true_bin = (y == i).astype(int)
            y_score_bin = y_scores[:, i]

            fpr, tpr = self.compute_binary_roc(y_true_bin, y_score_bin)

            all_fpr.append(fpr)
            all_tpr.append(tpr)

        # Use a shared FPR grid from 0 to 1.
        mean_fpr = np.linspace(0, 1, 100)
        mean_tpr = np.zeros_like(mean_fpr)

        # Interpolate and average across classes.
        for i in range(n_classes):
            mean_tpr += np.interp(mean_fpr, all_fpr[i], all_tpr[i])

        mean_tpr /= n_classes

        # Ensure the curve starts at 0 and ends at 1.
        mean_tpr[0] = 0.0
        mean_tpr[-1] = 1.0

        return mean_fpr, mean_tpr

    def plot_roc(self, X, y, save_path=None):
        fpr, tpr = self.compute_macro_roc(X, y)

        plt.figure()

        # Plot the ROC curve in blue.
        plt.plot(fpr, tpr, lw=3, label="Macro-Average ROC", color='dodgerblue')
        
        plt.plot([0, 1], [0, 1], 'k--')

        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve)")
        plt.legend(loc="lower right")

        # Add a light dashed grid for readability.
        plt.grid(True, linestyle='--', alpha=0.6)

        if save_path:
            plt.savefig(save_path)
            plt.close()
            return save_path

        plt.show()