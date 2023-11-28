"""VPN Phase2 Object."""

from fortigate_api.base import Base


class VpnPhase2(Base):
    """VPN Phase2 Object."""

    def __init__(self, rest):
        """VPN Phase1 Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/vpn.ipsec/phase2-interface/")
