import unittest
from port_scanner import get_open_ports


class PortScannerTests(unittest.TestCase):

    def test_get_open_ports_returns_list(self):
        result = get_open_ports("scanme.nmap.org", [20, 80])
        self.assertIsInstance(result, list)

    def test_get_open_ports_correct_ports(self):
        result = get_open_ports("scanme.nmap.org", [20, 80])
        self.assertIn(22, result)
        self.assertIn(80, result)

    def test_verbose_mode_returns_string(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], True)
        self.assertIsInstance(result, str)

    def test_verbose_contains_header(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], True)
        self.assertIn("Open ports for scanme.nmap.org", result)
        self.assertIn("45.33.32.156", result)

    def test_verbose_contains_port_service(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], True)
        self.assertIn("22", result)
        self.assertIn("ssh", result)
        self.assertIn("80", result)
        self.assertIn("http", result)

    def test_verbose_contains_port_service_header(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], True)
        self.assertIn("PORT     SERVICE", result)

    def test_ip_input(self):
        result = get_open_ports("45.33.32.156", [20, 80])
        self.assertIsInstance(result, list)

    def test_invalid_hostname(self):
        result = get_open_ports("invalid.invalidhostname.xyz", [80, 80])
        self.assertEqual(result, "Error: Invalid hostname")

    def test_invalid_ip(self):
        result = get_open_ports("266.255.9.10", [80, 80])
        self.assertEqual(result, "Error: Invalid IP address")

    def test_verbose_with_ip(self):
        result = get_open_ports("45.33.32.156", [20, 80], True)
        self.assertIsInstance(result, str)
        self.assertIn("45.33.32.156", result)


if __name__ == "__main__":
    unittest.main()