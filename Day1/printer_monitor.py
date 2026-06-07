from pysnmp.hlapi import (
    getCmd,
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity
)

class PrinterMonitor:
    def __init__(self, host, community, snmp_ver):
        self.host = host
        self.community = community
        self.snmp_ver = snmp_ver

    def _get(self, oid):
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(self.community),
            UdpTransportTarget((self.host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
        error_indication, error_status, error_index, var_binds = next(iterator)

        if error_indication:
            return None

        for _, value in var_binds:
            return value.prettyPrint()
        
    def get_page_count(self):
        page_count = self._get("1.3.6.1.2.1.43.10.2.1.4.1.1")
        return page_count

    def is_ready(self):
        printer_status = self._get("1.3.6.1.2.1.25.3.5.1.1.1")
        if printer_status == 3:
            return True
        else:
            return False
        
    def has_toner(self):
        toner_level = int(self._get("1.3.6.1.2.1.43.11.1.1.9.1.1"))
        if toner_level > 20:
            return True
        else:
        	return False

        
def main():
    system = PrinterMonitor("localhost", "public", "v2c")
    value = system._get("1.3.6.1.2.1.1.1.0")
    print(value)

if __name__ == "__main__":
    main()