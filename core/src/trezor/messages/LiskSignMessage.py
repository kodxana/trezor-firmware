# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class LiskSignMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 118

    def __init__(
        self,
        *,
        message: bytes,
        address_n: List[int] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.message = message

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('message', p.BytesType, p.FLAG_REQUIRED),
        }
