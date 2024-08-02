class Device:

	def is_enabled(self):
		pass

	def enable(self):
		pass

	def disable(self):
		pass

	def get_volume(self) -> int:
		pass

	def set_volume(self, percent: int):
		pass

	def get_channel(self) -> int:
		pass

	def set_channel(self, channel: int):
		pass


class TV(Device):
	def __init__(self):
		self.on = False
		self.volume = 30
		self.channel = 1

	def is_enabled(self) -> bool:
		return self.on

	def enable(self):
		self.on = True
		print("TV is now ON")

	def disable(self):
		self.on = False
		print("TV is now OFF")

	def get_volume(self) -> int:
		return self.volume

	def set_volume(self, percent: int):
		self.volume = percent
		print(f"TV volume set to {self.volume}")

	def get_channel(self) -> int:
		return self.channel

	def set_channel(self, channel: int):
		self.channel = channel
		print(f"TV channel set to {self.channel}")


class Radio(Device):
	def __init__(self):
		self.on = False
		self.volume = 30
		self.channel = 1

	def is_enabled(self) -> bool:
		return self.on

	def enable(self):
		self.on = True
		print("Radio is now ON")

	def disable(self):
		self.on = False
		print("Radio is now OFF")

	def get_volume(self) -> int:
		return self.volume

	def set_volume(self, percent: int):
		self.volume = percent
		print(f"Radio volume set to {self.volume}")

	def get_channel(self) -> int:
		return self.channel

	def set_channel(self, channel: int):
		self.channel = channel
		print(f"Radio channel set to {self.channel}")


class RemoteControl:

	def __init__(self, device: Device):
		self.device = device

	def toggle_power(self):
		if self.device.is_enabled():
			self.device.disable()
		else:
			self.device.enable()

	def volume_down(self):
		self.device.set_volume(self.device.get_volume() - 10)

	def volume_up(self):
		self.device.set_volume(self.device.get_volume() + 10)

	def channel_down(self):
		self.device.set_channel(self.device.get_channel() - 1)

	def channel_up(self):
		self.device.set_channel(self.device.get_channel() + 1)


# Advanced remote control with additional functionality
class AdvancedRemoteControl(RemoteControl):
	def mute(self):
		self.device.set_volume(0)


def client_code(remote: RemoteControl):
	remote.toggle_power()
	remote.volume_up()
	remote.channel_up()

	remote.toggle_power()


if __name__ == '__main__':
	tv = TV()
	radio = Radio()

	basic_remote = RemoteControl(tv)
	advanced_remote = AdvancedRemoteControl(radio)

	print("Testing basic remote with TV:")
	client_code(basic_remote)

	print("\nTesting advanced remote with Radio:")
	client_code(advanced_remote)
	advanced_remote.mute()
