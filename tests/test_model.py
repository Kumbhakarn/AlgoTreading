import pytest
from src.model import build_model

def test_build_model():
    model = build_model(4)  # Assume 4 features
    assert model.input.shape[1] == 4
    assert len(model.layers) == 5  # Including dropout layers