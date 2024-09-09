from flask import Blueprint, request, jsonify
from models import Device
from conection import create_connection, close_connection
import mysql

devices_bp = Blueprint('devices', __name__)

@devices_bp.route('/add_device', methods=['POST'])
def add_device():
    data = request.get_json()
    device = Device.from_dict(data)
    
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO devices (mac_address, name, status, user_id) VALUES (%s, %s, %s, %s)",
            (device.mac_address, device.name, device.status, device.user_id)
        )
        conn.commit()
        device_id = cursor.lastrowid
        device.device_id = device_id
        return jsonify({'message': 'Device added successfully', 'device': device.to_dict()})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        close_connection(conn)

@devices_bp.route('/get')
def a():
    return "aa"