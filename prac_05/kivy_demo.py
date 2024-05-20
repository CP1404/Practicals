from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button


class KivyDemo(App):
    """Kivy program to demo some basic interactive functionality."""
    status_text = StringProperty("Hello. Click the buttons :)")

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.counter = 0
        self.names = ["Lindsay", "Osmond", "Paul"]

    def build(self):
        """Construct the dynamic widgets."""
        self.title = "Hello world!"
        self.root = Builder.load_file('kivy_layout.kv')
        for name in self.names:
            button = Button(text=name)
            button.bind(on_press=self.handle_name_button)
            self.root.ids.names_box.add_widget(button)
        return self.root

    def handle_name_button(self, instance):
        """Handle presses on the name button to greet people."""
        print("Hello", instance.text)

    def handle_press(self, amount):
        """Handle presses on the up/down buttons to change counter."""
        self.counter += amount
        self.status_text = f"The count is: {self.counter}"


# Create an instance of the KivyDemo class and start the App running
KivyDemo().run()
