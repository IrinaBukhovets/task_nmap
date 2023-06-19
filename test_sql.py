import nmap3


nmap = nmap3.Nmap()
ressults = nmap.nmap_version_detection("host", args="-sV --script=http-sql-injection 65.61.137.117")