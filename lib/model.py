# import autokeras as ak
# import tensorflow as tf
import numpy as np

REGRESSION = 'regression'
CLASSIFICATION = 'classification'

SAVED_MODEL = 'saved_model'
TFTRT = 'tftrt'
TFLITE = 'tflite'
ONNX = 'onnx'


# class StructuredDataModel:
#     """
#       Work flow:
#        ┌───────────────┐
#        │ Make datasets │
#        └───────┬───────┘
#                │
#        ┌───────▼───────┐
#        │ Train model   │
#        └───────┬───────┘
#                │
#        ┌───────▼────────┐
#        │ Evaluate model │
#        └───────┬────────┘
#                │
#       ┌────────▼──────────┐
#       │ Export best model │
#       └────────┬──────────┘
#                │
#         ┌──────▼────────┐          ▼
#         │ Serving model │
#         └───────────────┘
#       Train model from structured data, it will tune hparams automatically and do some nas searches, it will record training logs in a csv file.
#       Args:
#         max_trials: Int. The maximum number of different Keras Models to try.
#           The search may finish before reaching the max_trials.
#         task: task type.
#     """

#     def __init__(self, max_trials, task):
#         if task == REGRESSION:
#             self.model = ak.StructuredDataRegressor(max_trials=max_trials)
#         elif task == CLASSIFICATION:
#             self.model = ak.StructuredDataClassifier(max_trials=max_trials)

#         else:
#             raise NotImplemented
#         self.callbacks = [
#             tf.keras.callbacks.CSVLogger(
#                 tf.io.gfile.join(self.model.directory, 'training_log.csv')),
#             tf.keras.callbacks.ProgbarLogger()
#         ]

#     def train(self, dataset, batch_size=8, epochs=10):
#         """
#           Args:
#             dataset: Train dataset, tf dataset format.
#             batch_size: Train batch size, integer.
#             epochs: Train loops, integer.
#         """
#         return self.model.fit(dataset,
#                               epochs=epochs,
#                               batch_size=batch_size,
#                               callbacks=self.callbacks)

#     def evaluate(self, dataset):
#         return self.model.evaluate(dataset)

#     def export(self, format=SAVED_MODEL):
#         model = self.model.export_model()
#         if format == SAVED_MODEL:
#             tf.saved_model.save(
#                 model, tf.io.gfile.join(self.model.directory, 'saved_model'))
#         elif format == TFLITE:
#             converter = tf.lite.TFLiteConverter.from_keras_model(model)
#             converter.optimizations = {tf.lite.Optimize.DEFAULT}
#             tflite_model = converter.convert()
#             tf.io.write_file(
#                 tf.io.gfile.join(self.model.directory, 'model.tflite'),
#                 tflite_model)
#         else:
#             raise NotImplemented


class TextModel:
    pass


class ImageModel:
    pass


class measure_tool_classification:
    def __init__(self,actual_y,pre_y):
        self.actual_y = actual_y
        self.pre_y = pre_y
        self.TP = 0
        self.FN = 0
        self.FP = 0
        self.TN = 0
    
    def Multiple2TF(self):#多分类转换成二分类(待完成)
        return None

    def check_legality(self):#判断数组长度是否一致
        return True if (len(self.actual_y)==len(self.pre_y)) else False

    def transform_datatype(self,array):# list -> np.ndarray
        if type(array) != np.ndarray:
            return np.asarray(array)
        return array
    
    def count_num(self): #先计数
        # 时间复杂度O(n),空间复杂度O(1)
        #
        #                            predict
        #                      Positive   Negative  
        #                    ----------------------
        # actual  Positive  |     TP    |    FP    |
        #         Negative  |     FN    |    TN    |
        #
        #
        self.actual_y = self.transform_datatype(self.actual_y)
        self.pre_y = self.transform_datatype(self.pre_y)
        if self.check_legality()==True:
            total_num = len(self.actual_y)

            if total_num ==0:#长度为0，数组为空
                raise 'empty array for both of the actural_y and predicted_y'

            if self.TN!=0 or self.TP!=0 or self.FN!=0 or self.FP!=0:# 重置 矩阵计数
                self.TN,self.TP,self.FN,self.FP=0,0,0,0

            for i in range(total_num):
                if self.actual_y[i]==self.pre_y[i]==0:
                    self.TN += 1
                elif self.actual_y[i]==self.pre_y[i]:
                    self.TP += 1
                elif self.actual_y[i]>0:
                    self.FN += 1
                else:
                    self.FP += 1
            return self
        else:
            raise 'len(actual_y) != len(predicted_y)'
        
    def cal_accuracy(self):
        return round((self.TP+self.TN)/(self.TP+self.TN+self.FP+self.FN),6)

    def cal_precision(self):
        return round(self.TP/(self.TP+self.FP),6)
    
    def cal_recall(self):
        return round(self.TP/(self.TP+self.FN),6)
    
    def cal_F1(self):
        return round(2*self.TP/(self.TP+self.FN+self.TP+self.FP),6)

pre_y=     [1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1]
actual_y = [1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0]
Test = measure_tool_classification(actual_y,pre_y)
Test.count_num()
print(Test.FN)#10
print(Test.cal_accuracy())#0.542857
print(Test.cal_precision())#0.6
print(Test.cal_recall())#0.473684
print(Test.cal_F1())#0.529412