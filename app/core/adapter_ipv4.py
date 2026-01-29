import socket

import urllib3.util.connection as connection


def force_ipv4():
    """Force l'utilisation de l'IPv4 pour toutes les requêtes requests."""

    def allowed_gai_family():
        return socket.AF_INET

    connection.allowed_gai_family = allowed_gai_family
