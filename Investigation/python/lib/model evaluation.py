from sklearn.metrics import *
import numpy

'''
data = {
		y_predict: numpy,
		y_true: numpy
}
'''


class Evaluator:
	@classmethod
	def evaluate(cls, model_type, **kwarg):
		match model_type:
			case "TabularEvaluation":
				return cls.evaluate_tabular(**kwarg)
			case "RegressionEvaluation":
				return cls.evaluate_regressor(**kwarg)
			case "ClassificationEvaluation":
				return cls.evaluate_classifier(**kwarg)
			case "ForecastingEvaluation":
				return cls.evaluate_forecaster(**kwarg)
			case "EvaluationSlice":
				return cls.evaluate_slice(**kwarg)

	@classmethod
	def evaluate_tabular(cls, **kwarg):
		# TODO:Implement
		raise NotImplemented

	@classmethod
	def evaluate_regressor(cls, **kwargs) -> dict:
		y_true = kwargs.get("y_true")
		y_pred = kwargs.get("y_pred")
		scores = {
			"rootMeanSquaredError": mean_squared_error(y_true, y_pred, squared=False),
			"meanAbsoluteError": mean_absolute_error(y_true, y_pred),
			"meanAbsolutePercentageError": mean_absolute_percentage_error(y_true, y_pred),
			"rSquared": r2_score(y_true, y_pred),
			"rootMeanSquaredLogError": mean_squared_log_error(y_true, y_pred, squared=False)

		}
		return scores

	@classmethod
	def evaluate_classifier(cls, **kwargs) -> dict:
		y_true = kwargs.get("y_true")
		y_pred = kwargs.get("y_pred")
		classifier_type = kwargs.get("classifier_type")
		scores = dict()
		match classifier_type:
			case "binary":
				scores = {
					"auRoc": roc_auc_score(y_true, y_pred, multi_class="raise"),
					"logLoss": log_loss(y_true, y_pred),
					"confidenceMetrics": cls.confidence_metrics(y_true, y_pred, **kwargs),
				}
			case "multiclass":
				scores = {
					"auRoc": roc_auc_score(y_true, y_pred, multi_class="ovr"),
					"logLoss": log_loss(y_true, y_pred),
					"confidenceMetrics": cls.confidence_metrics(y_true, y_pred, **kwargs),
				}
			case "multilabel":
				scores = {
					"auRoc": "", 		# TODO:Implement
					"logLoss": log_loss(y_true, y_pred),
					"confidenceMetrics": cls.confidence_metrics(y_true, y_pred, **kwargs),
				}

		return scores

	@classmethod
	def evaluate_forecaster(cls, **kwargs):
		y_true = kwargs.get("y_true")
		y_pred = kwargs.get("y_pred")
		scores = {
			"rootMeanSquaredError": mean_squared_error(y_true, y_pred, squared=False),
			"meanAbsoluteError": mean_absolute_error(y_true, y_pred),
			"meanAbsolutePercentageError": mean_absolute_percentage_error(y_true, y_pred),
			"rSquared": r2_score(y_true, y_pred),
			"rootMeanSquaredLogError": mean_squared_log_error(y_true, y_pred, squared=False),
			"quantileMetrics": cls.quantile_metrics(y_true, y_pred, **kwargs)
		}

		return scores

	@classmethod
	def confidence_metrics(cls, y_true, y_pred, **kwargs) -> list:
		start = kwargs.get("cm_start")
		stop = kwargs.get("cm_stop")
		step = kwargs.get("cm_step")
		confidence_metrics = [
			{
				"confidenceThreshold": threshold,
				"recall": recall_score(y_true, y_pred),
				"precision": precision_score(y_true, y_pred),
				# TODO:Implement
				# "falsePositiveRate": "",
				# "f1Score": "",
				# "recallAt1": "",
				# "precisionAt1": "",
				# "falsePositiveRateAt1": "",
				# "f1ScoreAt1": "",
				# "truePositiveCount": "",
				# "falsePositiveCount": "",
				# "falseNegativeCount": "",
				# "trueNegativeCount": "",
			}
			for threshold in numpy.arange(start, stop, step)
		]

		return confidence_metrics

	@classmethod
	def quantile_metrics(cls, y_true, y_pred, **kwargs):
		start = kwargs.get("cm_start")
		stop = kwargs.get("cm_stop")
		step = kwargs.get("cm_step")
		sample_weight = kwargs.get("sample_weight")
		quantile_metrics = [
			{
				"quantile": quantile,
				"scaledPinballLoss": mean_pinball_loss(y_true, y_pred),
				"observedQuantile": cls.observed_quantile(y_true, y_pred),
				"weightedAbsolutePercentageError": mean_absolute_percentage_error(y_true, y_pred, sample_weight=sample_weight),
				"rootMeanSquaredPercentageError": mean_squared_error(y_true, y_pred, squared=False)
			}
			for quantile in numpy.arange(start, stop, step)
		]
		return quantile_metrics

	@classmethod
	def observed_quantile(cls, y_true, y_pred):
		# TODO:Implement
		raise NotImplemented

	@classmethod
	def evaluate_slice(cls, **kwargs):
		# TODO:Implement
		y_true = kwargs.get("y_true")
		raise NotImplemented


if __name__ == "__main__":
	e = Evaluator()
