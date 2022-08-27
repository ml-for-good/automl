class IModel:
    """
      Work flow:
       ┌───────────────┐
       │ Make datasets │
       └───────┬───────┘
               │
       ┌───────▼───────┐
       │ Train model   │
       └───────┬───────┘
               │
       ┌───────▼────────┐
       │ Evaluate model │
       └───────┬────────┘
               │
      ┌────────▼──────────┐
      │ Export best model │
      └────────┬──────────┘
               │
        ┌──────▼────────┐          ▼
        │ Serving model │
        └───────────────┘
      Interface for automl models
    """
    def train(self, dataset, batch_size=8, steps=100):
        raise NotImplemented

    def evaluate(self, dataset, batch_size=8, steps=10):
        raise NotImplemented

    def export(self, format):
        raise NotImplemented
    
    def summary(self):
        raise NotImplemented
