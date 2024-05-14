import pytest
from src.TextAnalyserIndices.indices import FleschKincaidGradeLevel, GunningFogIndex


@pytest.fixture
def empty_text():
    return []


@pytest.fixture
def sample_text():
    return [
        "The old oak tree stood tall and proud against the setting sun.",
        "The faithful dog fervently wagged its tail, exhibiting an eager anticipation for its owner's imminent return to the homestead."
    ]


def test_flesch_kincaid_grade_level():
    fk_index = FleschKincaidGradeLevel()
    index_value = fk_index.calculate((10, 3, 0.1))
    assert isinstance(index_value, float)

    expected_index_value = 23.71
    assert index_value == pytest.approx(expected_index_value, abs=0.001)

    interpretation = fk_index.interpret(index_value)
    expected_interpretation = "The text is for skilled readers. For example, an academic paper."
    assert interpretation == expected_interpretation


def test_gunning_fog_index():
    gf_index = GunningFogIndex()
    index_value = gf_index.calculate((10, 3, 0.1))
    assert isinstance(index_value, float)

    expected_index_value = 8.0
    assert index_value == pytest.approx(expected_index_value, abs=0.001)

    interpretation = gf_index.interpret(index_value)
    expected_interpretation = "A text is considered ideal for average readers."
    assert interpretation == expected_interpretation
