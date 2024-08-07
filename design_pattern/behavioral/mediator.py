from abc import ABC

class Mediator(ABC):

	def notify(self, sender: object, event: str):
		pass


class HomeAutoMediator(Mediator):
	def __init__(self):
		self.lights = None
		self.thermostat = None
		self.alarm = None

	def notify(self, sender, event):
		if event == "motion_detected":
			print("Hub: Motion detected! Turning on lights and setting thermostat to comfortable temperature.")
			self.lights.turn_on()
			self.thermostat.set_temperature(22)
		elif event == "no_motion":
			print("Hub: No motion detected. Turning off lights.")
			self.lights.turn_off()
		elif event == "fire_detected":
			print("Hub: Fire detected! Triggering alarm.")
			self.alarm.trigger()


class Light:

	def __init__(self, mediator):
		self.status = False
		self.mediator = mediator
		self.mediator.lights = self

	def turn_on(self):
		self.status = True

	def turn_off(self):
		self.status = False

	def motion_detected(self):
		self.mediator.notify(self, 'motion_detected')

	def no_motion(self):
		self.mediator.notify(self, 'no_motion')


class Thermostat:
	def __init__(self, mediator):
		self.mediator = mediator
		self.mediator.thermostat = self
		self.temperature = 0

	def set_temperature(self, number):
		self.temperature = number
		print(f"Thermostat: Setting temperature to {number} degrees.")


class Alarm:
	def __init__(self, mediator):
		self.mediator = mediator
		self.mediator.alarm = self
		self.temperature = 0

	def trigger(self):
		print("Alarm: Triggering alarm.")

	def detect_fire(self):
		print("Alarm: Fire detected.")
		self.mediator.notify(self, "fire_detected")


if __name__ == '__main__':
	mediator = HomeAutoMediator()

	light = Light(mediator)
	thermostat = Thermostat(mediator)
	alarm = Alarm(mediator)

	light.motion_detected()
	alarm.detect_fire()
	light.no_motion()




"""
+--------------------+
|    Mediator        |
+--------------------+
|+ notify(sender, ev)|-----------------+
+--------------------+                 |
                                      |
                                      |
+--------------------+          +------------------------+
| Colleague          |          |   ConcreteMediator     |
+--------------------+          +------------------------+
|+ setMediator(m: M) |<>------- |                        |
|+ notify(event)     |          |+ notify(sender, event) |
+--------------------+          +------------------------+
                                      |
                                      |
                                      |
                                      |
+-----------------------+  +----------------------+
| ConcreteColleague1    |  | ConcreteColleague2   |
+-----------------------+  +----------------------+
|+ notify(event)        |  |+ notify(event)       |
+-----------------------+  +----------------------+

"""