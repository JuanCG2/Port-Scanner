from port_scanner import get_open_ports
import unittest
from test_module import PortScannerTests

# Manual tests
if __name__ == "__main__":
    # Example calls from the spec
    print("=== Test 1: IP range ===")
    print(get_open_ports("209.216.230.240", [440, 445]))

    print("\n=== Test 2: URL range ===")
    print(get_open_ports("scanme.nmap.org", [20, 80]))

    print("\n=== Test 3: Verbose mode ===")
    print(get_open_ports("scanme.nmap.org", [20, 80], True))

    print("\n=== Test 4: Invalid hostname ===")
    print(get_open_ports("invalid.invalidhostname.xyz", [80, 80]))

    print("\n=== Test 5: Invalid IP ===")
    print(get_open_ports("266.255.9.10", [80, 80]))

    print("\n=== Running unit tests ===")
    unittest.main(argv=[""], exit=False, verbosity=2)