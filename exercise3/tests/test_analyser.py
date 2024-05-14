import pytest
from src.TextAnalyserIndices.analyser import TextMetricsAnalyzer


@pytest.fixture
def empty_text():
    return []


@pytest.fixture
def sample_text():
    return [
        "The old oak tree stood tall and proud against the setting sun.",
        "The faithful dog fervently wagged its tail, exhibiting an eager anticipation for its owner's imminent return to the homestead."
    ]


def test_text_metrics_analyzer(sample_text, empty_text):
    analyzer = TextMetricsAnalyzer()
    metrics = analyzer.calculate_text_metrics(sample_text)

    assert len(metrics) == 3
    assert all(isinstance(metric, float) for metric in metrics)

    expected_metrics = (16.0, 1.4375, 0.09375)
    assert metrics == pytest.approx(expected_metrics, abs=0.001)

    # Test with empty text
    with pytest.raises(ValueError):
        analyzer.calculate_text_metrics(empty_text)
