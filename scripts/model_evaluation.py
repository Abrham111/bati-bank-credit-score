from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Model Evaluation
def evaluate_model(y_test, y_pred, model_name):
  print(f"{model_name} Performance:")
  print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
  print(f"Precision: {precision_score(y_test, y_pred):.4f}")
  print(f"Recall: {recall_score(y_test, y_pred):.4f}")
  print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")
  print(f"ROC-AUC: {roc_auc_score(y_test, y_pred):.4f}\n")