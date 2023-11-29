"""RouterStatic Object."""

from fortigate_api.base import Base


class RouterStatic(Base):
    """RouterStatic Object."""

    def __init__(self, rest):
        """RouterStatic Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/router/static/")
