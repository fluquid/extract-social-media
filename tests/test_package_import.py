import extract_social_media


def test_package_metadata():
    assert extract_social_media.__author__
    assert extract_social_media.__email__
    assert extract_social_media.__version__
