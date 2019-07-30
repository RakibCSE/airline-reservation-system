import hashlib

from datetime import datetime


def generate_ticket_id(flight):
    encoded_timestamp_now = str(datetime.timestamp(datetime.now())).encode(encoding='utf_8')
    hash_id = hashlib.sha256(encoded_timestamp_now).hexdigest()[-10:].upper()
    return "{}-{}".format(flight, hash_id)
