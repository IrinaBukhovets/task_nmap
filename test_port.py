import nmap


def test_port():
    nmScan = nmap.PortScanner()
    res = nmScan.scan('65.61.137.117', '443')
    assert res['scan']['65.61.137.117']['443']['state'] == "open"