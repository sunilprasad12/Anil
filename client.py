from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException
from scp import SCPClient, SCPException
from io import StringIO


class Client:
    ...

    def upload(self, file, remote_directory):
        """Upload a single file to a remote directory"""
        self.client = self.__connect()
        scp = SCPClient(self.client.get_transport())
        try:
            scp.put(file,
                    recursive=True,
                    remote_path=remote_directory)
        except SCPException:
            raise SCPException.message
        finally:
            scp.close()