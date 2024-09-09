class User:
    def __init__(self, username, password, email, pfp, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.pfp = pfp

    def to_dict(self):
        return {
            'id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'pfp': self.pfp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            pfp=data['pfp'],
            user_id=data.get('id')
        )

class Device:
    def __init__(self, mac_address, name, status, user_id, device_id=None):
        self.device_id = device_id
        self.mac_address = mac_address
        self.name = name
        self.status = status
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.device_id,
            'mac_address': self.mac_address,
            'name': self.name,
            'status': self.status,
            'user_id': self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            mac_address=data['mac_address'],
            name=data['name'],
            status=data['status'],
            user_id=data['user_id'],
            device_id=data.get('id')
        )
