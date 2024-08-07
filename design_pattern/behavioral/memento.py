class Memento:
	def __init__(self, state):
		self._state = state

	def get_state(self):
		return self._state


# Originator
class TextEditor:
	def __init__(self):
		self._text = ""

	def type(self, words):
		self._text += " " + words

	def get_text(self):
		return self._text

	def create_memento(self):
		return Memento(self._text)

	def restore(self, memento):
		self._text = memento.get_state()


# Caretaker
class EditorHistory:
	def __init__(self):
		self._mementos = []

	def save(self, editor):
		self._mementos.append(editor.create_memento())

	def undo(self, editor):
		if not self._mementos:
			return
		memento = self._mementos.pop()
		editor.restore(memento)


if __name__ == '__main__':
	# Create the Originator
	editor = TextEditor()

	# Create the Caretaker
	history = EditorHistory()

	# Type some text and save state
	editor.type("Hello")
	history.save(editor)
	print(editor.get_text())  # Output: " Hello"

	# Type more text and save state
	editor.type("World")
	history.save(editor)
	print(editor.get_text())  # Output: " Hello World"

	# Type even more text
	editor.type("This is a text editor.")
	print(editor.get_text())  # Output: " Hello World This is a text editor."

	# Undo the last change
	history.undo(editor)
	print(editor.get_text())  # Output: " Hello World"

	# Undo another change
	history.undo(editor)
	print(editor.get_text())  # Output: " Hello"


"""
+--------------------+     +--------------------+
|   Originator       |<--->|     Memento        |
+--------------------+     +--------------------+
|+ setState(state)   |     |+ getState()        |
|+ createMemento()   |     +--------------------+
|+ restoreMemento(m) |
+--------------------+
        ^
        |
        |
+--------------------+
|    Caretaker       |
+--------------------+
|+ saveState(o: O)   |
|+ restoreState(o: O)|
+--------------------+
"""
