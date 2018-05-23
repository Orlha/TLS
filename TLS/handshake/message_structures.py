from basic_structures import Structure, FixedLenStructure, NoLengthStructure, VariableLenStructure, ListStructure


class HandshakeMessageStructure:
    def __init__(self, msg_type, body_children):
        self._msg_type = msg_type
        self._structure = NoLengthStructure([FixedLenStructure('msg_type', 1), VariableLenStructure('body', 3, body_children)])

    def parse_bytes(self, bytes_str):
        result, _ = self._structure.parse_bytes(bytes_str)
        assert result['msg_type'] == self._msg_type
        return result['body']

    def to_bytes(self, data):
        data = {'msg_type': self._msg_type, 'body': data}
        return self._structure.to_bytes(data)

    @staticmethod
    def get_type(bytes_str):
        return bytes_str[:1]


server_version_structure = NoLengthStructure([FixedLenStructure('major', 1), FixedLenStructure('minor', 1)], 'server_version')
random_structure = FixedLenStructure('random', 32)
session_id_structure = VariableLenStructure('session_id', 1)
cipher_suite = FixedLenStructure('cipher_suite', 2)
cipher_suites = ListStructure('cipher_suites', 2, FixedLenStructure('CipherSuite', 2), 2)
compression_method_structure = FixedLenStructure('compression_method', 1)
compression_methods_structure = ListStructure('compression_methods', 1, FixedLenStructure('CompressionMethod', 1), 1)
supported_signature_algorithms_structure = ListStructure(
    'supported_signature_algorithms', 2,
    NoLengthStructure([FixedLenStructure('hash', 1), FixedLenStructure('signature', 1)], 'SignatureAndHashAlgorithm'),
    2,
)
renegotiated_connection_extension_structure = NoLengthStructure(
    [
        FixedLenStructure('extension_type', 2),
        VariableLenStructure('extension_data', 2, [VariableLenStructure('renegotiated_connection', 1)])
    ],
    'Extention',
)
signature_algorithms_extension_structure = NoLengthStructure(
    [
        FixedLenStructure('extension_type', 2),
        VariableLenStructure('extension_data', 2, [supported_signature_algorithms_structure])
    ],
    'Extention',
)


server_hello_children = [
    server_version_structure,
    random_structure,
    session_id_structure,
    cipher_suite,
    compression_method_structure,
    ListStructure(
        'extensions', 2,
        renegotiated_connection_extension_structure,
        1,
    )
]

client_hello_children = [
    server_version_structure,
    random_structure,
    session_id_structure,
    cipher_suites,
    compression_methods_structure,
    ListStructure(
        'extensions', 2,
        [signature_algorithms_extension_structure, renegotiated_connection_extension_structure]
    )
]

certificate_children = [
    ListStructure('certificate_list', 3, VariableLenStructure('ASN.1Cert', 3), 1)
]

certificate_request_children = [
    ListStructure('certificate_types', 1, FixedLenStructure('ClientCertificateType', 1), 2),
    supported_signature_algorithms_structure,
    VariableLenStructure('certificate_authorities', 2)
]

SERVER_HELLO_MESSAGE = HandshakeMessageStructure(b'\x02', server_hello_children)
CLIENT_HELLO_MESSAGE = HandshakeMessageStructure(b'\x01', client_hello_children)
CLIENT_KEY_EXCHANGE_MESSAGE = HandshakeMessageStructure(b'\x10', [FixedLenStructure('exchange_keys', 149)])
CERTIFICATE_MESSAGE = HandshakeMessageStructure(b'\x0b', certificate_children)
CERTIFICATE_REQUEST_MESSAGE = HandshakeMessageStructure(b'\x0d', certificate_request_children)
SERVER_HELLO_DONE_MESSAGE = HandshakeMessageStructure(b'\x0e', [])
FINISHED_MESSAGE = HandshakeMessageStructure(b'\x14', [FixedLenStructure('verify_data', 32)])
