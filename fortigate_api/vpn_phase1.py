"""VPN Phase1 Object."""

from fortigate_api.base import Base


class VpnPhase1(Base):
    """VPN Phase1 Object."""

    def __init__(self, rest):
        """VPN Phase1 Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/vpn.ipsec/phase1-interface/")
