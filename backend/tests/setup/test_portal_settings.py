"""Portal settings tests."""

from plone import api


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    def test_portal_title(self, portal):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        assert value == "Intranet da Lactec"

    def test_navigation_depth(self, portal):
        """Test navigation depth."""
        value = api.portal.get_registry_record("plone.navigation_depth")
        assert value == 3
