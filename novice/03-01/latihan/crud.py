#!/usr/bin/env python3

import motor.motor_tornado

client = motor.motor_tornado.MotorClient("mongodb://localhost:27017")

db = client["test-database"]

print(db)