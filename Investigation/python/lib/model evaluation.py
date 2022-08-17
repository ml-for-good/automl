from sklearn.metrics import *

classification = 'classification'

class ModelEvaluation:
	def __init__(self, model_type):
		self.model_type = model_type
	
	def evaluate(self, y_true, y_predict):
		def evaluate_classification():
			scores = {
				'accuracy': accuracy_score(y_true, y_predict),
				'balanced_accuracy': balanced_accuracy_score(y_true, y_predict),
				'top_k_accuracy': top_k_accuracy_score(y_true,y_predict),
				'average_precision': average_precision_score(y_true, y_predict),
				'neg_brie_score': brier_score_loss(y_true,y_predict),
				'f1': f1_score(y_true,y_predict),
				'neg_log_loss': log_loss(y_true,y_predict)
				'precision': precision_score(y_true,y_predict),
				'recall': recall_score(y_true, y_predict),
				'jaccard': jaccard_score(y_true, y_predict),
				'roc_auc': roc_auc_score(y_true,y_predict)
			}
			return scores
		
		def evaluate_regression():
			pass
		
		if self.model_type == classification:
			return evaluate_classification()
		
		
			
