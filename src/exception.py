class StockDataFetchError(Exception):
    """Raised when there is an error fetching stock data."""
    def __init__(self, message="Error fetching stock data"):
        self.message = message
        super().__init__(self.message)

class ModelPredictionError(Exception):
    """Raised when there is an error making predictions with the model."""
    def __init__(self, message="Error making prediction"):
        self.message = message
        super().__init__(self.message)

class InvalidDataError(Exception):
    """Raised when the input data is invalid or incomplete."""
    def __init__(self, message="Invalid or incomplete data provided"):
        self.message = message
        super().__init__(self.message)

class ModelLoadingError(Exception):
    """Raised when there is an error loading the pre-trained model."""
    def __init__(self, message="Error loading the model"):
        self.message = message
        super().__init__(self.message)