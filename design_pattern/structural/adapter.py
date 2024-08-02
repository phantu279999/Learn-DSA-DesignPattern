class Target:
	def request(self):
		return "Target: The default target's behavior."


class JustReadASCII:
	def specific_request(self):
		return "72 101 108 108 111 32 87 111 114 108 100 33"


class Adapter(Target, JustReadASCII):
	def string_to_ascii(self, string):
		ans = []
		for s in string:
			ans.append(str(ord(s)))
		return " ".join(ans)

	def ascii_to_string(self, string):
		ans = ""
		for s in string.split(" "):
			ans += chr(int(s))
		return ans

	def request(self):
		return f"Adapter: (TRANSLATED): {self.ascii_to_string(self.specific_request())}"


def client_code(target: Target):
	print(target.request())


if __name__ == '__main__':
	adapter = Adapter()
	client_code(adapter)
	# Adapter: (TRANSLATED): Hello World!
