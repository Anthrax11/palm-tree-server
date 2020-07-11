from module import db


class User(db.Model):
    """Stores user data"""
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    devices = db.relationship('Device', backref='device', lazy=True) #setting relationship with Device

    def __repr__(self):
        return f"'{self.username}', '{self.email}'"


class Device(db.Model):
    """Stores devices"""
    device_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(24), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    sensors = db.relationship('Sensor', backref='sensor', lazy=True) #setting relationship with Sensor

    def __repr__(self):
        return f"'{self.device_name}', '{self.owner}'"


class Sensor(db.Model):
    """Stores sensors for each device"""
    sensor_id = db.Column(db.Integer, primary_key=True)
    sensor_name = db.Column(db.String(24), nullable=False, unique=True)
    sensor_type = db.Column(db.String(24))
    device = db.Column(db.Integer, db.ForeignKey('device.device_id'), nullable=False)
    data = db.relationship('Data', backref='data', lazy=True) #setting relationship with Data

    def __repr__(self):
        return f"'{self.sensor_name}', '{self.sensor_type}', '{self.device}'"


class Data(db.Model):
    """Stores sensor data"""
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'), nullable=False)
    data_type = db.Column(db.String(24), nullable=False)
    data = db.Column(db.String(64))
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"'{self.sensor_id}', '{self.data_type}', '{self.data}', '{self.time}'"